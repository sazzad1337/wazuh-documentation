# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# Note that not all possible configuration values are present in this
# autogenerated file. For a full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

import sys
import os
import glob
import re
import shlex
import datetime
import time
import json
import atexit
try:
    from jsmin import jsmin
except ImportError:
    atexit.register(print,"\nThe module jsmin is not available. Please, make sure you install all the required modules listed in requirements.txt.")
    sys.exit()
from requests.utils import requote_uri

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))
sys.path.append(os.path.abspath("_exts"))

# -- Project information -----------------------------------------------------

project = u'Wazuh'
author = u'Wazuh, Inc.'
copyright = u'&copy; ' + str(datetime.datetime.now().year) + u' &middot; Wazuh Inc.'

# The short X.Y version
version = '4.5'
is_latest_release = True

# The full version, including alpha/beta/rc tags
# Important: use a valid branch (4.0) or, preferably, tag name (v4.0.0)
release = '4.5.0'
api_tag = '4.5.0'
apiURL = 'https://raw.githubusercontent.com/wazuh/wazuh/'+api_tag+'/api/api/spec/spec.yaml'

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.8'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks', # Sphinx built-in extension
    'sphinx_tabs.tabs',
    'wazuh-doc-images', # Custom extension
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

extlinks = {'api-ref': ('https://DOMAIN/user-manual/api/reference.html#%s',
                        ''),
            'cloud-api-ref': ('https://DOMAIN/cloud-service/apis/reference.html#%s',
                              '')
            }

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en-US'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['redirects.js']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'wazuh_doc_theme_v3'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'wazuh_web_url': 'https://wazuh.com',
    'wazuh_doc_url': 'https://documentation.wazuh.com',
    'collapse_navigation': False, # Only for Wazuh documentation theme v2.0
    'include_edit_repo': True,
    'include_version_selector': True,
    'breadcrumb_root_title': 'Documentation',
}

if html_theme == 'wazuh_doc_theme_v3':
    # Check if the release was before the new the theme
    # Note v3_release represents the release that was 'current' when the theme
    # wazuh_doc_theme_v3 was published, that is, 4.3
    v3_release = [4,3]
    current_release = list(map(int, version.split('.')))
    is_pre_v3 = current_release[0] < v3_release[0] or (
                current_release[0] == v3_release[0] and
                current_release[1] < v3_release[1])
    html_theme_options['is_pre_v3'] = is_pre_v3
    
    # Allow dark mode is set to false by default
    html_theme_options['include_mode'] = True
    # Allow switching between modes is set to false by default
    # html_theme_options['include_mode_switch'] = True

    # Check if the URL for the redirects.min.js must be local or from current
    # redirects.min.js should be loaded from the local folder if:
    # * the release is "current" (is_latest_release = True) or
    # * is a normal compilation (not for production)
    html_theme_options['local_redirects_file'] = is_latest_release or not (tags.has("production") or tags.has("dev"))

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['_themes']

# Custom variable to store the path to the selected theme assets
theme_assets_path = html_theme_path[0] + '/' + html_theme

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = project + ' documentation'

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = theme_assets_path + '/static/images/wazuh-logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = theme_assets_path + '/static/images/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True
smartquotes = False

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {}

html_additional_pages['not_found'] = 'not-found.html'

if is_latest_release == True and html_theme_options['breadcrumb_root_title'] == 'Documentation':
    html_additional_pages['moved-content'] = 'moved-content.html'

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# If empty string, we eliminate permalinks from documentation.
html_add_permalinks = ' '

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'WazuhDocs'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  (master_doc, 'WazuhDocs.tex', u'Documentation',
   u'Wazuh, Inc.', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'wazuhdocs', u'Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  (master_doc, 'WazuhDocs', u'Documentation',
   author, 'Wazuh', 'Documentation',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be an ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html', 'not_found.html']


# -- Extension configuration -------------------------------------------------

# -- Images extension -----------------------------------------------------

wazuh_images_config = {
  'override_image_directive': 'thumbnail',
  'show_caption': True
}

html_scaled_image_link = False

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
# intersphinx_mapping = {'https://docs.python.org/': None}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Minify ------------------------------------------------------------------

extra_assets = [
    'style-redirect.css',
    'moved-content.js'
]

def minification(current_path):

    files = [
        ['style','css'],
        ['wazuh-icons','css'],
        ['custom-redoc','css'],
        ['accordions','css'],
        ['version-selector','js'],
        ['redirects','js'],
        ['style','js'],
        ['custom-redoc','js'],
        ['accordion', 'js']
    ]

    if is_latest_release == True:
        for asset in extra_assets:
            files.append(asset.split('.'))

    for file in files:

        min_file = os.path.join(current_path, 'static', file[1], 'dist', file[0]+'.min.'+file[1])
        minify = True
        min_file_content = ''

        if os.path.isfile(min_file):
            with open(min_file, 'r') as f_min:
                min_file_content = f_min.read()

        if file[0]+'.'+file[1] in exclude_patterns:
            source_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), html_static_path[0], file[1], file[0]+'.'+file[1])
        else:
            source_file = os.path.join(current_path, file[1]+'-src', file[0]+'.'+file[1])

        with open(source_file, 'r') as f:

            output = f.read()

            # remove comments - this will break a lot of hacks :-P
            output = re.sub( r'\s*/\*\s*\*/', "$$HACK1$$", output ) # preserve IE<6 comment hack
            output = re.sub( r'/\*[\s\S]*?\*/', "", output )
            output = output.replace( "$$HACK1$$", '/**/' ) # preserve IE<6 comment hack

            # url() doesn't need quotes
            output = re.sub( r'url\((["\'])([^)]*)\1\)', r'url(\2)', output )

            # spaces may be safely collapsed as generated content will collapse them anyway
            output = re.sub( r'\s+', ' ', output )

            # shorten collapsable colors: #aabbcc to #abc
            output = re.sub( r'#([0-9a-f])\1([0-9a-f])\2([0-9a-f])\3(\s|;)', r'#\1\2\3\4', output )

            # fragment values can loose zeros
            output = re.sub( r':\s*0(\.\d+([cm]m|e[mx]|in|p[ctx]))\s*;', r':\1;', output )

        if output == min_file_content:
            minify = False

        if minify:
            with open(min_file, 'w') as f2:
                f2.write(output)

# -- Versions -------------------------------------------------------------------

def customReplacements(app, docname, source):
    result = source[0]
    for key in app.config.custom_replacements:
        result = result.replace(key, app.config.custom_replacements[key])
    source[0] = result

custom_replacements = {
    # === URLs and base URLs
    "|CHECKSUMS_URL|" : "https://packages.wazuh.com/4.x/checksums/wazuh/",
    "|APK_CHECKSUMS_I386_URL|" : "alpine/x86",
    "|APK_CHECKSUMS_X86_64_URL|" : "alpine/x86_64",
    "|APK_CHECKSUMS_AARCH64_URL|" : "alpine/aarch64",
    "|APK_CHECKSUMS_ARMV7_URL|" : "alpine/armv7",
    "|APK_CHECKSUMS_ARMHF_URL|" : "alpine/armhf",
    "|APK_CHECKSUMS_PPC_URL|" : "alpine/ppc64le",
    "|APK_AGENT_I386_URL|" : "https://packages.wazuh.com/4.x/alpine/v3.12/main/x86/wazuh-agent",
    "|APK_AGENT_X86_64_URL|" : "https://packages.wazuh.com/4.x/alpine/v3.12/main/x86_64/wazuh-agent",
    "|APK_AGENT_AARCH64_URL|" : "https://packages.wazuh.com/4.x/alpine/v3.12/main/aarch64/wazuh-agent",
    "|APK_AGENT_ARMV7_URL|" : "https://packages.wazuh.com/4.x/alpine/v3.12/main/armv7/wazuh-agent",
    "|APK_AGENT_ARMHF_URL|" : "https://packages.wazuh.com/4.x/alpine/v3.12/main/armhf/wazuh-agent",
    "|APK_AGENT_PPC_URL|" : "https://packages.wazuh.com/4.x/alpine/v3.12/main/ppc64le/wazuh-agent",
    "|RPM_AGENT_URL|" : "https://packages.wazuh.com/4.x/yum/wazuh-agent",
    "|RPM_MANAGER_URL|" : "https://packages.wazuh.com/4.x/yum/wazuh-manager",
    "|DEB_AGENT_URL|" : "https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent",
    "|DEB_MANAGER_URL|" : "https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-manager/wazuh-manager",
    #
    # === Global and Wazuh version (wazuh agent, manager, indexer, and dashboard)
    "|WAZUH_CURRENT_MAJOR|" : "4.x",
    "|WAZUH_CURRENT_MINOR|" : version,
    "|WAZUH_CURRENT|" : release,
    # --- Revision numbers for Wazuh agent and manager packages versions
    # Alpine APK packages revisions
    "|WAZUH_REVISION_APK_AGENT_I386|" : "r1",
    "|WAZUH_REVISION_APK_AGENT_X86_64|" : "r1",
    "|WAZUH_REVISION_APK_AGENT_AARCH64|" : "r1",
    "|WAZUH_REVISION_APK_AGENT_ARMV7|" : "r1",
    "|WAZUH_REVISION_APK_AGENT_ARMHF|" : "r1",
    "|WAZUH_REVISION_APK_AGENT_PPC|" : "r1",
    # Yum packages revisions
    "|WAZUH_REVISION_YUM_AGENT_I386|" : "1",
    "|WAZUH_REVISION_YUM_MANAGER_I386|" : "1",
    "|WAZUH_REVISION_YUM_AGENT_I386_EL5|" : "1",
    #"|WAZUH_REVISION_YUM_MANAGER_I386_EL5|" :
    "|WAZUH_REVISION_YUM_AGENT_X86|" : "1",
    "|WAZUH_REVISION_YUM_MANAGER_X86|" : "1",
    "|WAZUH_REVISION_YUM_AGENT_X86_EL5|" : "1",
    #|WAZUH_REVISION_YUM_MANAGER_X86_EL5|
    "|WAZUH_REVISION_YUM_AGENT_AARCH64|" : "1",
    "|WAZUH_REVISION_YUM_MANAGER_AARCH64|" : "1",
    "|WAZUH_REVISION_YUM_AGENT_ARMHF|" : "1",
    #"|WAZUH_REVISION_YUM_MANAGER_ARMHF|" : "1",
    "|WAZUH_REVISION_YUM_AGENT_PPC|" : "1",
    #|WAZUH_REVISION_YUM_MANAGER_PPC|" :
    # Deb packages revisions
    "|WAZUH_REVISION_DEB_AGENT_I386|" : "1",
    "|WAZUH_REVISION_DEB_MANAGER_I386|" : "1",
    "|WAZUH_REVISION_DEB_AGENT_X86|" : "1",
    "|WAZUH_REVISION_DEB_MANAGER_X86|" : "1",
    "|WAZUH_REVISION_DEB_AGENT_AARCH64|" : "1",
    "|WAZUH_REVISION_DEB_MANAGER_AARCH64|" : "1",
    "|WAZUH_REVISION_DEB_AGENT_ARMHF|" : "1",
    "|WAZUH_REVISION_DEB_MANAGER_ARMHF|" : "1",
    "|WAZUH_REVISION_DEB_AGENT_PPC|" : "1",
    #"|WAZUH_REVISION_DEB_MANAGER_PPC|" : 
    #
    # === Wazuh indexer version revisions
    "|WAZUH_INDEXER_CURRENT_REV|" : "1", # RPM and Deb
    #"|WAZUH_INDEXER_CURRENT_REV_DEB|" :
    # --- Architectures for Wazuh indexer packages
    "|WAZUH_INDEXER_x64_RPM|" : "x86_64",
    "|WAZUH_INDEXER_x64_DEB|" : "amd64",
    #
    # === Wazuh dashboard version revisions
    "|WAZUH_DASHBOARD_CURRENT_REV_RPM|" : "1",
    "|WAZUH_DASHBOARD_CURRENT_REV_DEB|" : "1",
    # --- Architectures for Wazuh dashboard packages
    "|WAZUH_DASHBOARD_x64_RPM|" : "x86_64",
    "|WAZUH_DASHBOARD_x64_DEB|" : "amd64",
    #
    # === Versions and revisions for other Wazuh deployments
    #"|WAZUH_CURRENT_MAJOR_AMI|" :
    #"|WAZUH_CURRENT_MINOR_AMI|" :
    "|WAZUH_CURRENT_AMI|" : release,
    "|WAZUH_CURRENT_MAJOR_OVA|" : "4.x",
    #"|WAZUH_CURRENT_MINOR_OVA|" :
    "|WAZUH_CURRENT_OVA|" : release,
    #"|WAZUH_CURRENT_MAJOR_DOCKER|" :
    "|WAZUH_CURRENT_MINOR_DOCKER|" : version,
    "|WAZUH_CURRENT_DOCKER|" : release,
    #"|WAZUH_CURRENT_MAJOR_KUBERNETES|" :
    #"|WAZUH_CURRENT_MINOR_KUBERNETES|" :
    "|WAZUH_CURRENT_KUBERNETES|" : release,
    #"|WAZUH_CURRENT_MAJOR_ANSIBLE|" :
    "|WAZUH_CURRENT_MINOR_ANSIBLE|" : version,
    "|WAZUH_CURRENT_ANSIBLE|" : release,
    #"|WAZUH_CURRENT_MAJOR_PUPPET|" :
    #"|WAZUH_CURRENT_MINOR_PUPPET|" :
    "|WAZUH_CURRENT_PUPPET|" : release,
    #"|WAZUH_CURRENT_MAJOR_FROM_SOURCES|" :
    "|WAZUH_CURRENT_MINOR_FROM_SOURCES|" : version,
    "|WAZUH_CURRENT_FROM_SOURCES|" : release,
    #"|WAZUH_CURRENT_MAJOR_WIN_FROM_SOURCES|" :
    #"|WAZUH_CURRENT_MINOR_WIN_FROM_SOURCES|" :
    "|WAZUH_CURRENT_WIN_FROM_SOURCES|" : release,
    "|WAZUH_CURRENT_WIN_FROM_SOURCES_REV|" : "1",
    #
    # === Versions and revisions for packages of specific operating systems
    "|WAZUH_CURRENT_MAJOR_WINDOWS|" : "4.x",
    #"|WAZUH_CURRENT_MINOR_WINDOWS|" :
    "|WAZUH_CURRENT_WINDOWS|" : release,
    "|WAZUH_REVISION_WINDOWS|" : "1",
    "|WAZUH_CURRENT_MAJOR_OSX|" : "4.x",
    #"|WAZUH_CURRENT_MINOR_OSX|" :
    "|WAZUH_CURRENT_OSX|" : release,
    "|WAZUH_REVISION_OSX|" : "1",
    "|WAZUH_CURRENT_MAJOR_SOLARIS|" : "4.x",
    #"|WAZUH_CURRENT_MINOR_SOLARIS|" :
    "|WAZUH_CURRENT_SOLARIS|" : release, # Set here the lesser of WAZUH_CURRENT_MAJOR_SOLARIS10 and 11 values
    #"|WAZUH_REVISION_SOLARIS|" : "1",
    "|WAZUH_CURRENT_MAJOR_SOLARIS10|" : "4.x",
    #"|WAZUH_CURRENT_MINOR_SOLARIS10|" :
    "|WAZUH_CURRENT_SOLARIS10|" : release,
    #"|WAZUH_REVISION_SOLARIS10|" : "1",
    "|WAZUH_CURRENT_MAJOR_SOLARIS11|" : "4.x",
    #"|WAZUH_CURRENT_MINOR_SOLARIS11|" :
    "|WAZUH_CURRENT_SOLARIS11|" : release,
    #"|WAZUH_REVISION_SOLARIS11|" : "1",
    "|WAZUH_CURRENT_MAJOR_SOLARIS10_i386|" : "4.x",
    #"|WAZUH_CURRENT_MINOR_SOLARIS10_i386|" :
    "|WAZUH_CURRENT_SOLARIS10_i386|" : release,
    #"|WAZUH_REVISION_SOLARIS10_i386|" : "1",
    "|WAZUH_CURRENT_MAJOR_SOLARIS10_SPARC|" : "4.x",
    #"|WAZUH_CURRENT_MINOR_SOLARIS10_SPARC|" :
    "|WAZUH_CURRENT_SOLARIS10_SPARC|" : release,
    #"|WAZUH_REVISION_SOLARIS10_SPARC|" : "1",
    "|WAZUH_CURRENT_MAJOR_SOLARIS11_i386|" : "4.x",
    #"|WAZUH_CURRENT_MINOR_SOLARIS11_i386|" :
    "|WAZUH_CURRENT_SOLARIS11_i386|" : release,
    #"|WAZUH_REVISION_SOLARIS11_i386|" : "1",
    "|WAZUH_CURRENT_MAJOR_SOLARIS11_SPARC|" : "4.x",
    #"|WAZUH_CURRENT_MINOR_SOLARIS11_SPARC|" :
    "|WAZUH_CURRENT_SOLARIS11_SPARC|" : release,
    #"|WAZUH_REVISION_SOLARIS11_SPARC|" : "1",
    "|WAZUH_CURRENT_MAJOR_AIX|" : "4.x",
    #"|WAZUH_CURRENT_MINOR_AIX|" :
    "|WAZUH_CURRENT_AIX|" : release,
    "|WAZUH_REVISION_AIX|" : "1",
    "|WAZUH_CURRENT_MAJOR_HPUX|" : "4.x",
    #"|WAZUH_CURRENT_MINOR_HPUX|" :
    "|WAZUH_CURRENT_HPUX|" : release,
    "|WAZUH_REVISION_HPUX|" : "1",
    #
    # === Elastic
    # --- Filebeat
    "|FILEBEAT_LATEST|" : "7.10.2",
    "|FILEBEAT_LATEST_AMI|" : "7.10.2",
    "|FILEBEAT_LATEST_OVA|" : "7.10.2",
    # --- Open Distro for Elasticsearch
    "|OPEN_DISTRO_LATEST|" : "1.13.2",
    # --- Elasticsearch
    "|ELASTICSEARCH_ELK_LATEST|" : "7.17.9", # Basic license
    "|ELASTICSEARCH_LATEST|" : "7.10.2",
    # --- Other Elastic
    "|ELASTIC_6_LATEST|" : "6.8.8",
    #
    # === Splunk
    "|SPLUNK_LATEST|" : "8.2.8",
    "|WAZUH_SPLUNK_CURRENT|" : release,
    #
    "|SPLUNK_LATEST_MINOR|" : "8.2",
    "|WAZUH_SPLUNK_REV_CURRENT_LATEST|" : "1", # 8.2
    "|WAZUH_SPLUNK_REV_CURRENT_8.1|" : "1",
}

# -- Customizations ---------------------------------------------------------

## emptyTocNodes ##
emptyTocNodes = json.dumps([
    'amazon/configuration/index',
    'containers',
    'deployment',
    'docker-monitor/index',
    'installation-guide/elasticsearch-cluster/index',
    'installation-guide/wazuh-cluster/index',
    'installation-guide/upgrading/legacy/index',
    'installation-guide/packages-list/linux/linux-index',
    'installation-guide/packages-list/solaris/solaris-index',
    'user-manual/agents/index',
    'user-manual/agents/remove-agents/index',
    'user-manual/agents/listing/index',
    'user-manual/kibana-app/reference/index',
    'user-manual/ruleset/ruleset-xml-syntax/index',
    'installation-guide/distributed-deployment/step-by-step-installation/elasticsearch-cluster/index',
    'installation-guide/distributed-deployment/step-by-step-installation/wazuh-cluster/index',
    'user-manual/capabilities/active-response/ar-use-cases/index',
])

# -- Setup -------------------------------------------------------------------

compilation_time = str(time.time())

def setup(app):

    current_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), theme_assets_path)
    static_path_str = os.path.join(os.path.dirname(os.path.realpath(__file__)), html_static_path[0])

    if not os.path.exists(app.srcdir + '/' + html_static_path[0] + '/'):
        os.mkdir(app.srcdir + '/' + html_static_path[0] + '/')

    if html_theme == 'wazuh_doc_theme_v3':
        
        # Minify redirects.js
        if html_theme_options['include_version_selector'] == True:
            with open(os.path.join(static_path_str, "js/redirects.js")) as redirects_file:
                minified = jsmin(redirects_file.read())
                
                # Create redirects.min.js file
                with open(os.path.join(current_path, "static/js/min/redirects.min.js"), 'w') as redirects_min_file:
                    redirects_min_file.write(minified)
        
        # CSS files
        app.add_css_file("css/min/bootstrap.min.css?ver=%s" % os.stat(
            os.path.join(current_path, "static/css/min/bootstrap.min.css")).st_mtime)

        # JS files
        app.add_js_file("js/jquery.js?ver=%s" % os.stat(
            os.path.join(current_path, "static/js/jquery.js")).st_mtime)
        app.add_js_file("js/min/bootstrap.bundle.min.js?ver=%s" % os.stat(
            os.path.join(current_path, "static/js/min/bootstrap.bundle.min.js")).st_mtime)
        app.add_js_file("js/underscore.js?ver=%s" % os.stat(
            os.path.join(current_path, "static/js/underscore.js")).st_mtime)

    if html_theme == 'wazuh_doc_theme':
        minification(current_path)

        # CSS files
        app.add_css_file("css/fontawesome.min.css?ver=%s" % os.stat(
            os.path.join(current_path, "static/css/fontawesome.min.css")).st_mtime)
        app.add_css_file("css/dist/wazuh-icons.min.css?ver=%s" % os.stat(
            os.path.join(current_path, "css-src/wazuh-icons.css")).st_mtime)
        app.add_css_file("css/dist/style.min.css?ver=%s" % os.stat(
            os.path.join(current_path, "css-src/style.css")).st_mtime)
        app.add_css_file("css/dist/accordions.min.css?ver=%s" % os.stat(
            os.path.join(current_path, "css-src/accordions.css")).st_mtime)

        # JS files
        app.add_js_file("js/dist/version-selector.min.js?ver=%s" % os.stat(
            os.path.join(current_path, "js-src/version-selector.js")).st_mtime)
        app.add_js_file("js/dist/style.min.js?ver=%s" % os.stat(
            os.path.join(current_path, "js-src/style.js")).st_mtime)
        app.add_js_file("js/dist/accordion.min.js?ver=%s" % os.stat(
            os.path.join(current_path, "js-src/accordion.js")).st_mtime)
        app.add_js_file("js/dist/redirects.min.js?ver=%s" % os.stat(
            os.path.join(static_path_str, "js/redirects.js")).st_mtime)

    app.add_config_value('custom_replacements', {}, True)
    app.connect('source-read', customReplacements)

	# List of compiled documents
    app.connect('html-page-context', collect_compiled_pagename)
    app.connect('html-page-context', insert_inline_style)
    if html_theme == 'wazuh_doc_theme_v3':
        app.connect('html-page-context', insert_inline_js)
        app.connect('html-page-context', manage_assets)
    app.connect('build-finished', finish_and_clean)


def insert_inline_style(app, pagename, templatename, context, doctree):
    ''' Runs once per page, inserting the content of the compiled style for Google Fonts into the context '''
    google_fonts_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), theme_assets_path, 'static', 'css', 'google-fonts.min.css')
    # Fonts to be preloaded
    with open(google_fonts_path, 'r') as reader:
        google_fonts = reader.read()
        context['inline_fonts'] = google_fonts

def insert_inline_js(app, pagename, templatename, context, doctree):
    ''' Runs once per page, inserting the content of minified javascript snippets into the context '''
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), theme_assets_path, 'static', 'js', 'inline')
    js_scripts = ['light-dark-mode-inline']
    inline_scripts = []
    
    for script in js_scripts:
        script_path = os.path.join(path, script + '.min.js')
    
        # Inline scripts
        with open(script_path, 'r') as reader:
            inline_scripts.append(reader.read())
    context['inline_scripts'] = inline_scripts

def manage_assets(app, pagename, templatename, context, doctree):
    theme_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), theme_assets_path)
    static = '_static/'
    if html_theme_options['include_version_selector'] == True:
        conditional_redirects = static + "js/min/redirects.min.js?ver=%s" % os.stat(os.path.join(theme_dir, "static/js/min/redirects.min.js")).st_mtime
        if tags.has("production") or tags.has("dev"):
            conditional_redirects = static + "js/min/redirects.min.js?ver=%s" % str(time.time())
    else:
        conditional_redirects = ''
    # Full list of non-common javascript files
    individual_js_files = {
        "redirects": conditional_redirects,
        "wazuh-documentation": static + "js/min/wazuh-documentation.min.js?ver=%s" % os.stat(os.path.join(theme_dir, "static/js/min/wazuh-documentation.min.js")).st_mtime,
        "index": static + "js/min/index.min.js?ver=%s" % os.stat(os.path.join(theme_dir, "static/js/min/index.min.js")).st_mtime,
        "index-redirect": static + "js/min/index-redirect.min.js?ver=%s" % os.stat(os.path.join(theme_dir, "static/js/min/index-redirect.min.js")).st_mtime,
        "search-results": static + "js/min/search-results.min.js?ver=%s" % os.stat(os.path.join(theme_dir, "static/js/min/search-results.min.js")).st_mtime,
        # "searchIndex": "searchindex.js",
        "not-found": static + "js/min/not-found.min.js?ver=%s" % os.stat(os.path.join(theme_dir, "static/js/min/not-found.min.js")).st_mtime,
        "api-reference": static + "js/min/api-reference.min.js?ver=%s" % os.stat(os.path.join(theme_dir, "static/js/min/api-reference.min.js")).st_mtime,
        "redoc-standalone": static + "js/redoc.standalone.js?ver=%s" % os.stat(os.path.join(theme_dir, "static/js/redoc.standalone.js")).st_mtime,
        "moved-content": static + "js/min/moved-content.min.js?ver=%s" % os.stat(os.path.join(theme_dir, "static/js/min/moved-content.min.js")).st_mtime
    }

    # The template function
    def get_css_by_page(pagename):
        css_map = {
            'index': "css/min/index.min.css?ver=%s" % os.stat(os.path.join(theme_dir, "static/css/min/index.min.css")).st_mtime,
            'user-manual/api/reference': "css/min/api-reference.min.css?ver=%s" % os.stat(os.path.join(theme_dir, "static/css/min/api-reference.min.css")).st_mtime,
            'cloud-service/apis/reference': "css/min/api-reference.min.css?ver=%s" % os.stat(os.path.join(theme_dir, "static/css/min/api-reference.min.css")).st_mtime,
            'search': "css/min/search-results.min.css?ver=%s" % os.stat(os.path.join(theme_dir, "static/css/min/search-results.min.css")).st_mtime,
            'moved-content': "css/min/moved-content.min.css?ver=%s" % os.stat(os.path.join(theme_dir, "static/css/min/moved-content.min.css")).st_mtime,
            'not_found': "css/min/not-found.min.css?ver=%s" % os.stat(os.path.join(theme_dir, "static/css/min/not-found.min.css")).st_mtime
        }
        default = "css/min/wazuh-documentation.min.css?ver=%s" % os.stat(os.path.join(theme_dir, "static/css/min/wazuh-documentation.min.css")).st_mtime
        
        if version < '4.0':
            css_map['user-manual/api/reference'] = default
        
        if html_theme_options['breadcrumb_root_title'] == 'Training':
            css_map['index'] = default

        if pagename in css_map.keys():
            return css_map[pagename]
        else:
            return default

    # The template function
    def get_js_by_page(pagename):
        js_map = {
            'index': [
                individual_js_files['index']
            ],
            'index-redirect': [
                individual_js_files['index-redirect']
            ],
            'search': [
                individual_js_files['redirects'],
                individual_js_files['search-results'],
                # individual_js_files['searchIndex']
            ],
            'not_found': [
                individual_js_files['redirects'],
                individual_js_files['not-found']
            ],
            'user-manual/api/reference': [
                individual_js_files['redoc-standalone'],
                individual_js_files['redirects'],
                individual_js_files['api-reference']
            ],
            'cloud-service/apis/reference': [
                individual_js_files['redoc-standalone'],
                individual_js_files['redirects'],
                individual_js_files['api-reference']
            ],
            'moved-content': [
                individual_js_files['redirects'],
                individual_js_files['moved-content']
            ]
        }
        default = [
            individual_js_files['redirects'],
            individual_js_files['wazuh-documentation']
            # tabs (extension)
            # lightbox (extension)
        ]
        
        if html_theme_options['breadcrumb_root_title'] == 'Training':
            js_map['index'] = default

        if pagename in js_map.keys():
            return js_map[pagename]
        else:
            return default

    # Add it to the page's context
    context['get_css_by_page'] = get_css_by_page
    context['get_js_by_page'] = get_js_by_page

exclude_doc = ["not_found"]
list_compiled_html = []

def finish_and_clean(app, exception):
    ''' Performs the final tasks after the compilation '''
    # Create additional files such as the `.doclist` and the sitemap
    creating_file_list(app, exception)

    if html_theme == 'wazuh_doc_theme':
        # Remove extra minified files
        for asset in extra_assets:
            mini_asset = '.min.'.join(asset.split('.'))
            if os.path.exists(app.srcdir + '/_static/' + mini_asset):
                os.remove(app.srcdir + '/_static/' + mini_asset)

    if html_theme == 'wazuh_doc_theme_v3':
        # Remove map files and sourcMapping line in production
        if production or html_theme_options['breadcrumb_root_title'] == 'Training':
            mapFiles = glob.glob(app.outdir + '/_static/*/min/*.map')
            assetsFiles = glob.glob(app.outdir + '/_static/js/min/*.min.js') + glob.glob(app.outdir + '/_static/css/min/*.min.css')
            # Remove map files
            for mapFilePath in mapFiles:
                try:
                    os.remove(mapFilePath)
                except:
                    print("Error while deleting file : ", mapFilePath)
            
            # Remove the source mapping URLs
            for assetsFilePath in assetsFiles:
                try:
                    with open(assetsFilePath, "r") as f:
                        lines = f.readlines()
                    with open(assetsFilePath, "w") as f:
                        for line in lines:
                            line = re.sub("//# sourceMappingURL=.*\.map", "", line)
                            line = re.sub("/\*# sourceMappingURL=.*\.map \*/", "", line)
                            f.write(line)
                except:
                    print("Error while removing source mapping from file: ", assetsFilePath)
                    
def collect_compiled_pagename(app, pagename, templatename, context, doctree):
    ''' Runs once per page, storing the pagename (full page path) extracted from the context
        It stores the path of all compiled documents except the orphans and the ones in exclude_doc '''
    if templatename == "page.html" and pagename not in exclude_doc:
        if not context['meta'] or ( context['meta']['orphan'] ):
            list_compiled_html.append(context['pagename']+'.html')
    else:
        pass

def creating_file_list(app, exception):
    ''' Creates the files containing the path to every html file that was compiled. These files are the `.doclist` and the release sitemap. '''
    if app.builder.name == 'html':
        build_path = app.outdir
        separator = '\n'
        sitemap_version = version
        if is_latest_release == True:
            sitemap_version = 'current'

        # Create the release sitemap content
        sitemap = '<?xml version=\'1.0\' encoding=\'utf-8\'?>'+separator
        sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+separator

        for compiled_html in list_compiled_html:
            sitemap += '\t<url><loc>' + requote_uri(html_theme_options.get('wazuh_doc_url') + '/' + sitemap_version + '/' + compiled_html) + '</loc></url>' + separator
        # Close sitemap content
        sitemap += '</urlset>'

        # Create .doclist file
        with open(build_path+'/.doclist', 'w') as doclist_file:
            list_text = separator.join(list_compiled_html)
            doclist_file.write(list_text)

        # Create release sitemap file
        with open(build_path+'/'+sitemap_version+'-sitemap.xml', 'w') as sitemap_file:
            sitemap_file.write(sitemap)

# -- Additional configuration ------------------------------------------------

if (tags.has("production")):
    production = True
else:
    production = False

html_context = {
    "display_github": True,
    "github_user": "wazuh",
    "github_repo": "wazuh-documentation",
    "conf_py_path": "/source/",
    "github_version": version,
    "production": production,
    "apiURL": apiURL,
    "compilation_ts": compilation_time,
    "empty_toc_nodes": emptyTocNodes,
    "is_latest_release": is_latest_release
}
sphinx_tabs_nowarn = True
