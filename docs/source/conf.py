# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sphinx_rtd_theme

import os
import sys

sys.path.append(os.path.abspath("./_ext"))

# -- Project information -----------------------------------------------------

project = 'Principles of GIS and Remote Sensing'
copyright = '2020, University of Twente'
author = 'The Course Team'

# The full version, including alpha/beta/rc tags
release = '4.0.0'
show_authors = True
html_show_sourcelink = False

# Name of the master document. 
master_doc = 'index'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
    "sphinx_copybutton",
    "helloworld",
    "todo"
]


todo_include_todos = True

# Figure numbering
numfig = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.

exclude_patterns = ['assets/ltb-links-gis.rst', 
'assets/data-links-gis.rst',
'assets/data-links-di.rst', 
'assets/ltb-links-eo.rst', 
'assets/data-links-eo.rst',
'assets/ltb-links-di.rst',  
'style-demo.rst', 
'style-guide.rst', ]

# Allows storing external links in separated rst
rst_epilog=""

# Target link-files
link_files = ['assets/ltb-links-gis.rst',
            'assets/data-links-gis.rst',
            'assets/data-links-eo.rst',
            'assets/ltb-links-eo.rst',
            'assets/ltb-links-di.rst',
            'assets/data-links-di.rst',
            'substitutions.txt'
            ]

# Read links in the from the target files
for file in link_files:
    with open(file) as f:
        rst_epilog += f.read()



# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Costume css. Paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]

# Latex Costume configurations
# Configure paper size, font size, preamble options, etc.
latex_elements = {
    'figure_align': 'H',
    'preamble': '''
        \\usepackage{float}
        ''',
}

