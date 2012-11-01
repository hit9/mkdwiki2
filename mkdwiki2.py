from mkdwiki2 import *

opt = {
	'init':mdw_core.init, 
	'build':mdw_core.build, 
	'clean':mdw_cache.clean
}

import sys

argv = sys.argv[1:]

if len(argv) == 1 and argv[0] in opt.keys():
	opt[argv[0]]()
else:
	mdw_report.help()
