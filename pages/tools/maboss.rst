.. title: MaBoSS
.. tags: tools, related-groups
.. related-groups: curie
.. description: Continuous time Boolean modeling

MaBoSS (Markovian Boolean Stochastic Simulator) is a C++ software for simulating continuous/discrete time Markov processes based on Boolean networks.
It relies on a specific language to define the model and transition rates, and applies the Gillespie algorithm to produce time trajectories.
The evolution of probabilities over time is estimated, and global and semi-global characterizations of the whole system are computed. 

The LogicalModel library provides an export filter to the MaBoSS format, and conversion of MaBoSS models to SBML qual are planned.
See https://maboss.curie.fr/.

.. ref:: Stoll2012

