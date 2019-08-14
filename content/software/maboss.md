---
title: "MaBoSS"
website: https://maboss.curie.fr/
related-groups: curie
summary: Continuous time Boolean modeling
formats: 
methods: stochastic
features: 
---

MaBoSS (Markovian Boolean Stochastic Simulator) is a C++ software for simulating continuous/discrete time Markov processes based on Boolean networks.
It relies on a specific language to define the model and transition rates, and applies the Gillespie algorithm to produce time trajectories.
The evolution of probabilities over time is estimated, and global and semi-global characterizations of the whole system are computed. 

The LogicalModel library provides an export filter to the MaBoSS format, and conversion of MaBoSS models to SBML qual are planned.


{{<ref Stoll2012>}}



