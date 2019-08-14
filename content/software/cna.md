---
title: "CellNetAnalyzer"
summary: A MATLAB package with graphical user interface for structural and functional analysis of cellular networks
website: http://www2.mpi-magdeburg.mpg.de/projects/cna/cna.html
related-groups: mpi-magdeburg
formats: 
features: multivalued
---


CellNetAnalyzer (CNA) is a MATLAB toolbox providing a graphical user interface and various
(partially unique) computational methods and algorithms for exploring structural and functional
properties of metabolic, signaling, and regulatory networks.

Metabolic networks are formalized and analyzed by stoichiometric and constraint-based
modeling techniques, including flux balance analysis (FBA), metabolic flux analysis,
elementary-modes analysis, minimal cut set analysis, and many more. Several algorithms
are provided for computational strain design / metabolic engineering.

Signal transduction and (gene) regulatory networks are represented in CNA as logical networks
(both Boolean and multivalued logic are supported) or/and as interaction graphs.
Among other features, CNA supports logical steady state analysis (e.g., for studying the
input-output behavior of signaling networks), the computation of minimal intervention sets
enforcing or blocking certain behaviors, discrete simulations of Boolean models as well as
simulation of logic-based ODEs derived from Boolean models (via ODEfy plugin).
Methods for studying properties of interaction graphs include enumeration and analysis 
of feedback loops and signaling paths as well as analysis of global interdependencies.

Provided algorithms can be invoked within the GUI or from command line via API functions.


{{<ref Klamt2007>}}



