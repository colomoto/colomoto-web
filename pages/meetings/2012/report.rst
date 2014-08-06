.. title: Report for the second CoLoMoTo meeting (Hinxton, 2012)
.. date: 2012/06/19 21:37:11
.. tags: 
.. description: 


This report is a synthesis of the `2nd CoLoMoTo meeting <index.html>`_
This two days meeting was dedicated to presentations on tools, methods and models (slides are available on the main page indicated above) and to discussions summarised here.


Objective of the CoLoMoTo project
=================================


* Integrate community: is being reached through colomoto meetings
  Still a lot of outsiders / newcomers
* Clarification of classes of models / terms
  !!! Start a wikipedia page on logical modelling
  Denis has a draft...
* Special session / SIG / workshop / course
* Focus on project as a whole instead of single tool will increase visibility of the project.
* Exchange models -> SBML-qual
* Andreas asks about possible alternatives

  * Petri net format -> not suitable for qualitative models per se.
* Common platform -> Cytoscape-based - prototype. 

  * Not essential, but nice to have
  * Slowly shift development effort towards this toolbox...
  * Reduced maintenance effort.
  * Feature rich or minimal? -> Plug-ins


Mission/Purpose Statement
-------------------------

The Common Logical Modeling Toolbox (CoLoMoTo) consortium aims at integrating the scientific community utilizing logic-based modeling to study biological systems. The main goal of CoLoMoTo is to create a common ground in the form of software tools, methodologies, and models for research groups employing logical modeling. As an international effort, we strive to generate more visibility and adoption of this powerful computational approach.



Project structure
------------------

Should we define a more formal structure (editors, scientific advisors)?
It seems too early for this, continue discussion with Nicolas Le Novère.


Funding
-------

* Funding for travel would be possible.
* Funding to hire a person seems out of scope for now

We need to mature more before we go deep into funding. First more PR


SBML qual
=========

We can remove some features to formalize the spec, and add them back later.

Multiple outputs?
-----------------

Needed for petri-nets
We can restrict cardinality to 1 for now, to leave the option of changing later.

Clarifications
--------------

* constant -> true for QS that can not ever change state. Can be used to fix initial state
* boundaryCondition -> in SBML core, this means: if the species occurs in a reaction you don’t have an ODE for it.
  But in SBML-qual, this meaning is interpreted similar as constant. Thus we don’t need it...
  true for QS that can not ever change state.


Summary of suggested changes to SBML-Qual
remove boundaryCondition ???
fix # of outputs to 1 for now..

Two ways of fixing the state of QS that have no regulators
either make it constant
create a transition with no inputs

Symbol vs level
---------------

Hidde De Jong, Gregory Batt are using this. Discuss if they are going to implement soonish.


TemporisationMath
-----------------

We decided to leave out temporisationMath and temporisationType as we don't have a clear use case for them now.



Outreach
========

Website
-------

SBML-qual already has a web page on sbml.org, but SBML-qual is just one part of the Colomoto project,
we agreed to make a setup a dedicated page for CoLoMoTo itself.

For now, we will get some space on the COMBINE wiki for a description of the project and the meeting pages.
Colomoto.org is still available and will be reserved by Julio and Martijn (EBI) and setup a redirection.


Conferences
-----------

* Combine - make sure we have a representative (Poster / Talk). 
* SBML-Qual automatically part of COMBINE
* Bring poster about SBML-Qual to COMBINE + ICSB Toronto (deadline 15 May). Who is going? Maybe Andreas/SarahK...
* ICSB 2013 in Kopenhagen
  Useful to exchange ideas on e.g. interaction on SED-ML

* Organize workshop and tutorial at .eg. ICSB/ ECCB/ ISMB:
  Probably ISMB/ECCB 2013 which will be in Europe, both workshop on science and tutorial on tools. Maybe in combination with publication in Education section of PloS biology


Publications
------------

* SBML-qual pub; there was App note in bioinformatics about SBML layout, maybe other journal more for modeling e.b. BMC SysBio or Mol Sys Bio (perhaps as letter. we can ask, first choice) or PLoS Comp. Biol (likely not, but Dennis will ask. Not standard-friendly acc. to Nicolas)

  - No need to request journals to publish models in SBML-qual, this is already part of requiring SBML. But needs PR -> write letter to editor...

* Colomoto later on needs more time and depends on Cytoscape 3. - Perhaps Nature (Biotech? or another sub-journal) (Ioannis Xenarios mentioned this in Lisbon)

* Paragraph about the Colomoto initiative


Social media
------------

Should we establish some presence on social media websites?

* A LinkedIn group was created: http://www.linkedin.com/groups/CoLoMoTo-4375380?home=&gid=4375380
* Twitter?
* Facebook / Google+:  do we care about these?


