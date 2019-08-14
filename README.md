
This repository hosts the source files behind the colomoto web pages on http://draft.colomoto.org.
It uses the hugo static generator: each page is a simple text file using a wiki-like markup.


Requirements and initial setup
=============================

* install the hugo binary from https://gohugo.io/



Adding/editing pages
====================


Folder organisation
-------------------

* the content of the "static" folder will be copied directly to the output.
* the main pages are in the "content" folder: they will be parsed by hugo and turned into HTML according to layout templates


Markup
------

Pages are written in markdown with some custom extensions (i.e. hugo's shortcodes)


* Titles are underlined.
  While there is no fixed rule to associate one underline-style to one title level (the first style used is associated to the higher level titles),
  we generally use "======" lines for sections and "-----" lines for subsections. The line should be as long as the title text.
* Skip at least one line to change paragraph. Line breaks inside paragraphs are ignored.
* define a list with "*" (unnumbered) or "#" (numbered).
* To add a simple link, just put a raw URL: http://www.colomoto.org.
* A more powerful syntax for links is available for relative links and custom text:
  [your text](http://www.colomoto.org) (look at the source of this file, not the rendered version on github).



Custom shortcodes
-----------------

We can define custom markup in the md files (called shortcodes) using a template language.

* Some groups of pages have custom layout for their metadata
* References are loaded and rendered based on a JSON representation

