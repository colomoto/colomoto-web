---
title: "Block-Sequential"
date: 2014/10/31 09:37:11
summary: Sequential updating of synchronous groups of components
methods: block-sequential
---



The block-sequential updating requires the definition of an ordered partition of the components.
This updating is deterministic updating: each state has a single successor.
The components in the first group are first updated synchronously.
The resulting state is then used to update the components of the second group and so on.


The sequential updating is a special case of the block-sequential one, where all groups contain a single component.

The synchronous updating corresponds to the block-sequential with a single group containing all components.

A transition in the block-sequential updating corresponds to at least one
of the alternative trajectories in the generalized asynchronous one.

