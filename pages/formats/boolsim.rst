.. title: boolsim
.. date: 2014/10/31 09:37:11
.. tags: formats
.. link: 
.. description: list of functions used by the boolsim tool
.. type: text
.. features: 

This format defines logical functions:

* Syntax: function -> target
* targets can be associated to multiple functions (combined with a OR)
* & denotes a AND, ^ denotes a NOT


Example::

  A & ^C -> A
  A & C -> B
  B -> B
  ^A -> C


Supported by
------------

.. usedby:: tools formats


