# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sarhad NGFW'
copyright = '2026, Sarhad NGFW Team'
author = 'Sarhad NGFW Team'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_togglebutton',
    'sphinx_simplepdf',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Change this line in source/conf.py
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'collapse_navigation': True,  # Faqat faol bo'lim ochiq turadi, qolganlari yopiq
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}

# Hujjat versiyasini pastki qismda ko'rsatish uchun:
version = '2026.1'
release = 'v2026.1.0'

# source/conf.py fayliga qo'shing:

# Loyiha nomi yonida versiya raqamini ko'rsatishni majburlash
html_display_toc_header_version = True

# Pastki futer qismida mualliflik huquqi va versiyani ko'rsatish
html_show_sphinx = False  # "Powered by Sphinx" yozuvini o'chiradi (toza brending uchun)
