.. title: EpiLog
.. description: Simulation of epithelial patterning using multi-cellular multivalued logical models
.. tags: tools, related-groups
.. link: http://ginsim.org/epilog
.. type: text
.. website: http://ginsim.org/epilog
.. related-groups: igc inesc
.. formats: sbml-qual
.. features: multivalued


.. tool_header::

EpiLog is a Java software for the qualitative simulation of epithelial patterning.

It defines an epithelium as a 2D grid of hexagonal cells, each containing a LRG regulating the internal proper components.
It is also capable of integrating as input components of each cell, stable environmental influences as well as varying signals from neighbouring cells.
The software provides a graphical user interface representing the hexagonal grid of cells to facilitate the definition of initial conditions,
definition of perturbations, and visualization of the simulation. The latter is performed synchronously with respect to all components of all cells.

It relies on the `LogicalModel <https://github.com/colomoto/logicalmodel>`_ library to import multi-valued logical models from SBML qual and compute the successor states.



.. tool_info::

