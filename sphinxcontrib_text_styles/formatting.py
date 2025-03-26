import sphinx
import os
from docutils import nodes
from sphinx.util.docutils import SphinxRole
from sphinx.writers.latex import LaTeXTranslator
from typing import Dict, Any, List

class FormattingRole(SphinxRole):
    """
    Customizable text formatting role with support for aliases
    """
    def __init__(self, style_classes: List[str]):
        super().__init__()
        self.style_classes = style_classes

    def __call__(self, name: str, rawtext: str, text: str, lineno: int, 
                 inliner, options: Dict[str, Any] = None, content: List[str] = None):
        options = options or {}
        node = nodes.inline(rawtext, text, classes=self.style_classes)
        return [node], []

def create_role_mapping(app, config):
    """
    Create role mappings based on configuration
    """
    # Default roles
    default_roles = {
        'red'       : ['text-red'],
        'blue'      : ['text-blue'],
        'green'     : ['text-green'],
        'yellow'    : ['text-yellow'],

        'bg-red'    : ['bg-red'],
        'bg-blue'   : ['bg-blue'],
        'bg-green'  : ['bg-green'],
        'bg-yellow' : ['bg-yellow'],
        'bg-grey'   : ['bg-grey'],

        'strike'    : ['text-strike'],
        'mono'      : ['text-mono'],
        'underline' : ['text-underline'],
        'bold'      : ['text-bold'],
        'italic'    : ['text-italic'],
    }

    # Implementation of styles in Latex markup
    latex_styles = {
        'text-red'       : r'\textcolor{red}{',
        'text-blue'      : r'\textcolor{blue}{',
        'text-green'     : r'\textcolor{green}{',
        'text-yellow'    : r'\textcolor{yellow}{',

        'bg-red'         : r'\colorbox{red!20}{',
        'bg-blue'        : r'\colorbox{blue!20}{',
        'bg-green'       : r'\colorbox{green!20}{',
        'bg-yellow'      : r'\colorbox{yellow!20}{',
        'bg-grey'        : r'\colorbox{gray!10}{',

        'text-strike'    : r'\sout{',
        'text-mono'      : r'\texttt{',
        'text-underline' : r'\underline{',
        'text-bold'      : r'\textbf{',
        'text-italic'    : r'\textit{',
    }

    # Merge default roles with user-defined roles
    role_mapping = default_roles.copy()

    # Allow users to override or add new roles
    user_roles = config.text_formatting_roles or {}
    role_mapping.update(user_roles)

    # Store the mapping for use in translator
    app.config.text_styles = role_mapping
    app.config.latex_styles = latex_styles

    return role_mapping

# ==============================================================================
# Latex bits
# ==============================================================================

def add_preamble(app, filename):
    """
    Add custom LaTeX preamble to support inline formatting
    """
    preamble = r"""
    % Custom inline formatting
    \usepackage{color}
    \usepackage{soul}  % for background colours
    \usepackage{ulem}  % for strikethrough
    \usepackage{listings}  % for monospace
    """
    for package in ['color', 'soul', 'ulem', 'listings']:
        app.add_latex_package(package)

class CustomLaTeXTranslator(LaTeXTranslator):

    def visit_inline(self, node):
        # Retrieve the latex style mapping
        text_styles  = self.document.settings.env.text_styles
        latex_styles = self.document.settings.env.latex_styles

        # Get classes and find matching LaTeX commands
        classes = node.get('classes', [])

        # Track opened environments to ensure proper closing
        self._opened_environments = []

        for cls in classes:
            if cls in text_styles:
                latex_style = latex_styles[text_styles[cls]]
                self.body.append(latex_styles)
                self._opened_environments.append(cls)

        super().visit_inline(node)

    def depart_inline(self, node):
        super().depart_inline(node)

        # Close any opened environments in reverse order
        while self._opened_environments:
            self.body.append('}')
            self._opened_environments.pop()

# ==============================================================================
# Setup and role registration
# ==============================================================================

def copy_css(app):
    sphinx.util.fileutil.copy_asset(
        os.path.join(os.path.dirname(__file__), 'static', 'formatting.css'),
        os.path.join(app.builder.outdir, '_static'))

def process_formatting_roles(app, config):
    """
    Process and register formatting roles dynamically
    """
    # Create role mapping
    role_mapping = create_role_mapping(app, config)

    # Dynamically add roles
    for role_name, style_classes in role_mapping.items():
        app.add_role(role_name, FormattingRole(style_classes))

def setup(app):
    """
    Set up the Sphinx extension with custom roles and configuration
    """
    # Add configuration value for custom roles
    app.add_config_value('text_formatting_roles', {}, 'env')

    # Connect to configuration processing
    app.connect('config-inited', add_preamble)
    app.connect('config-inited', process_formatting_roles)

    # Add CSS for HTML output
    app.add_css_file('formatting.css')
    app.connect('builder-inited', copy_css)

    # Use custom translator for Latex
    app.set_translator('latex', CustomLaTeXTranslator, override=True)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
