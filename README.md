# SDF_Redundancy_Eliminator

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/abeebyekeen/SDF_Redundancy_Eliminator?style=flat-square)](https://github.com/abeebyekeen/SDF_Redundancy_Eliminator/releases)
[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.7049711.svg?style=svg)](https://zenodo.org/record/7049711#.YxWvrHZBzi0)

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
> Option 1: [Install RDKit with Conda](https://www.rdkit.org/docs/Install.html#how-to-install-rdkit-with-conda) if you have conda installed

Create a python3 environment (tested with python versions 3.8 and 3.7)
```bash
conda create -n py38_rdkit python=3.8
```
Install RDkit with pip using
```bash
pip install rdkit
```
or
```bash
pip install rdkit-pypi
```

> Option 2: [Install RDKit from repositories](https://www.rdkit.org/docs/Install.html#installation-from-repositories)

[On Ubuntu, you may run](https://www.rdkit.org/docs/Install.html#ubuntu-12-04-and-later)

```bash
sudo apt-get install python3-rdkit librdkit1 rdkit-data
```
or run
```bash
pip3 install rdkit
```

> Option 3: [Build from Source](https://www.rdkit.org/docs/Install.html#building-from-source)

### On Windows
You may follow the instructions [here](https://www.rdkit.org/docs/Install.html#windows), or [here](https://www.rdkit.org/docs/Install.html#cross-platform-under-anaconda-python-fastest-install)

## How to Use SDF_Redundancy_Eliminator
1. Create a folder and copy in your *.SD/.SDF* compound library
2. Copy *RedundancyEliminator.py* into the same directory
3. Run the code and it will walk you through the steps:
```bash
python3 RedundancyEliminator.py
```


## Features
* Generates *canonical SMILES* for the compounds in the library if they are not annotated with *SMILES strings*
* Produces another copy of the library with *SMILES string* annotation
* Interactively walks the user through the steps

## Citation
If you use this code in your work, kindly cite it as:

**Yekeen, A. A. (2022). SDF_Redundancy_Eliminator: A python code to remove redundant ligands in a .SD/.SDF compound library. <em>https://github.com/abeebyekeen/SDF_Redundancy_Eliminator</em>, DOI: <em>https://doi.org/10.5281/zenodo.7049711</em>**
