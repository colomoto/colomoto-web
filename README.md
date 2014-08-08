What is this?
=============

The source files behind the colomoto web pages on http://draft.colomoto.org


Requirements and initial setup
=============================

This site uses the nikola static generator.


Virtualenv
----------

To avoid messing with your system-level python packages, we encourage the use of virtualenv,
which provides separate collections of python packages and a mechanism to switch from one to the other.

* install virtualenv and virtualenv-wrapper
* virtualenvwrapper requires to configure your shell:
  load some helper shortcuts and define the default folder for virtualenv installations

See http://virtualenv.readthedocs.org/en/latest/virtualenv.html for more details.


Using virtualenv:

* use the "workon virtenvName" command to enter your virtualenv
* use the "deactivate" command to get back to your normal environment


Nikola
------

Nikola (http://getnikola.com) is a static site generator: it takes text files in light markup, applies templates and turns them into a set of consistent web pages.


Installation (in your virtualenv):  pip install nikola[extras]

As of now, it will install nikola 7.0.1 and dependencies and provide a "nikola" command.
Usage:

* nikola build: build the site in the output folder
* nikola serve: launch a minimalist local web server to test it
* nikola clean: clean the cache (to force a rebuild)



Adding/editing pages
====================


Folder organisation
-------------------

* the content of the "files" folder will be copied to the output. images, pdfs,... should go in this folder
* the main pages are in the "pages" folder: they will be parsed by nikola and turned into HTML before going to the output folder
* the pages in the "news" folder make up the news section. A RSS feed and archive pages are generated from them.


Markup
------

Most pages are defined in files with a "rst" extension.
These pages use the restructuredtext markup (http://en.wikipedia.org/wiki/ReStructuredText) with some extensions.
Here are a few instructions for editing, refer to the main RST and nikola documentations for more details.


* Titles are underlined.
  While there is no fixed rule to associate one underline-style to one title level (the first style used is associated to the higher level titles),
  we generally use "======" lines for sections and "-----" lines for subsections. The line should be as long as the title text.
* Skip at least one line to change paragraph. Line breaks inside paragraphs are ignored.
* define a list with "*" (unnumbered) or "#" (numbered).
* To add a simple link, just put a raw URL: http://www.colomoto.org.
* A more powerful syntax for links is available for relative links and custom text:
  `your text <http://www.colomoto.org>`_ (look at the source of this file, not the rendered version on github).
  Note the ending underline and beware the weird quotes!

rst reference: http://docutils.sourceforge.net/docs/user/rst/quickref.html


Custom directives and annotations
---------------------------------

We can define custom commands (called directives) using plugins.

* Each group or tool page must be tagged as such in the metadata (.. tag: groups).
* We curently have a ".. listof:: groups" directive to generate the lists of groups, which will find all pages
  associated to the desired tag. The same method is used for tools and meetings pages.
* group pages should also define two extra metadata: geolocation and members.
* We plan to add some directives to make it easier to properly format references.

