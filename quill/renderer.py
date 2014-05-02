# coding=utf8

from . import charset

from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateNotFound


class Renderer(object):

    def initialize(self, templates_path, global_data):
        pass
