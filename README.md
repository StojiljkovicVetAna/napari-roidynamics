# napari-roidynamics

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

[![License BSD-3](https://img.shields.io/pypi/l/napari-roidynamics.svg?color=green)](https://github.com/StojiljkovicVetAna/napari-roidynamics/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-roidynamics.svg?color=green)](https://pypi.org/project/napari-roidynamics)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-roidynamics.svg?color=green)](https://python.org)
[![tests](https://github.com/StojiljkovicVetAna/napari-roidynamics/workflows/tests/badge.svg)](https://github.com/StojiljkovicVetAna/napari-roidynamics/actions)
[![codecov](https://codecov.io/gh/StojiljkovicVetAna/napari-roidynamics/branch/main/graph/badge.svg)](https://codecov.io/gh/StojiljkovicVetAna/napari-roidynamics)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-roidynamics)](https://napari-hub.org/plugins/napari-roidynamics)

Plugin to use the python package 'roidynamics' within napari.

The [roidynamics] package provides interesting tools to analyze the dynamics of intensity in time-lapse images split into regions of specific geometries.

Here we have wrapped the roidynamics functions into an easy-to-use napari plugin, which enables to interactively setup points of interest, which are used to generate masks of different geometries. In the current version you can select three different geometries:

<center><img src="https://raw.githubusercontent.com/StojiljkovicVetAna/napari-roidynamics/main/docs/images/napari-roidynamics_shapes.png" width="490" height="190"/></center>

We also allow to combine one of these three masks with any user-defined shape. This increases the flexibility of the plugin. However, if you wish to see a new shape please [file an issue]. 

These specific masks are then used to measure intensity on different channels of the time-lapse images. The intensity data can be viewed in napari or saved as plots and csv data along with the masks.

----------------------------------
## Installation

Install napari-roidynamics in a python environment where you have pre-installed the python viewer [napari]!

If you don't have a python environment yet, follow the example below, which uses a package manager called [mamba]. We suggest using Mamba because is faster, but a [conda] environment manager is a valid alternative. If you use conda, you will need to use the example below writing "conda" instead of "mamba" in the command line. <br> Alternatively, explore the different options illustrated on the [napari installation] website.<br>
If you are not familiar with this topics we suggest reading the [BiAPoL blog post] about mambaforge & python.

### First create a python environment containing napari
After installing [mamba], execute these three commands in your terminal(OS) or command prompt.

```
mamba create -y -n napari-roidynamics -c conda-forge python=3.9
mamba activate napari-roidynamics
mamba install -c conda-forge napari pyqt
```
In this example, with the first command you create a new environment called 'napari-roidynamics' (this is only an exemplar name, you can assign the name that you prefer to this new environment).<br> In the same first line of code you also install python 3.9 from conda-forge.<br> Then you activate the newly created environment and finally you install napari and pyqt from conda-forge in this environment.<br>
At this stage we suggest testing if the napari installation works, before proceeding with installing napari-roidynamics. To do so, after making sure that the newly created environment is actives, simply write napari in the terminal and execute it. A napari window should open.<br>

If you don't remember the name of your environment you can always use the command:

    mamba env list

### Install napari-roidynamics
In the new environment with napari correctly running, now you can install the napari-roidynamics plugin.
#### stable version from pip:

    pip install napari-roidynamics
#### latest development version from GitHub:

    pip install git+https://github.com/StojiljkovicVetAna/napari-roidynamics.git

### Use napari-roidynamics
If the installation was successful, you will be able to use napari-roidynamics from your new environment. Make sure that the environment is active and type napari in the terminal, the napari GUI should appear. From the GUI you should navigate to Plugins/Dynamics(napari-roidynamics) to open the plugin. <br/>
Detailed instructions for the plugin are provided in the [step-by-step guide].

## Authors

roidynamics has been created by Guillaume Witz, Microscopy Imaging Center and Data Science Lab, University of Bern in collaboration with Jakobus van Unen, Pertz lab, Institute of Cell Biology, University of Bern.

Ana Stojiljkovic & Guillaume Witz, Data Science Lab (DSL), University of Bern have developed the napari-roidynamics plugin.

## License

Distributed under the terms of the [BSD-3] license,
"napari-roidynamics" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://napari.org/stable/
[napari installation]: https://napari.org/stable/tutorials/fundamentals/installation.html

[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[file an issue]: https://github.com/StojiljkovicVetAna/napari-roidynamics/issues

[napari]: https://napari.org/stable/tutorials/fundamentals/installation.html
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/

[roidynamics]: https://github.com/guiwitz/roidynamics
[conda]: https://docs.conda.io/en/latest/miniconda.html
[mamba]: https://github.com/conda-forge/miniforge#mambaforge
[BiAPoL blog post]: https://biapol.github.io/blog/mara_lampert/getting_started_with_mambaforge_and_python/readme.html
[step-by-step guide]: https://stojiljkovicvetana.github.io/napari-roidynamics/docs/instructions.html