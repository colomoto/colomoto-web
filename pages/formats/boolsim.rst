.. title: Boolsim
.. date: 2014/10/31 09:37:11
.. tags: formats
.. link: 
.. description: list of functions used by the boolsim tool
.. type: text
.. features: 

This format defines a model as a list of activating and inhibiting conditions of its components.

* The conditions use the & operator for AND, and ^ for NOT
* Activations are defined as: condition -> target
* Inhibitions are defined as: condition -| target
* The complete function will be: (activation1 OR activation2) & !(inhibition1 OR inhibition2)


Example::

  A&^C -> A
  A&C -| B
  B -> B
  ^A -> C


Supported by
------------

.. usedby:: tools formats


