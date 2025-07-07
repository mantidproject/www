:orphan:

Conda Troubleshooting
=====================

Before using the troubleshooting below please ensure you are using Mambaforge. Using mamba is preferable over conda as it's faster and better at resolving dependencies.
To install mambaforge please follow `this documentation <https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html>`__

Issues
------

- :ref:`Unable to find mantid or mantidworkbench <unable_to_find>`
- :ref:`Installing on Apple silicon devices <osx_install>`
- :ref:`Unable to resolve dependencies <dependency_fail>`
- :ref:`404 error when trying to install <404_error>`

.. _unable_to_find:

Unable to find ``mantid`` or ``mantidworkbench``
############################################

.. code-block:: sh

	PackagesNotFoundError: The following packages are not available from current channels

If you encounter this error it may be because you have not included the mantid channel in your download command. Please ensure you include ``-c mantid`` when installing.

Example

.. code-block:: sh

   mamba create -n mantid_env -c mantid mantid

You may also encounter this error when trying to install on Apple silicon devices. See :ref:`Installing on Apple silicon devices <osx_install>` for help.

.. _osx_install:

Installing on Apple silicon devices
###################################

On macOS we provide both an Intel (x86) and Apple Silicon (ARM) package from
v6.13 onwards. Mamba will automatically determine  which package to install
based on your device.

The processor in your machine can be found by navigating to the ``Apple logo``
-> ``About This Mac``. On an Apple Silicon device, the ``Chip``
line will say ``Apple M`` then a number indicating the version of the chip on
the device. An Intel device will have a ``Processor`` line, followed by some
details of the specific CPU used in the device.

For versions of mantid prior to v6.13, only x86 packages are available. These
can still be used by those with Apple Silicon devices using Rosetta. You will
need to `have Rosetta installed <https://support.apple.com/en-gb/102527>`__ and
precede the mamba commands with ``CONDA_SUBDIR=osx-64``.

For example, if you want to install v6.12 of mantidworkbench, use the following
command:

.. code-block:: sh

	CONDA_SUBDIR=osx-64 mamba create -n mantid_env -c mantid mantidworkbench=6.12

.. _dependency_fail:

Unable to resolve dependencies
##############################

If you are having problems with dependencies we recommend installing Mantid into a new clean environment with no other packages. Please do not specify any dependency versions e.g. Python. All dependencies will be installed automatically with the version required to use Mantid.
Problems with resolving dependencies is often caused by installing other packages into the same environment that require different versions of the same dependency. You can view the direct dependencies of recent stable versions of mantid
available through conda-forge require by running the following command

.. code-block:: sh

	mamba search -c mantid mantid --info

To list the currrent depedencies being used in the nightly replace the channel name with ``mantid/label/nightly``.


.. _404_error:

404 error when trying to install
################################

Mantid's dependencies are all available through ``conda-forge``. To access this channel please check your ``.condarc`` file. It should contain the following

.. code-block:: sh

	channels:
		- conda-forge

or

.. code-block:: sh

	channels: [conda-forge]

If either of these are in the file then please make sure there are no other channels added for accessing Mantid. For example any of the following will cause a 404 error and should be removed from `.condarc`

.. code-block:: sh

	channels:
		- https://anaconda.org/mantid
		- mantid

Qt platform plugin error
########################

On Windows, if you are met with the following error upon launching ``workbench``

.. code-block:: sh

	qt.qpa.plugin: Could not find the Qt platform plugin "windows" in ""
	This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Deactivate your environment, reactivate it, and run ``workbench`` again.

Still having problems?
######################

If the above has not resolved your problem please post to our `community forum <https://forum.mantidproject.org>`_ or e-mail the team directly on ``mantid-help@mantidproject.org``.
