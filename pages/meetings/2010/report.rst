.. title: Report for the first CoLoMoTo meeting (Lisbon, 2010)
.. date: 2010/11/25 21:26:37
.. tags: 
.. description: 


This report is a synthesis of the `1st CoLoMoTo meeting <index.html>`_.
This two days meeting was dedicated to presentations on tools, methods and models (listed on the main page indicated above) and to discussions summarised here.


Motivations
===========

* Need for a flexible and biologist-friendly toolbox for qualitative modelling, including parameter derivation
* Different ways to approach model definition: spreadsheet, wiki, graphs, rules/formula/constraints
* Need scaling up!!!
* Improve model annotations, using existing standards (MIRIAM)
* Friendly database lookup system
* Import of pathways, e.g. from Reactome (more than 60 resources claiming that they encode pathways, but most pumping from each other without true curation!)
* Models should be easy to grasp by biologist, but maybe not easily defined by biologists
* Biologist should be strongly involve in the initial stage, to define model components and interactions
* Need for optimisation of the creation and edition of networks, from both sides (graphs and rules)
* Comparison of model dynamics and omic data sets (expression) – generic need
* Common tools would enable different groups to further focus on their own research
* Success stories? Show cases?


Aims
====

* Provide a common toolbox for qualitative (discrete) modelling of biological (regulatory)
  networks, taking advantage of existing softwares
* Define the functionalities and implementation strategies
* Set up a consortium, gathering the key players, to apply for financial support, ensure a better
  visibility of this modelling framework, profit from complementary methods and approaches


Logical model editor(s)
=======================

Common, modular core, making Cytoscape 3.0 code covering node/interaction listing/annotation,
graph edition, rule edition
Feasibility study: Martial, Aurélien, Pedro, Benno => discussion with core Cytoscape developers
Pre-defined, modifiable generic rules
Interfacing with Cytoscape (+ CellDesigner, others?)

Modules: Java plugins and/or web services

* Stable state identification
* Dependency matrix (approximation, exact solutions computationally expensive )
* Minimal intervention sets (computationally expensive)
* Model checking and temporal logic patterns
* Model reduction
* Model de/composition
* Interaction/circuit functionality analysis, canalisation, dependencies
* Inference of interactions or rules from state transition graphs or traces
* Compression of regulatory function and alternative standard forms for logical formula
* Compression of STG
* (Probabilistic) reachability analyses
* Data discretisation
* Parameter sensitivity and bifurcation analysis


Transversal issues:

* Parallelisation of some algorithms => shared library
* dealing with abstract (classes of) models


Benchmarking and case studies

* Make a list of reference models + artificial ones if needed
* Assess the functionalities of the different software modules
* Reference network modules for composition (drosophila development, cell cycle, apopotosis, signalling pathways, ...)
* Network inference: reference model and dynamic traces, DREAM


Organisational issues
=====================

Launching of a consortium with all the groups represented => 1 member per group to form a provisional board:

* IGC (Claudine)
* Univ Nebraska Omaha (Tomas)
* EBI (Julio)
* UnivMed (Laurent)
* SIB-UNIL (Ioannis)
* Institut Curie (Andrei)
* Institut Pasteur (Benno)
* ENS (Denis)
* MPI Magdeburg (Steffen)


In the future, co-option of additional groups.

Possibility to mobilise EBI support, starting with the organisation of a meeting/visiting group
Wiki/Webpage at IGC for the time being, with minutes of the meeting, the list of groups and
representative members.

We plan to organize the next meeting at EBI or Switzerland (spring 2012?)

Funding: Some possibilities in Switzerland and EBI. We should also consider FP7, NIH and joint founding.

