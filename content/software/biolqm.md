---
title: "bioLQM: Logical Qualitative Modelling toolkit"
summary: Java library for the manipulation and conversion of logical models
website: http://colomoto.org/biolqm
members: 
- ibens
formats: 
- sbml-qual
- boolsim
- truthtable
methods:
- multivalued
---

This library provides a datastructure for the representation of logical models, and a collection of
filters to load or save these models in various formats, facilitating the interoperability between
tools which do not directly support SBML qual. It relies on JSBML for SBML qual support.

It can be used on the command line for model conversion or stable state identification.
It can also provide the "boring core" for other tools (such as GINsim and Epilog) which can benefit
from additional API for the representation of perturbations or simulation engines.

{{<ref Naldi2018c>}}



