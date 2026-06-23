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

# # Sarhad NGFW logosi (yon panel yuqorisida ko'rsatiladi)
# html_logo = '_static/sarhad_logo.jpg'

# # Maxsus CSS (logo o'lchamini boshqarish uchun)
# html_css_files = ['custom.css']

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


# -- PDF (sphinx-simplepdf) sozlamalari --------------------------------------
# PDF fayl nomi (build/simplepdf/<name>.pdf)
simplepdf_file_name = 'SarhadNGFW.pdf'

# Rang palitrasi — izchil yashil brending.
# DIQQAT: 'primary-light' 'primary'dan OCHROQ, 'primary-dark' esa TO'QROQ
# bo'lishi kerak. Avvalgi sozlamada bu teskari va rang nomuvofiq edi.
simplepdf_vars = {
    'primary': '#1e4537',          # Asosiy yashil — sarlavhalar, chiziqlar, linklar
    'primary-light': '#2e6b54',    # Ochroq yashil — fon urg'ulari, hover holatlari
    'primary-dark': '#12231d',     # To'q yashil — kuchli urg'u
    'secondary': '#2e6b54',        # Ikkilamchi yashil ohang
    'cover-bg': '#0B1A08',         # Muqova (1-sahifa) orqa foni — to'q yashil
    'cover': '#ffffff',            # Muqovadagi sarlavha/yozuvlar rangi — oq
    'white': '#ffffff',            # Muqova futeri matni — oq
    'links': '#1e4537',            # Havola (link) rangi
    'top-left-content': 'counter(page)',                 # Yuqori chap: sahifa raqami
    'top-right-content': "'Sarhad NGFW'",                # Yuqori o'ng: mahsulot nomi
    'bottom-center-content': "'Sarhad NGFW — Foydalanuvchi qo''llanmasi'",
}