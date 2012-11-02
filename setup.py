'''
setup for mkdwiki2.will install mkdwiki pakage for your python.and copy mkdiwki2.py to /usr/bin/mkdwiki2
'''
import os
from setuptools import setup

setup(
	name = 'mkdwiki2', 
	version = '0.2', 
	author = 'hit9', 
	author_email = 'nz2324@126.com', 
	description = ("Write wiki in Github Favorite Markdown."),
	license = 'BSD', 
	keywords = 'wiki markdown Github python', 
	packages=['mkdwiki2'],
	include_package_data = True, 
	entry_points = {
        'console_scripts': [
			'mkdwiki2 = mkdwiki2.mkdwiki2:main'
        ]
    }, 
	install_requires = ['markdown2 >= 2.1.0', 'pygments'],
	url = "https://github.com/hit9/mkdwiki2"
)
