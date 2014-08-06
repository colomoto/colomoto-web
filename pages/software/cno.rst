.. title: CellNOpt (CellNetOptimizer)
.. tags: tools, related-groups
.. link: 
.. type: text
.. related-groups: ebi

See `cellnopt.org <http://www.cellnopt.org/>`_

CellNOpt is an open-source software used for creating logic-based models of signal transduction networks and training then with data.
While the core of CellNOpt consists of a set of R packages, it can be used through a Python wrapper, as well as a Cytoscape plug-in (CytoCopteR)
which provides support for the SBML qual format and a bridge for further analysis by other cytoscape plugins.

CellNOpt converts a network (a signed, directed graph) into a scaffold of all possible models compatible with the network and subsequently trains this scaffold with data [58]. It includes a variety of formalisms: (i) Boolean models, simulated via synchronous update or by computation of steady-states, (ii) semi-quantitative constrained Fuzzy logic, and (iii) ordinary differential equations (ODEs) derived from the logical model [30]. While the choice of a specific formalism depends on the data at hand, scope, and question, the followed workflow is similar. The network can be simplified by compressing nodes that are intermediates between perturbed or measured nodes. Links impinging on nodes that are not observable (with no readout downstream) or not controllable (with no perturbation upstream of them) are also taken aside as their status cannot be derived from the data.

CellNOpt generates logical models as hyper-graphs by adding all combinations of OR and AND gates that are compatible with the network (i.e., Sums of Products [59]). This leads to a hyper-graph representing a superposition of all Boolean models compatible with the initial network. Subsequently, an optimisation procedure is applied to find the combination of gates and the parameters that best explain the data, by minimising an objective function that quantifies the difference between data and simulation, while penalising model size. This provides an optimum model or, more generally, a family of optimal models. Optimisation can be performed using a built-in genetic algorithm, or using external optimisation packages; in particular CellNOpt is connected to Meigo [60]. Furthermore, CellNOpt can leverage Answer Set Programming to efficiently find all possible Boolean models via the software package caspo [61].

.. ref:: Terfve2012

