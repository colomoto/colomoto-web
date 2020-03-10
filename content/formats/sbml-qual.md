---
title: "SBML qual"
slug: sbml-qual
date: 2014/08/06 21:37:11
summary: Exchange format for logical models based on SBML
features: multivalued, documentation, layout#extension
formats: sbml-qual
---

[SBML qual](http://sbml.org/Documents/Specifications/SBML_Level_3/Packages/Qualitative_Models_%28qual%29)
is an extension of the [Systems Biology Markup Language (SBML)](http://sbml.org) Level 3 standard,
designed for the representation of multivalued qualitative models of biological networks.
The first SBML qual proposal in 2008 led to the creation of the CoLoMoTo consortium.
The extension was accepted by the SBML community in 2011, after consulting the wider
community and refining the original proposal through additional meetings with developers
of various related software tools.

The final specification was approved by the SBML Editors in the spring of 2013.



Warning
-------

When importing SBML qual files, most softwares recover the interaction network from the functions associated to the components.
Thus Transitions lacking a FunctionTerm element will be ignored.
Similarly, if the math elements describing the FunctionTerms are not consistent, the interaction is not considered.

In the case of the Path2Models non-metabolic models in BioModels database (http://www.ebi.ac.uk/biomodels-main/path2models),
while the structure of the network is described and annotated, transitions have no function associated.
Those files are scaffolds of logical models from KEGG signaling pathways (see [Path2Models publication](http://www.biomedcentral.com/1752-0509/7/116)).

These SBML files can be imported using the [Cytoscape plugin CytoCopter](http://www.cellnopt.org/cytocopter) and,
using [CellNOpt](http://www.cellnopt.org), train this scaffold network on data to get logical functions.



# Sample 


```xml
<?xml version='1.0' encoding='UTF-8' standalone='no'?>
<sbml xmlns="http://www.sbml.org/sbml/level3/version1/core" layout:required="false" level="3" qual:required="true" xmlns:layout="http://www.sbml.org/sbml/level3/version1/layout/version1" version="1" xmlns:qual="http://www.sbml.org/sbml/level3/version1/qual/version1">
  <model id="model_id">
  
    <layout:listOfLayouts xmlns:layout="http://www.sbml.org/sbml/level3/version1/layout/version1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <layout:layout>
        <layout:listOfSpeciesGlyphs>
          <layout:speciesGlyph layout:species="G0">
            <layout:boundingBox>
              <layout:position layout:x="297" layout:y="138"/>
              <layout:dimensions layout:height="25" layout:width="45"/>
            </layout:boundingBox>
          </layout:speciesGlyph>
          <layout:speciesGlyph layout:species="G1">
            <layout:boundingBox>
              <layout:position layout:x="250" layout:y="270"/>
              <layout:dimensions layout:height="25" layout:width="45"/>
            </layout:boundingBox>
          </layout:speciesGlyph>
          <layout:speciesGlyph layout:species="G2">
            <layout:boundingBox>
              <layout:position layout:x="439" layout:y="271"/>
              <layout:dimensions layout:height="25" layout:width="45"/>
            </layout:boundingBox>
          </layout:speciesGlyph>
        </layout:listOfSpeciesGlyphs>
      </layout:layout>
    </layout:listOfLayouts>
    
    <qual:listOfQualitativeSpecies xmlns:qual="http://www.sbml.org/sbml/level3/version1/qual/version1">
      <qual:qualitativeSpecies qual:maxLevel="1" qual:compartment="comp1" qual:constant="true" qual:id="G0"/>
      <qual:qualitativeSpecies qual:maxLevel="1" qual:compartment="comp1" qual:id="G1"/>
      <qual:qualitativeSpecies qual:maxLevel="1" qual:compartment="comp1" qual:id="G2"/>
    </qual:listOfQualitativeSpecies>
    
    <qual:listOfTransitions xmlns:qual="http://www.sbml.org/sbml/level3/version1/qual/version1">
      <qual:transition qual:id="tr_G1">
        <qual:listOfInputs>
          <qual:input qual:qualitativeSpecies="G0" qual:transitionEffect="none" qual:sign="positive" qual:id="tr_G1_in_0"/>
        </qual:listOfInputs>
        <qual:listOfOutputs>
          <qual:output qual:qualitativeSpecies="G1" qual:transitionEffect="assignmentLevel" qual:id="tr_G1_out"/>
        </qual:listOfOutputs>
        <qual:listOfFunctionTerms>
          <qual:defaultTerm qual:resultLevel="0">
          </qual:defaultTerm>
          <qual:functionTerm qual:resultLevel="1">
            <math xmlns="http://www.w3.org/1998/Math/MathML">            
              <apply>
                <eq/>
                <ci> G0 </ci>
                <cn type="integer"> 1 </cn>
              </apply>
            </math>
                    </qual:functionTerm>
        </qual:listOfFunctionTerms>
      </qual:transition>
      <qual:transition qual:id="tr_G2">
        <qual:listOfInputs>
          <qual:input qual:qualitativeSpecies="G0" qual:transitionEffect="none" qual:sign="negative" qual:id="tr_G2_in_0"/>
          <qual:input qual:qualitativeSpecies="G1" qual:transitionEffect="none" qual:sign="positive" qual:id="tr_G2_in_1"/>
        </qual:listOfInputs>
        <qual:listOfOutputs>
          <qual:output qual:qualitativeSpecies="G2" qual:transitionEffect="assignmentLevel" qual:id="tr_G2_out"/>
        </qual:listOfOutputs>
        <qual:listOfFunctionTerms>
          <qual:defaultTerm qual:resultLevel="0">
          </qual:defaultTerm>
          <qual:functionTerm qual:resultLevel="1">
            <math xmlns="http://www.w3.org/1998/Math/MathML">            
              <apply>
                <and/>
                <apply>
                  <eq/>
                  <ci> G0 </ci>
                  <cn type="integer"> 0 </cn>
                </apply>
                <apply>
                  <eq/>
                  <ci> G1 </ci>
                  <cn type="integer"> 1 </cn>
                </apply>
              </apply>
            </math>
          </qual:functionTerm>
        </qual:listOfFunctionTerms>
      </qual:transition>
    </qual:listOfTransitions>
    
    <listOfCompartments>
      <compartment constant="true" id="comp1"/>
    </listOfCompartments>
  
  </model>
</sbml>
```


