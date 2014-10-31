.. title: SBML qual
.. slug: sbml-qual
.. date: 2014/08/06 21:37:11
.. tags: formats
.. link: 
.. description: Exchange format for logical models based on SBML
.. type: text


`SBML qual <http://sbml.org/Documents/Specifications/SBML_Level_3/Packages/Qualitative_Models_%28qual%29>`_
is an extension of the `Systems Biology Markup Language (SBML) <http://sbml.org>`_ Level 3 standard,
designed for the representation of multivalued qualitative models of biological networks.
The first SBML qual proposal in 2008 led to the creation of the CoLoMoTo consortium.
The extension was accepted by the SBML community in 2011, after consulting the wider
community and refining the original proposal through additional meetings with developers
of various related software tools.

The final specification was approved by the SBML Editors in the spring of 2013.


.. ref:: Chaouiya2013



Warning
-------

When importing SBML qual files, most softwares recover the interaction network from the functions associated to the components.
Thus Transitions lacking a FunctionTerm element will be ignored.
Similarly, if the math elements describing the FunctionTerms are not consistent, the interaction is not considered.

In the case of the Path2Models non-metabolic models in BioModels database (http://www.ebi.ac.uk/biomodels-main/path2models),
while the structure of the network is described and annotated, transitions have no function associated.
Those files are scaffolds of logical models from KEGG signaling pathways (see `Path2Models publication <http://www.biomedcentral.com/1752-0509/7/116>`_).

These SBML files can be imported using the Cytoscape plugin CytoCopter (http://www.cellnopt.org/cytocopter/) and,
using CellNOpt, train this scaffold network on data to get logical functions (http://www.cellnopt.org/).



