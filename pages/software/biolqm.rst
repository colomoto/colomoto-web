.. title: Logical Qualitative Modelling toolkit
.. tags: tools, related-groups
.. description: Java library for the manipulation and conversion of logical models
.. link: 
.. type: text
.. website: http://colomoto.org/biolqm
.. related-groups: 
.. formats: sbml-qual, boolsim, truthtable
.. features: multivalued

.. tool_header::

This library provides a datastructure for the representation of logical models, and a collection of
filters to load or save these models in various formats, facilitating the interoperability between
tools which do not directly support SBML qual. It relies on JSBML for SBML qual support.

It can be used on the command line for model conversion or stable state identification.
It can also provide the "boring core" for other tools (such as GINsim and Epilog) which can benefit
from additional API for the representation of perturbations or simulation engines.

.. ref:: Chaouiya2013


.. tool_info::

