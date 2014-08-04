.. title: Updating policies
.. slug: policies
.. date: 2014/08/04 09:37:11
.. tags: 
.. link: 
.. description: 
.. type: text


The construction of the State Transition Graph (STG) relies on the logical functions, but also requires an /updating policy/,
which can have a strong impact on the resulting STG.
The asynchronous and synchronous policies are commonly used, but many alternatives exist.
These updating policies are listed and described in the following.

In the synchronous case, all logical regulatory functions are applied simultaneously to update the corresponding network components.
This means that there is exactly one possible successor for each node of the STG.
In the asynchronous case, only one node is updated at each time point, i.e. a separate transition is possible for each component.
Here, many alternative paths in the STG can exist. The asynchronous updating policy, considering many concurrent successor states for the
exploration of the STG, may become untractable for the analysis of large models, while the synchronous alternative may prove too simplistic.

To analyse large models using asynchronous updates, one can alternatively randomly pick a single component to be updated at each step,
leading to a single successor. This "random walk" in the asynchronous STG is repeated to create a sampling of
the reachable attractors. More generally, such random walks can be applied to any updating policy which yields multiple successors.

The sequential updating policy can be seen as a special case of asynchronous updating.
Here, an ordering of the nodes is determined, and a sequence of successor states can be constructed by applying the regulatory functions in this order.
Like in the synchronous case, there is only a single successor state at each step.
The chosen order of the components can dramatically change the resulting STG.

The block-sequential policy provides a more general policy based on the same principle.
The components are still ordered, but groups of components can be updated synchronously (in blocks).
The sequential and the synchronous policies are special cases of the block-sequential policy.


An alternative approach relies on the definition of priority classes: grouping components depending on their qualitative production
and/or degradation delays, and assigning a priority to each group of components. These groups can themselves be considered synchronous or asynchronous.
Then, at any state, among all concurrent transitions, only those belonging to the group with highest priority are called to be updated.

