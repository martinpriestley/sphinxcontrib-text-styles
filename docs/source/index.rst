============================
Sphinx Text Styles Extension
============================

sphinxcontrib_text_styles is an extension providing a number of basic text style
roles, plus the ability to create alias roles with meaningful names. Styles have
both HTML (CSS) and PDF (Latex) implementations.

The aim is for users to be able to define character styles meaningful to their
document, and have them render in HTML and PDF, without having to author CSS and
Latex markup themselves.

Built-in Styles
===============

Basic Text Styles
-----------------

.. code-block:: rst

    - :text-bold:`Bold text`
    - :text-italic:`Italic text`
    - :text-mono:`Monospaced text`
    - :text-strike:`Strikethrough text`
    - :text-underline:`Underlined text`

- :text-bold:`Bold text`
- :text-italic:`Italic text`
- :text-mono:`Monospaced text`
- :text-strike:`Strikethrough text`
- :text-underline:`Underlined text`

Text Colors
-----------

.. code-block:: rst

    :text-red:`Red text`
    :text-green:`Green text`
    :text-blue:`Blue text`
    :text-cyan:`Cyan text`
    :text-magenta:`Magenta text`
    :text-yellow:`Yellow text`
    :text-black:`Black text`
    :text-gray:`Gray text`
    :text-white:`White text`
    :text-darkgray:`Darkgray text`
    :text-lightgray:`Lightgray text`
    :text-brown:`Brown text`
    :text-lime:`Lime text`
    :text-olive:`Olive text`
    :text-orange:`Orange text`
    :text-pink:`Pink text`
    :text-purple:`Purple text`
    :text-teal:`Teal text`
    :text-violet:`Violet text`


- :text-red:`Red text`
- :text-green:`Green text`
- :text-blue:`Blue text`
- :text-cyan:`Cyan text`
- :text-magenta:`Magenta text`
- :text-yellow:`Yellow text`
- :text-black:`Black text`
- :text-gray:`Gray text`
- :text-white:`White text`
- :text-darkgray:`Darkgray text`
- :text-lightgray:`Lightgray text`
- :text-brown:`Brown text`
- :text-lime:`Lime text`
- :text-olive:`Olive text`
- :text-orange:`Orange text`
- :text-pink:`Pink text`
- :text-purple:`Purple text`
- :text-teal:`Teal text`
- :text-violet:`Violet text`

Background Colors
-----------------

.. code-block:: rst

    :bg-red:`Red background`
    :bg-green:`Green background`
    :bg-blue:`Blue background`
    :bg-cyan:`Cyan background`
    :bg-magenta:`Magenta background`
    :bg-yellow:`Yellow background`
    :bg-black:`Black background`
    :bg-gray:`Gray background`
    :bg-white:`White background`
    :bg-darkgray:`Darkgray background`
    :bg-lightgray:`Lightgray background`
    :bg-brown:`Brown background`
    :bg-lime:`Lime background`
    :bg-olive:`Olive background`
    :bg-orange:`Orange background`
    :bg-pink:`Pink background`
    :bg-purple:`Purple background`
    :bg-teal:`Teal background`
    :bg-violet:`Violet background`

- :bg-red:`Red background`
- :bg-green:`Green background`
- :bg-blue:`Blue background`
- :bg-cyan:`Cyan background`
- :bg-magenta:`Magenta background`
- :bg-yellow:`Yellow background`
- :bg-black:`Black background`
- :bg-gray:`Gray background`
- :bg-white:`White background`
- :bg-darkgray:`Darkgray background`
- :bg-lightgray:`Lightgray background`
- :bg-brown:`Brown background`
- :bg-lime:`Lime background`
- :bg-olive:`Olive background`
- :bg-orange:`Orange background`
- :bg-pink:`Pink background`
- :bg-purple:`Purple background`
- :bg-teal:`Teal background`
- :bg-violet:`Violet background`

Customizing Roles and Styles
============================

In your ``conf.py``, you can define roles that use one or more of the basic
styles:

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
