---
title: "GNA format"
date: 2014/10/31 09:37:11
summary: Model representation in GNA (non-xml) format
features: multivalued
---
This format defines the representation of a model through the use of piecewise-linear differential equations (PLDEs).
For each variable, the domain partitions must be defined by the *threshold-parameters*, as well as the synthesis and degradation parameters (*synthesis-parameters* and *degradation-parameters*).
The rules afecting the system are then given by a set of inequality constraints on the parameters.

See http://ibis.inrialpes.fr/people/dejong/GNA/user/ch02.html 

Example::

  state-variable: geneB
    zero-parameter: zero_geneB
    box-parameter: max_geneB
    threshold-parameters: t1_geneB
    synthesis-parameters: k1_geneB
    degradation-parameters: g_geneB
    state-equation:
      d/dt geneB = k1_geneB * s-(geneA,t1_geneA)
          - g_geneB * geneB
    parameter-inequalities:
      zero_geneB < t1_geneB < k1_geneB / g_geneB < max_geneB
  state-variable: geneA
    zero-parameter: zero_geneA
    box-parameter: max_geneA
    threshold-parameters: t1_geneA
    synthesis-parameters: k_geneA, k1_geneA
    degradation-parameters: g_geneA
    state-equation:
      d/dt geneA = k_geneA
          - g_geneA * geneA
    parameter-inequalities:
      zero_geneA < k_geneA / g_geneA < t1_geneA < k1_geneA / g_geneA < max_geneA


Supported by
------------

.. usedby:: tools formats


