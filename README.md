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
* [RDKit](https://www.rdkit.org/docs/Install.html)

 ### On Linux or OS X, there are multiple options:
> Option 1 (recommneded): [Install RDKit with Conda](https://www.rdkit.org/docs/Install.html#how-to-install-rdkit-with-conda) if you have conda installed

 ```bash
 conda create -c conda-forge -n rdkit_env rdkit
 ```

> Option 2 (recommended): [Install RDKit from repositories](https://www.rdkit.org/docs/Install.html#installation-from-repositories)

[On Ubuntu, you may run](https://www.rdkit.org/docs/Install.html#ubuntu-12-04-and-later)

 ```bash
sudo apt-get install python3-rdkit librdkit1 rdkit-data
```

> Option 3: [Build from Source](https://www.rdkit.org/docs/Install.html#building-from-source)

### On Windows
You may follow the instructions [here](https://www.rdkit.org/docs/Install.html#windows), or [here](https://www.rdkit.org/docs/Install.html#cross-platform-under-anaconda-python-fastest-install)

## How to Use SDF_Redundancy_Eliminator
1. Create a folder and copy in your *.SD/.SDF* compound library
2. Copy *SDF_Redundancy_Eliminator.py* into the same directory
3. Run the code and it will walk you through the steps.


## Features
* Generates *canonical SMILES* for the compounds in the library if they are not annotated with *SMILES strings*
* Produces another copy of the library with *SMILES string* annotation
* Interactively walks the user through the steps