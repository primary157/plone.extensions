====================
rapido.extensions
====================

**Extending Rapido.Plone**

**rapido.plone repository:** *https://github.com/collective/rapido.plone*

What for?
---------

Creating a small form able to send an email, or to store some data, generating
some extra information about a page and inserting it wherever we want: with Plone
these kind of tasks are complex for experts, and almost impossible for beginners.

**rapido.extensions** allows any developer having a little knowledge of HTML and a
little knowledge of Python to implement custom elements and insert them anywhere
they want in their Plone site.

How?
----

The unique interface to build applications with rapido.extensions is the **Plone
theming tool**.

This means that it can be done on the **file system** or through the 
**inline theming editor**.

A Rapido application is just a part of our current theme; it can be
imported, exported, copied, modified, etc. like the rest of the theme.

Moreover, we can use `Diazo <http://docs.diazo.org/en/latest/>`_ extensively to
inject our application in the Plone layout easily.

Documentation and screencast
----------------------------

- Full `Rapido documentation <http://rapidoplone.readthedocs.org/en/latest/>`_.

    - `Rapido Spanish documentation <http://rapidoplone-spanish.readthedocs.io/es/latest/>`_.

- How to implement a rating system in 3'33'' (`tutorial <http://rapidoplone.readthedocs.org/en/latest/tutorial.html>`_,
  `screencast <https://www.youtube.com/watch?v=a7B-lX0caW0>`_).

- How to implement a glossary system as a tool to manage a list of terms (`tutorial <http://rapidoplone.readthedocs.io/en/latest/use-cases/glossary.html>`_).

- How to use Rapido to create custom SearchableText field (`tutorial <http://rapidoplone.readthedocs.io/en/latest/use-cases/book.html>`_).

- `example.rapidoplone <https://github.com/collective/example.rapidoplone>`_, is a source code package for differents examples "rapido.extensions" apps.

Credits
-------

|makinacom|_

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com
