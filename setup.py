'''
setup for mkdwiki2.will install mkdwiki pakage for your python.and copy mkdiwki2.py to /usr/bin/mkdwiki2
'''
import os
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
	include_package_data = True, 
	entry_points = {
        'console_scripts': [
			'mkdwiki2 = mkdwiki2.mkdwiki2:main'
        ]
    }, 
	install_requires = ['markdown2', 'pygments >= 1.5'],
	url = "https://github.com/hit9/mkdwiki2"
)
