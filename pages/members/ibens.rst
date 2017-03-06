.. title: Computational Systems Biology group
.. subtitle: IBENS - UMR ENS - CNRS 8197 - INSERM 1024 (Paris, FR)
.. tags: groups
.. geolocation: 48.842177, 2.343683
.. description: Functional genomic data analysis and logical modelling of cellular signaling/regulatory networks involved in cell fate decisions
.. members: Denis Thieffry, Aurélien Naldi, Céline Hernandez
.. website: http://www.ibens.ens.fr/spip.php?article26


Our team develop efficient tools to process functional genomic data and build computational models
of regulatory networks controlling mammalian cell differentiation.
We rely on the articulation of two approaches that are usually considered separately:
(i) a bioinformatic workflow to process epigenomic data and predict combinatorial transcriptional factor binding in promotors and enhancers;
(ii) a flexible logical modelling framework enabling the development of predictive models based on qualitative information,
e.g. regarding transcriptional factor binding and gene expression, potentially in the presence of genetic perturbations.
These two approaches are combined to decipher and model networks controlling mammalian cell fate, particularly focusing on blood cell specification, differentiation and reprogramming.

The first approach leans on the popular software RSAT (http://www.rsat.eu), which includes various algorithms for motif discovery and pattern matching, along with many utilities. We are currently extending this suite to support comparative and differential analyses of epigenomic data sets, including genome-wide DNA methylation and histone modification essays, in order to predict active enhancers, binding transcription factors and sites.

The second approach leans on the software GINsim (http://www.ginsim.org), dedicated to the definition and analysis of (multilevel) logical models of regulatory networks. To enable the analysis of larger networks (encompassing several hundreds of components), we are currently integrating advanced methods for model reduction, state transition graph compression, and model checking. We will further implement refinements of the logical framework through the association of probabilities with state transitions, to enable more quantitative simulations.


We are currently building a comprehensive model for the differentiation of T-helper cell into different canonical and hybrid subtypes in response to combinatorial signals (antigen presentation, co-stimulatory molecules, cytokines), in collaboration with the group of Dr Soumelis (Paris), who will provide systematic measurements (transcriptomics and proteomics).
In parallel, we are modelling the network controlling the specification of blood cells, primarily focusing on the myeloid and lymphoid pathways. In this respect, we rely on collaborations with Thomas Graf (Barcelona), Daniel Tenen (Singapore), and Ellen Rothenberg (Pasadena).
For both studies, we particularly focus on the articulation of three regulatory layers that are usually modelled separately: signalling pathways, transcriptional regulatory networks, and epigenetic remodelling mechanisms. We systematically exploit high-throughput data (from our partners or public repositories) to decipher the regulatory mechanisms (transcription factor binding at promoters and enhancers, epigenetic status) underlying functional effects (gene expression). We will progressively consider other functional data, starting with the roles of non coding RNAs known to affect blood cell fate.
Systematic confrontation of computational predictions against experimental data will foster model refinements until satisfactory recapitulation of cell responses to external signals and genetic perturbations. This then set the ground for predictive simulations of cell behaviour in novel situations, including responses to known drugs, with a emphasis on the delineation of efficient combinations of interventions, based on the prediction of synergistic effects of known drugs.


.. group_info::

