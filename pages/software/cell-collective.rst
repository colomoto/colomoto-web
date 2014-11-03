.. title: The Cell Collective
.. tags: tools, related-groups
.. description: Web-based plateform for the construction and simulation of Boolean models
.. link: 
.. type: text
.. related-groups: nebraska
.. formats: sbml-qual
.. features: 


The Cell Collective (see `www.thecellcollective.org <http://www.thecellcollective.org>`_) is a web-based platform for the construction,
simulation, and analysis of Boolean-based models.

The platform includes a Knowledge Base facilitating the collaborative annotation of the models by tracking the evidence associated with each interaction.
Models defined in the platform can be shared directly on the web or exported as SBML qual files (or as text files listing logical expressions and truth tables).

The Cell Collective relies on the ChemChains engine, the user can assign a probability of being active in time t to each external species (i.e., those with no regulators),
in contrast to classical Boolean simulations where they are fixed to 0 or 1. The activity level of the output species is then defined as the ratio of 0’s and 1′s
over a configurable number of time steps in multiple synchronous simulations.

.. ref:: Helikar2012

