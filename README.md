# SDF_Redundancy_Eliminator

**SDF_Redundancy_Eliminator** is a **Python3** code to: 
 1. Generate *canonical SMILES* for each of the compounds in an *.SD/.SDF* compound library, 
 2. Detect redundant ligands/structural isomers in the library,  
 3. Generate unique and redundant name lists and, optionally,  
 4. Move redundant ligands/structural isomers to a separate file to produce a library of unique compounds.


## Prerequisites/Dependencies

* Python3
* RDKit

## Installation of dependencies
* Conda
> Option 1: [Install RDKit with Conda](https://www.rdkit.org/docs/Install.html#how-to-install-rdkit-with-conda)
```bash
conda create -c conda-forge -n rdkit_env rdkit
```


## How to Use SDF_Redundancy_Eliminator
1. Create a folder and copy in your *.SD/.SDF* compound library
2. Copy *SDF_Redundancy_Eliminator.py* into the same directory
3. Run the code and it will walk you through the steps.


## Features
* Generates *canonical SMILES* for the compounds in the library if they are not annotated with *SMILES strings*
* Produces another copy of the library with *SMILES* string annotation
* Interactively walks the user through the steps