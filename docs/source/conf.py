import os
import sys

project = 'Sphinxcontrib Text Styles'
copyright = '2025, Martin Priestley'
author = 'Martin Priestley'

extensions = [
    'sphinxcontrib_text_styles',
]

# Extension-specific configuration
text_formatting_roles = {
    'important': ['text-red', 'text-italic', 'text-bold', 'text-underline', 'bg-black'],
    'success': ['text-green'],
    'error': ['text-red'],
}

# HTML and PDF theme
html_theme = 'alabaster'
latex_engine = 'pdflatex'
