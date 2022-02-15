.. title:: Mantid Project

.. raw:: html
   :file: index_top_images.html

.. toctree::
   :hidden:

   privacy

The Mantid project provides tools to support the processing of materials-science
data. This data can be gathered from Neutron scattering or Muon spectroscopy
experiments or as the result of simulation. The project provides:

- a Python library, ``mantid``, providing custom high-performance algorithms and
  data structures for processing compatible data

- a general-purpose graphical user interface, ``MantidWorkench``, for
  visualisation of raw or processed data including

  - `matplotlib <https://matplotlib.org>`__-based plotting

  - script editor allowing immediate script execution

  - an instrument viewer displaying both 3D and unwrapped views of instruments

  - a slice viewer for slicing through higher-dimensional data

- custom graphical user interfaces for a variety of scientific techniques to
  reduce the burden on users understanding how to process their data

The tools are:

- `open source <https://github.com/mantidproject/mantid>`__

- 64-bit, cross platform: Linux, Windows, macOS

- built using `many other open source projects <https://github.com/mantidproject/mantid/blob/main/DEPENDENCY_LICENSES.md>`__.

Getting Started
===============

You can get started by first visiting the `download page <download>`__ where you
will find links to various methods of installation. Once installed checkout our
`user documentation <https://docs.mantidproject.org>`__ for tutorials,
algorithm documentation and more.

Development
===========

The Mantid source is hosted on `GitHub <https://github.com/mantidproject/mantid>`__.
There are pages on `getting started with development <https://developer.mantidproject.org/GettingStarted.html>`__,
`issue tracking <https://developer.mantidproject.org/IssueTracking.html>`__,
and more on the development process, tools, testing, etc. on our
`developer documentation <https://developer.mantidproject.org/>`__.

Governance
==========

Mantid is an open-source project with `many contributors <https://github.com/mantidproject/mantid/graphs/contributors>`__.
The project is governed by a steering committee separated into 2 working groups:
the `Scientific Working Group <https://github.com/mantidproject/governance/tree/main/scientific-working-group>`__ &
the `Technical Working Group <https://github.com/mantidproject/governance/tree/main/technical-working-group>`__.
Each group formulates a roadmap for future developments from either a scientific
or technical perspective.
For full details of the governance model please see
`the governance document <https://github.com/mantidproject/governance/blob/main/governance.md#revised-governance-structure-2021---present>`__.


Citing Mantid
=============

If Mantid contributes to a project that leads to a scientific publication,
please acknowledge this work by citing:

- *Mantid (2013): Manipulation and Analysis Toolkit for Instrument Data.; Mantid Project.* http://dx.doi.org/10.5286/SOFTWARE/MANTID

- Arnold, O. et al. *Mantid-Data Analysis and Visualization Package for Neutron Scattering and mu-SR Experiments.* Nuclear Instruments
  and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment 764 (2014): 156-166
  `doi: 10.1016/j.nima.2014.07.029 <https://doi.org/10.1016/j.nima.2014.07.029>`__
  (`download bibtex <https://raw.githubusercontent.com/mantidproject/mantid/main/docs/source/mantid.bib>`__)

To cite a specific release then please find the relevant DOI citation under the
release notes for that `particular version <https://docs.mantidproject.org/release/>`__.

Privacy Policy
==============

Tools provided by the project are able to send both anonymised and identifiable
data to help the project in terms of tracking feature usage and collecting error
information.
Please see our :ref:`privacy policy <privacy_policy>` for more detail on how
this data is stored and used.
