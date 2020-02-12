# multiVitamin
In-Terminal multiple alignment tool for graphs

`multiVitamin` is a software package which allows users to perform multiple alignments with graphs.
There are three algorithms available for this task: The `Bron-Kerbosch` and the `VF2` algorithm and a custom subgraph-isomorphism-VF2 (called `subVF2`). Details
on the algorithms can be found in the theory section [here](multivitaminReadme.pdf). The main function of the package is to align
two or more graphs following a binary alignment guide tree containing the "best" alignment procedure.
The resulting multiple graph alignment is represented as one single graph itself. Next to this main
function, there is also the possibility to show all co-optimals of an alignment between 2 graphs or
to view graphical representations of graphs.
Sounds exciting, so let's get started!


## Installation instructions

Clone the repo from github with
```
git clone https://github.com/MaxJoas/graph_alignment.git
```
There are two possibilities to run `multiVitamin`.

#### pip3 install

Navigate to the directory containing the setup.py file
```
cd graph_alignment/multivitamin_project/multivitamin/
```
If you have **root permissions**, run
```
pip3 install -e .
```
and you're good to go.

If you **do not have root permissions**, run
```
pip3 install -e . --user
```
to install `multiVitamin` locally. Then put it into your PATH, so it can be run from everywhere within the system.
```
echo 'export PATH=$PATH:~/.local/bin/' >> ~/.bashrc
```
After this, you will need to either run `source ~/.bashrc` or open a new terminal window.

Done, now you can run multiVitamin in the command shell. You can test if the installation was successful by typing
```
multiVitamin -h
```

## How to use

#### Basics

You can get an overview of the basic flags and functionalities by typing
```
multiVitamin -h
```
A basic run example looks like the following
```
multiVitamin -a subVF2 -m graph1.graph graph2.graph graph3.graph
```
or simply
```
multiVitamin -m .
```
This will align all the .graph files (mind the extension!) in the current working directory.

Examples on what our custom graph file format looks like can be found in [graph_examples](graph_examples) inside the module.


## Further reading

More information on how to use the module can be found [here](multivitamin_paper/multivitaminReadme.pdf.pdf).
