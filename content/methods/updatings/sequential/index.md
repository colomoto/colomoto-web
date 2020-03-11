---
title: "Sequential"
date: 2014/10/31 09:37:11
summary: Sequential updating policy
methods: sequential
---


The sequential updating requires the definition of an ordering of the components.
This updating is deterministic: each state has a single successor.
The successor of a state is obtained by updating all components in the defined order,
such that the update of each component takes into account the changes of the previous ones.


As the state is updated between each components, this defines a sequence of intermediate
successors leading to the final state. A transition from a state to its successor then
corresponds to a trajectory in the asynchronous updating.

The chosen order of the components can dramatically change the resulting dynamics.

