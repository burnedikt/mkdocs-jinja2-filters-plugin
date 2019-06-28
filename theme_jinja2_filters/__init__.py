# coding: utf-8

import sys

from mkdocs.plugins import BasePlugin

from .theme import ThemeProxy


class ThemeJinja2FiltersPlugin(BasePlugin):

    def on_config(self, config, **kwargs):
        # replace the Theme with our ThemeProxy which will dynamically add in
        # jinja2 filters in a module called 'template_filters.py' within the
        # docs directory
        config['theme'] = ThemeProxy(config['theme'])
        return config