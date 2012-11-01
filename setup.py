'''
setup for mkdwiki2.will install mkdwiki pakage for your python.and copy mkdiwki2.py to /usr/bin/mkdwiki2
'''
from setuptools import setup

setup(
	name = 'mkdwiki2', 
	version = '1.0', 
	author = 'hit9', 
	author_email = 'nz2324@126.com', 
	description = ("use Github Favorite Markdown to write wiki"),
	license = 'BSD', 
	keywords = 'wiki markdown Github python', 
	packages=['mkdwiki2'], 
	package_data = {
		'mkdwiki2':['tpl.html', 'static/style.css', 'static/code_style/*.css', 'static/code_style/noise.png']
	}, 
	entry_points = {
        'console_scripts': [
			'mkdwiki2 = mkdwiki2.mkdwiki2:main'
        ]
    }, 
	install_requires = ['markdown2', 'pygments >= 1.5'],
	url = "http://hit9.org/mkdwiki2"
)
