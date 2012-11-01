'''
This is report module for mkdwiki2
'''
def help():
	print '''mkdwiki2 -- write wiki in Github Favorite Markdown.
usage:
  mkdwiki2 init 
  mkdwiki2 build
  mkdwiki2 clean'''

def color(msg, color):
	import os
	colordict = {'red':'\033[91m', 'green':'\033[92m', 'yellow':'\033[93m', 'blue':'\033[94m'}
	return colordict.get(color, '\033[0m')+msg+'\033[0m' if os.name == 'posix' else msg

def error(msg):
	print color('[error]', 'red'), msg
	exit()

def warning(ty, msg):
	print color('['+ty+']', 'yellow'), msg

def success(msg = ''):
	print color('[ok]', 'green'), msg

def log_gen(build_l, skip_d):
	import mdw
	text = '--------------- build files :'+str(len(build_l))+' -----------------\n  '
	text = text+reduce(lambda x, y:x+'\n  '+y, build_l) if  build_l else text+'no file build\n'
	text = text+('\n--------------- skip files :'+str(len(skip_d))+' -------------------\n  ')
	
	text  = text+'\n'
	
	from itertools import groupby
	for i, k in groupby(sorted(skip_d.items(), key = lambda x:x[1]), lambda x:x[1]):
		text = text+'-- skip reason : '+i+'\n    '
		text = text+reduce(lambda x, y:x+'\n    '+y, [x for x, y in k]) 
		text = text+'\n\n'
	open(mdw.log_fn, 'w').write(text)
