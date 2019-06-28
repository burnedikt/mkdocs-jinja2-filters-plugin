from setuptools import setup

setup(
    name='Mkdocs Jinja2 Filters',
    version='0.1.0',
    packages=['theme_jinja2_filters'],
    url='https://github.com/burnedikt/mkdocs-template-filters-plugin',
    license='MIT',
    author='Benedikt Reiser',
    author_email='dev@burnedikt.com',
    description='Allows to register custom jinja2 template filters with any mkdocs theme.',
    install_requires=['mkdocs'],

    # The following rows are important to register your plugin.
    # The format is "(plugin name) = (plugin folder):(class name)"
    # Without them, mkdocs will not be able to recognize it.
    entry_points={
        'mkdocs.plugins': [
            'theme-jinja2-filters = theme_jinja2_filters:ThemeJinja2FiltersPlugin',
        ]
    },
)