============================
Sphinx Text Styles Extension
============================

.. contents:: Contents
   :depth: 1
   :local:
   :backlinks: none


Introduction
============

This extension provides a number of basic text style roles, plus the ability to
create additional styles, and alias roles with meaningful names. Styles have
both HTML (CSS) and PDF (Latex) implementations.

The aim is for users to be able to define character styles meaningful to their
document, and have them render in HTML and PDF, without having to author CSS and
Latex markup themselves.

.. admonition:: Rationales

   Stackoverflow is full of "how do I make my text red in Sphinx" type
   questions. The answers are generally HTML-specific, and require the user to
   insert RST preambles and custom CSS for what should be trivial. This
   extension aims to make it trivial, and portable across multiple builders.

   Word-processing software allows users to easily create character styles named
   for their use cases. This extension aims to do the same.

.. tip::

   It's good practice to name your styles after what they represent, rather than
   how they are rendered. For example, let's say you're documenting a CPU and
   want all the opcodes to stand out. There are multiple approaches:

   .. code-block:: rst

      ``NOP``
      :text-mono:`NOP`
      :opcode:`NOP`

   We might use built-in RST markup to format the opcodes, but that's quite
   limited, and awkward to change later.

   We might use a role descriptive of the formatting, but again it's awkward to
   change our minds.

   Best to use a role descriptive of the *thing*, and define how the thing gets
   formatted elsewhere, and only once.

.. warning::
  How good any of this looks is likely to be affected by your choice of theme!

Installation
============

Install the extension in your Python environment:

.. code-block::

  pip install sphinxcontrib-text-styles

Enable the extension in the ``conf.py`` of your document:

.. code-block:: python

  extensions = [
      'sphinxcontrib_text_styles',
      ...
  ]

Built-in Styles
===============

The extension provides a number of built-in styles. These can be used directly,
or referenced in a :ref:`custom role <custom_roles>`.

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

Text and Background Colors
--------------------------

The built in list of colours comes from
https://www.overleaf.com/learn/latex/Using_colors_in_LaTeX#Named_colors_provided_by_the_xcolor_package,
all of which are recognised by both Latex and CSS.

Further colours are possible with :ref:`custom_styles`.

.. code-block:: rst

    :text-red:`Red text` :bg-red:`Red background`
    :text-green:`Green text` :bg-green:`Green background`
    :text-blue:`Blue text` :bg-blue:`Blue background`
    :text-cyan:`Cyan text` :bg-cyan:`Cyan background`
    :text-magenta:`Magenta text` :bg-magenta:`Magenta background`
    :text-yellow:`Yellow text` :bg-yellow:`Yellow background`
    :text-black:`Black text` :bg-black:`Black background`
    :text-gray:`Gray text` :bg-gray:`Gray background`
    :text-white:`White text` :bg-white:`White background`
    :text-darkgray:`Darkgray text` :bg-darkgray:`Darkgray background`
    :text-lightgray:`Lightgray text` :bg-lightgray:`Lightgray background`
    :text-brown:`Brown text` :bg-brown:`Brown background`
    :text-lime:`Lime text` :bg-lime:`Lime background`
    :text-olive:`Olive text` :bg-olive:`Olive background`
    :text-orange:`Orange text` :bg-orange:`Orange background`
    :text-pink:`Pink text` :bg-pink:`Pink background`
    :text-purple:`Purple text` :bg-purple:`Purple background`
    :text-teal:`Teal text` :bg-teal:`Teal background`
    :text-violet:`Violet text` :bg-violet:`Violet background`

- :text-red:`Red text` :bg-red:`Red background`
- :text-green:`Green text` :bg-green:`Green background`
- :text-blue:`Blue text` :bg-blue:`Blue background`
- :text-cyan:`Cyan text` :bg-cyan:`Cyan background`
- :text-magenta:`Magenta text` :bg-magenta:`Magenta background`
- :text-yellow:`Yellow text` :bg-yellow:`Yellow background`
- :text-black:`Black text` :bg-black:`Black background`
- :text-gray:`Gray text` :bg-gray:`Gray background`
- :text-white:`White text` :bg-white:`White background`
- :text-darkgray:`Darkgray text` :bg-darkgray:`Darkgray background`
- :text-lightgray:`Lightgray text` :bg-lightgray:`Lightgray background`
- :text-brown:`Brown text` :bg-brown:`Brown background`
- :text-lime:`Lime text` :bg-lime:`Lime background`
- :text-olive:`Olive text` :bg-olive:`Olive background`
- :text-orange:`Orange text` :bg-orange:`Orange background`
- :text-pink:`Pink text` :bg-pink:`Pink background`
- :text-purple:`Purple text` :bg-purple:`Purple background`
- :text-teal:`Teal text` :bg-teal:`Teal background`
- :text-violet:`Violet text` :bg-violet:`Violet background`

.. _custom_roles:

Custom Roles
============

In your ``conf.py``, you can define roles that use one or more of the basic
styles:

.. code-block:: python

   text_styles_roles = {
       'success': ['text-green'],
       'error': ['text-red'],
       'important': ['text-red', 'text-italic', 'text-bold', 'text-underline', 'bg-black'],
   }

You can then use these in your documentation:

.. code-block:: rst

  - :success:`Operation completed successfully`
  - :error:`Critical error occurred`
  - :important:`I can't emphasise this enough`

- :success:`Operation completed successfully`
- :error:`Critical error occurred`
- :important:`I can't emphasise this enough`

.. _custom_styles:

Custom Styles
=============

In your ``conf.py`` you can define additional style roles with their CSS and
Latex implementations, which can then be used directly or as part of your custom
roles:

.. code-block:: python

    text_styles_styles = {
        'text-small-caps' : ("font-variant: small-caps;", r'\textsc{'),
    }

    text_styles_roles = {
        'legal-term' : ['text-small-caps', 'text-bold']
    }


.. code-block:: rst

    - :text-small-caps:`Small caps`
    - :legal-term:`Defendant`

- :text-small-caps:`Small caps`
- :legal-term:`Defendant`

Details
-------

Each member of ``text_styles_styles`` has the style/role name as the key,
followed by a tuple containing ``(CSS, Latex)``.

The CSS goes into a stylesheet as: ``.<style-name> { <your CSS here> }``,
meaning multiple attributes can be set.

The Latex goes directly in the markup: ``<your-Latex-here>Original text}``. Note
the single closing ``}``. You CANNOT use multiple Latex tags in a single style
(but you can stack them up by using multiple styles in a custom role).

If you're only interested in one builder you can leave the implementation for
the other blank.

Issues / Feedback
=================

Raise any bugs or suggested enhancements on the issue tracker:
https://github.com/martinpriestley/sphinxcontrib-text-styles/issues
