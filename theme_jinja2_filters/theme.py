# coding: utf-8

import sys
import importlib.util
from os import path

from mkdocs.theme import Theme as BaseTheme


def import_python_module_from_path(module_name, path):
    spec = importlib.util.spec_from_file_location(module_name, path)
    imported_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(imported_module)
    return imported_module


class ThemeProxy(BaseTheme):
    """
    An implementation of a mkdocs Theme that extends the jinja2 environment with
    additionally specified jinjfa2 filters
    """

    def __init__(self, original_theme):
        self.original_theme = original_theme

    def __getattr__(self, attr):
        return getattr(self.original_theme, attr)

    def get_env(self):
        """ Return a Jinja environment for the theme. """
        env = self.original_theme.get_env()

        filter_module_name = 'template_filters'
        theme_package_name = path.basename(self.dirs[0])

        custom_jinja2_filters = import_python_module_from_path('%s.%s' % (theme_package_name, filter_module_name), path.join(self.dirs[0], '%s.py' % filter_module_name))

        for filter_name in [f for f in dir(custom_jinja2_filters) if not f.startswith('__')]:
            env.filters[filter_name] = getattr(custom_jinja2_filters, filter_name)

        return env
