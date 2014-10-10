.. title: Genetic Network Analyzer (GNA)
.. tags: tools, related-groups
.. description: Genetic Network Analyzer (GNA) is a computer tool for the qualitative modeling, analysis, and simulation of gene regulatory networks
.. link: 
.. type: text
.. related-groups: ibis


The aim of GNA is to assist biologists and bioinformaticians in constructing a model of a gene regulatory network using knowledge about regulatory interactions in combination with gene expression data. GNA consists of a simulator of qualitative models of genetic regulatory networks in the form of piecewise-linear differential equations. Instead of exact numerical values for the parameters, which are often not available for networks of biological interest, the user of GNA specifies inequality constraints. This information is sufficient to generate a state transition graph that describes the qualitative dynamics of the network. GNA has been coupled to state-of-the art model checking tools to formulate and verify properties of the state transition graph that are of biological interest. GNA has been implemented in Java and has been applied to the analysis of various regulatory systems, such as the networks controlling the carbon starvation response in E. coli and the biodegradation of polluants by P. putida.

More information can be found at http://www-helix.inrialpes.fr/gna.

.. ref:: Batt2012

