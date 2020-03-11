---
title: "Priority classes"
date: 2014/10/31 09:37:11
summary: Updating policy relying on strict priorities
methods: priority
---

Priority classes define a partition of components depending on their production and/or degradation delays.
Each group of components is associated to a priority rank.
These groups can themselves be considered synchronous or asynchronous.

The priority groups are evaluated in order.
If none of the components in the group can be updated, then the next group is considered.
Otherwise, all components in the group are considered (synchronously or asynchronously depending 
on the definition of the current group).
Components belonging to groups with lower priority rank are ignored.

This updating is non-deterministic in the general case (each state can have several successors).
It can be deterministic if all priority classes are synchronous or contain a single component.

