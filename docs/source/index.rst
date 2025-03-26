============================
Sphinx Text Styles Extension
============================

sphinxcontrib_text_styles is an extension providing a number of basic text style
roles, plus the ability to create alias roles with meaningful names. Styles have
both HTML (CSS) and PDF (Latex) implementations.

Built-in Styles
===============

Text Colors
-----------

.. code-block:: rst

    - :red:`Red text`
    - :blue:`Blue text`
    - :green:`Green text`
    - :yellow:`Yellow text`

- :red:`Red text`
- :blue:`Blue text`
- :green:`Green text`
- :yellow:`Yellow text`

Background Colors
-----------------

.. code-block:: rst

    - :bg-red:`Red background`
    - :bg-blue:`Blue background`
    - :bg-green:`Green background`
    - :bg-yellow:`Yellow background`
    - :bg-grey:`Grey background`

- :bg-red:`Red background`
- :bg-blue:`Blue background`
- :bg-green:`Green background`
- :bg-yellow:`Yellow background`
- :bg-grey:`Grey background`

Basic Text Styles
-----------------

- :bold:`Bold text`
- :italic:`Italic text`
- :mono:`Monospaced text`
- :strike:`Strikethrough text`
- :underline:`Underlined text`

Customizing Roles and Styles
============================

In your ``conf.py``, you can create custom roles that use one or more styles:

.. code-block:: python

   text_formatting_roles = {
       'success': ['text-green'],
       'error': ['text-red'],
       'important': ['text-red', 'text-italic', 'text-bold', 'text-underline'],
   }

You can then use these in your documentation:

.. code-block:: rst

  - :success:`Operation completed successfully`
  - :error:`Critical error occurred`
  - :important:`I can't emphasise this enough`

- :success:`Operation completed successfully`
- :error:`Critical error occurred`
- :important:`I can't emphasise this enough`
