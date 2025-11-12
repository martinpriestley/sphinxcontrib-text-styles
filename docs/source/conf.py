import os
import sys

project = 'Sphinxcontrib Text Styles'
copyright = '2025, Martin Priestley'
author = 'Martin Priestley'

extensions = [
    'sphinxcontrib_text_styles',
]

# Extension-specific configuration

text_styles_styles = {
    'text-small-caps' : ("font-variant: small-caps;", r'\textsc{'),
}

text_styles_roles = {
    'important': ['text-red', 'text-italic', 'text-bold', 'text-underline', 'bg-black'],
    'success': ['text-green'],
    'error': ['text-red'],
    'legal-term' : ['text-small-caps', 'text-bold'],
}

# HTML and PDF theme
html_theme = 'sphinx_rtd_theme'
latex_engine = 'pdflatex'

latex_elements = {
  # Avoid blank page before each chapter
  'extraclassoptions': 'openany,oneside'
}

html_theme_options = {
    'navigation_depth': -1,
}
