import os, re, markdown2
import mdw, mdw_report

def check_cwd():
	if os.path.exists(mdw.mark_fn) == False:
		mdw_report.error('mkdwiki2\'s mark file not found.this not was marked as a mkdwiki2-work-directory.')

# init a wiki project 

def init():
	try:
		os.mkdir(mdw.src_dirname)
	except:
		mdw_report.error('failed to mkdir \''+mdw.src_dirname+'\'')
	
	import shutil
	shutil.copytree(os.path.join(mdw.mdw_dir_path, 'static'), 'static')
	shutil.copyfile(os.path.join(mdw.mdw_dir_path, 'tpl.html'), os.path.join(mdw.src_dirname, 'tpl.html'))
	open(mdw.mark_fn, 'w').write('DO NOT Delete this file.')
	mdw_report.success('''
source file directory : src
output html directory : .
template file : src/tpl.html
enjoy!''')

''' convert single src file to html
argv: 
	src_fp  source file path
	tpl_c   template file content
'''
def convert(src_fp, tpl_c):
	# read source file
	f = open(src_fp)
	c = f.read()
	f.close()

	# decode from utf-8
	
	try:
		c = c.decode(mdw.encoding)
	except:
		mdw_report.warning('skip', 'file \''+src_fp+'\' not encoding '+mdw.encoding)
		mdw.skip_files[src_fp] = 'encoding not '+mdw.encoding # encoding error
		mdw.rel_build_files.remove(src_fp)
		return 
	# get title
	t = mdw.title_re.search(c)
	if t :
		title = t.group(1).strip()
		c = c[:t.start()] + c[t.end():]
	else:
		title = 'Untitled'
	
	# html_root
	html_root = os.path.relpath(mdw.src_dirname, os.path.normpath(os.path.dirname(src_fp)))
	
	# markdown2 convert
	c = markdown2.markdown(c, extras = ['fenced-code-blocks', 'toc'])
	
	# replace tpl_c
	tpl_c = tpl_c.replace(u'%title%', title)  
	tpl_c = tpl_c.replace(u'%html_root%',html_root+u'/')
	c = c.replace(u'[TOC]', '<div class="toc">'+c.toc_html+'</div>', 1) if c.toc_html else c
	c = tpl_c.replace(u'%content%', c)
	
	#output
	out_p = mdw.html_re.sub(r'\1.html', os.path.relpath(src_fp, mdw.src_dirname))
	out_dirname = os.path.dirname(out_p)
	if out_dirname and os.path.exists(out_dirname) == False:
		os.makedirs(out_dirname)
	
	#write
	f = open(out_p, 'w')
	f.write(c.encode(mdw.encoding))
	f.close()
	mdw_report.success(src_fp+' -> '+out_p)

# --- get all files in a dir ---
def getfilelist(d):
	filelist = list()
	for i in os.listdir(d):
		f = os.path.join(d,i)
		if os.path.isdir(f):
			filelist.extend(getfilelist(f))
		else:
			filelist.append(f)
	return filelist


def build():
	check_cwd()
	
	# --------------- init filelist  -----------------
	if os.path.exists(mdw.src_dirname) and os.path.isdir(mdw.src_dirname):
		filelist = getfilelist(mdw.src_dirname)
	else:
		mdw_report.error('sourc file directory not found.')
	# ----------------- filter out mdw ignore files -------
	import mdw_ignore
	filelist = filter(mdw_ignore.ignore_mdw, filelist)
	
	# -------- filter out user file -----
	mdw_ignore.user_ignore_rules_gen() # generate user ignore rules list
	filelist = filter(mdw_ignore.ignore_user, filelist)

	# ----------------- get cache ------------------
	import mdw_cache
	
	cache_dict = mdw_cache.get_cache()
	#-----------filter out exists file
	cache_dict = dict((k, v) for k, v in cache_dict.iteritems() if os.path.exists(k))
	
	# ----------------- read template ------------
	
	if os.path.exists(mdw.tpl_path):
		try:
			tpl_c = open(mdw.tpl_path).read().decode(mdw.encoding)
		except:
			mdw_report.error('template file \''+mdw.tpl_path+'\' not '+mdw.encoding+' encode')
	else:
		tpl_c = u'%content%'
	
	# --------- filter out not modefied files in filelist ---------
	
	m_list = filter(lambda x:mdw_cache.ifilter(cache_dict, x), filelist)
	
	
	mdw.rel_build_files = m_list[:] #make a copy of m_list to make log
	
	# ---------- build ------------
	map(convert, m_list, (tpl_c, )*len(m_list))
	
	# ---------- write cache --------
	
	mdw_cache.write_cache(dict((k, os.stat(k).st_mtime) for k in filelist))
	
	# ----------- generate log file -----
	mdw_report.log_gen(mdw.rel_build_files, mdw.skip_files)
	
	# ---------- report status-------
	
	print mdw_report.color('[status]', 'blue'), 'build:%d files. skip:%d files. log file:%s'%(len(mdw.rel_build_files), len(mdw.skip_files), mdw.log_fn)
