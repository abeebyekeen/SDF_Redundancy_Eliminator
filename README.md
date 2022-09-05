# SDF_Redundancy_Eliminator

**SDF_Redundancy_Eliminator** is a **Python** code to: 
 1. Generate *canonical SMILES* for each of the compounds in an *.SD/.SDF* compound library, 
 2. Detect redundant ligands/structural isomers in the library,  
 3. Generate unique and redundant name lists and, optionally,  
 4. Move redundant ligands/structural isomers to a separate file to produce a library of unique compounds.

## Prerequisite

* Python 2 or 3

## How to Use SDF_Redundancy_Eliminator
1. Create a folder and copy in your *.SD/.SDF* compound library
2. Copy into the same directory the *SDF_Redundancy_Eliminator.py* version appropriate for your python version
3. Run the code and it will walk you through the steps.

## Features
* Generates canonical SMILES if the compounds in your library are not annotated with SMILES strings
* Support both python 2 and 3 versions