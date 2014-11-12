.. title: Stochastic simulations
.. date: 2014/10/31 09:37:11
.. tags: methods, :simulation
.. link: 
.. description: 
.. type: text


To analyse large models using asynchronous updates, one can alternatively randomly pick a single component to be updated at each step,
leading to a single successor. This "random walk" in the asynchronous STG is repeated to create a sampling of
the reachable attractors. More generally, such random walks can be applied to any updating policy which yields multiple successors.

.. method_info:: 

