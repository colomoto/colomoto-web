---
title: "TruthTable"
date: 2014/10/31 09:37:11
summary: Represents the synchronouns dynamics formated as a two-column text file.
features: multivalued
---

This format is represented as a two-column file where each line contains a source state followed by its corresponding target state, in the synchronouns dynamics.
The first line of the table can have a non-mandatory list of node identifiers to be used.
This file can be incomplete i.e., can lack information regarding some of the source states of the corresponding state transition graph.

See http://doc.ginsim.org/format-truthtable.html


# Sample

```
GeneA GeneB GeneC
000 100
001 010
# This is a comment
010 110
011 110
100 100
# Yet another unnecessary comment
101 000
110 110
111 110
```


