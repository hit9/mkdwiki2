'''
names for mkdwiki2
'''
import os, re

version = '0.2'

mdw_dir_path = os.path.dirname(__file__)

src_dirname = 'src'  # mkd files src directory name

tpl_fn = 'tpl.html' # template file name

tpl_path = os.path.join(src_dirname, tpl_fn) # template file path

mark_fn = '.mkdwiki2.markfile' # mark a directory as a mkdwiki2-work-directory

encoding = 'utf-8' # source file and tpl and output html encoding

skip_files = dict() # record sikp file {'file_path':'skip reason'}

rel_build_files = [] # record rel_build_files

title_re = re.compile(r'%title (.*)')

html_re = re.compile('(.*)\.[^\.]*$')

cache_fn = '.mkdwiki2.cache~' # mkdwiki2 cache file

log_fn = 'mkdwiki2.log' # log file

path_ignore_path = os.path.join(src_dirname, '.pathignore')

fn_ignore_path = os.path.join(src_dirname, '.fnignore')

user_ignore_rules_fn = list()

user_ignore_rules_path = list()

ignore_mdw_files = [tpl_path,path_ignore_path, fn_ignore_path]
