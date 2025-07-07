:orphan:

Installation
============

Here you can find instructions on how to install Mantid on various platforms.
We currently offer:

- :ref:`Conda packages <installation_conda>` for use with the
  `conda package manager <https://docs.conda.io/en/latest/>`__ (64-bit, Intel)
- :ref:`full installers <installation_full>` bundling
  all components (64-bit, Intel)

Please see the relevant sections for installation instructions and check our :doc:`troubleshooting page <condafaq>` if you run into difficulties.

.. _installation_conda:

Conda
-----

Our packages are available through our `mantid <https://anaconda.org/mantid>`__
channel on Anaconda.org. The available packages are:

- ``mantid``: Python library accessing algorithms and workspaces.

- ``mantidqt`` Python library providing custom Qt widgets such as
  instrument viewer, slice viewer for use in other applications.

- ``mantidworkbench``: General-purpose graphical-user-interface for plotting,
  writing scripts etc.

It is worth noting that versions of Mantid after v6.7 (including the nightly) use
Python 3.10. Mantid v6.7 and before use Python 3.8.

Latest Release
##############
It is recommended to use Mambaforge to create and manage a Conda environment for Mantid. Using mamba is preferable over conda as it's faster and better at resolving dependencies.

To install Mantid into a new Conda environment use these options:

- `-n` to specify the name of your new environment
- `-c` to add the 'mantid' Conda channel

These options should be followed by the name of the package you want
to install. This will probably be any library from the ``mantid`` python library

Installing using mambaforge
+++++++++++++++++++++++++++++++++++++++++++++++++++

To install mambaforge please follow `this documentation <https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html>`__

.. code-block:: sh

   mamba create -n mantid_env -c mantid mantid

or the ``mantidworkbench`` package containing the graphical-user-interface

.. code-block:: sh

   mamba create -n mantid_env -c mantid mantidworkbench

On macOS we provide both an Intel (x86) and Apple Silicon (ARM) package from
v6.13 onwards. Mamba will automatically determine  which package to install
based on your device.

Earlier versions of Mantid can still be installed on and used on Apple Silicon
devices using Rosetta. You will need to `have Rosetta installed
<https://support.apple.com/en-gb/102527>`__ and precede the setup commands with
``CONDA_SUBDIR=osx-64``. For example, if you want to install mantidworkbench,
use the following command:

.. code-block:: sh

	CONDA_SUBDIR=osx-64 mamba create -n mantid_env -c mantid mantidworkbench

Nightly Build
#############

.. include:: ./nightly_build_warning.txt

If you wish to use a nightly build then add the ``nightly`` label
to the channel:

.. code-block:: sh

  mamba create -n mantid_env -c mantid/label/nightly mantidworkbench

----

How to Open Mantid Workbench (Conda)
####################################

To open the Mantid Workbench provided in the ``mantidworkbench`` Conda package,
you must first activate your Conda environment:

.. code-block:: sh

  mamba activate mantid_env

Then you can open Mantid with the following command:

.. code-block:: sh

   workbench

----

.. _installation_full:

Full Installers
---------------

Latest Release
##############

.. raw:: html
   :file: latest.html

Instructions:

- :doc:`Windows <windows>`
- :doc:`macOS <macos>`
- :doc:`Linux <linux>`: Starting with version ``6.4`` the above `.tar.xz` file for Linux can
  simply be extracted and run on any modern Linux (>2010) system.
  Prior and up to versions ``6.4``, ``rpm`` and ``deb`` versions are available for
  Red Hat/CentOS 7 and various versions of Ubuntu: 18.04, 16.04, 14.04.

Nightly Build
#############

Go to our `releases page on Github <https://github.com/mantidproject/mantid/releases>`__,
find the latest nightly and download the relevant package.

.. include:: ./nightly_build_warning.txt

----

Sample Data
-----------

Below we provide links to various sets of sample data for use with Mantid:

- `Usage Examples <https://sourceforge.net/projects/mantid/files/Sample%20Data/UsageData.zip/download>`__:
  Data used within the usage sections of the mantid documentation pages

- `ISIS <https://sourceforge.net/projects/mantid/files/Sample%20Data/SampleData-ISIS.zip/download>`__:
  A sample of ISIS data files.

- `ORNL <https://sourceforge.net/projects/mantid/files/Sample%20Data/SampleData-ORNL.zip/download>`__:
  A sample of SNS & HFIR data files.

- `Muon <https://sourceforge.net/projects/mantid/files/Sample%20Data/SampleData-Muon.zip/download>`__:
  A sample of Muon files.

- `MLZ <https://sourceforge.net/projects/mantid/files/Sample%20Data/SampleData-MLZ.zip/download>`__:
  A sample of MLZ files.

- `Training Course Data <https://sourceforge.net/projects/mantid/files/Sample%20Data/TrainingCourseData.zip/download>`__:
  Data used for the `mantid training courses <https://docs.mantidproject.org/nightly/tutorials/index.html#training>`__.
