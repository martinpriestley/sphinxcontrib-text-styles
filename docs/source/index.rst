============================
Sphinx Text Styles Extension
============================

sphinxcontrib_text_styles is an extension providing a number of basic text style
roles, plus the ability to create additional styles, and alias roles with
meaningful names. Styles have both HTML (CSS) and PDF (Latex) implementations.

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

.. _custom_roles:

Customizing Roles
=================

In your ``conf.py``, you can define roles that use one or more of the basic
styles:

.. code-block:: python

   text_styles_roles = {
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

Customizing Styles
==================

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
