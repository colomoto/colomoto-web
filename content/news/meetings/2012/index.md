---
title: "Second CoLoMoTo meeting (Hinxton, March 2012)"
date: 2012/04/01 21:37:11
summary: Setting up the consortium on the EBI campus
---


The second CoLoMoTo meeting took place on March 27-28 2012, at the [Wellcome trust conference centre, Hinxton UK](http://www.wtconference.org.uk).
It was organized by the [Systems Biomedicine group, EMBL-EBI](http://www.ebi.ac.uk/research/saez-rodriguez).


## Thurday, 18

Presentations by Colomoto members, focusing on getting to know each other, and progress update.

Time   | Who               |  Topic
------ | ----------------- | --------------------------------------------------------
13:00  |                   | Arrival, lunch
14:00  | J Saez-Rodriguez  | [CellNOpt, modelling prior knowledge networks trained to data](01_CellNOpt.pdf)
14:20  | C Chaouiya        | [GINsim, current status and future developments](02_GINsim.pdf)
14:40  | D Thieffry        | [Compression of state transitions graph for the analysis of cell fate decisions](03_HTG.pdf)
15:00  | A Dräger          | [Modeling the influence of nuclear receptors and statins on hepatocyte metabolism](04_NR_hepatocyte_model.pdf)
15:20  | T Helikar         | [The Cell Collective: Towards a more open, collaborative, and integrated systems biology](05_theCellCollective.pdf)
15:35  |                   | Coffee break
16:00  | S Klamt           | Qualitative modeling approaches for signaling and regulatory networks (CANCELED)
16:30  |                   | Brainstorm on governance, funding
18:00  |                   | End of meeting
19:30  |                   | Conference dinner in Cambridge


## Friday, 19

Developers presentations.

Time   | Who               |  Topic
------ | ----------------- | --------------------------------------------------------
09:00  | A Naldi           | [Colomoto toolbox](06_colomoto_toolbox.pdf)
09:30  | M van Iersel      | [SBML-qual validation workshop](07_sbml_qual.pdf)
10:00  | S Keating         | [SBML packaging workshop](08_sbml-L3-packages.pdf)
10:30  |                   |  Coffee break
11:00  | N Rodriguez       | [JSBML workshop](09_JSBML.pdf)
11:30  |                   |  Brainstorm on development process, validation and interoperability
12:30  |                   |  Lunch
13:30  |                   |  Brainstorm on future development


# Summary of discussions

## Objective of the CoLoMoTo project


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


### Mission/Purpose Statement


The Common Logical Modeling Toolbox (CoLoMoTo) consortium aims at integrating the scientific community utilizing logic-based modeling to study biological systems. The main goal of CoLoMoTo is to create a common ground in the form of software tools, methodologies, and models for research groups employing logical modeling. As an international effort, we strive to generate more visibility and adoption of this powerful computational approach.



### Project structure


Should we define a more formal structure (editors, scientific advisors)?
It seems too early for this, continue discussion with Nicolas Le Novère.


### Funding

* Funding for travel would be possible.
* Funding to hire a person seems out of scope for now

We need to mature more before we go deep into funding. First more PR


## SBML qual

We can remove some features to formalize the spec, and add them back later.

### Multiple outputs?


Needed for petri-nets
We can restrict cardinality to 1 for now, to leave the option of changing later.

### Clarifications

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

### Symbol vs level


Hidde De Jong, Gregory Batt are using this. Discuss if they are going to implement soonish.


### TemporisationMath


We decided to leave out temporisationMath and temporisationType as we don't have a clear use case for them now.



## Outreach


### Website


SBML-qual already has a web page on sbml.org, but SBML-qual is just one part of the Colomoto project,
we agreed to make a setup a dedicated page for CoLoMoTo itself.

For now, we will get some space on the COMBINE wiki for a description of the project and the meeting pages.
Colomoto.org is still available and will be reserved by Julio and Martijn (EBI) and setup a redirection.


### Conferences


* Combine - make sure we have a representative (Poster / Talk). 
* SBML-Qual automatically part of COMBINE
* Bring poster about SBML-Qual to COMBINE + ICSB Toronto (deadline 15 May). Who is going? Maybe Andreas/SarahK...
* ICSB 2013 in Kopenhagen
  Useful to exchange ideas on e.g. interaction on SED-ML

* Organize workshop and tutorial at .eg. ICSB/ ECCB/ ISMB:
  Probably ISMB/ECCB 2013 which will be in Europe, both workshop on science and tutorial on tools. Maybe in combination with publication in Education section of PloS biology


### Publications


* SBML-qual pub; there was App note in bioinformatics about SBML layout, maybe other journal more for modeling e.b. BMC SysBio or Mol Sys Bio (perhaps as letter. we can ask, first choice) or PLoS Comp. Biol (likely not, but Dennis will ask. Not standard-friendly acc. to Nicolas)

  - No need to request journals to publish models in SBML-qual, this is already part of requiring SBML. But needs PR -> write letter to editor...

* Colomoto later on needs more time and depends on Cytoscape 3. - Perhaps Nature (Biotech? or another sub-journal) (Ioannis Xenarios mentioned this in Lisbon)

* Paragraph about the Colomoto initiative


### Social media


Should we establish some presence on social media websites?

* A LinkedIn group was created: http://www.linkedin.com/groups/CoLoMoTo-4375380?home=&gid=4375380
* Twitter?
* Facebook / Google+:  do we care about these?


# Participants

* Julio Saez-Rodriguez, EMBL-EBI, Cambridge, UK
* Sarah Keating, EMBL-EBI, Cambridge, UK
* Nicolas Rodriguez, EMBL-EBI, Cambridge, UK
* Nicolas Le Novère, EBML-EBI, Cambridge, UK
* Martijn van Iersel, EMBL-EBI, Cambridge, UK
* Emanuel Gonçalves, EMBL-EBI, Cambridge, UK
* Thomas Cokelaer, EMBL-EBI, Cambridge, UK
* Claudine Chaouiya, Instituto Gulbenkian de Ciência, Portugal
* Aurelien Naldi, CIG-UNIL, Lausanne, Switzerland
* Tomas Helikar, University of Nebraska USA
* Andreas Dräger, University of Tübingen, Germany
* Denis Thieffry, IBENS, Paris, France


