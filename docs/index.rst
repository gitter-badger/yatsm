.. _index:

Yet Another Time Series Model (YATSM)
=====================================

About
-----

Yet Another Timeseries Model (YATSM) is a Python package for utilizing a
collection of timeseries algorithms and methods designed to monitor the land
surface using remotely sensed imagery. Algorithms within YATSM are coupled to
utilities for running, exploring, visualizing, and making maps of timeseries
analysis results. By making multiple approaches to timeseries analysis
available to users in one place, the YATSM package aims to make combining
methods from any one algorithm a simple task, thereby overcoming the weaknesses
in any singular approach.

For example, one might attempt to find land cover change using the YATSM
implementation of the Continuous Change Detection and Classification (CCDC)
(:cite:`Zhu2014152,Zhu201567`) algorithm. When looking at the changemaps
created using :ref:`yatsm changemap <yatsm_changemap>` command, some
ephemeral forest disturbances, like a particularly bad insect defoliation
event that only affects the reflectance in one year, might be present. In this
hypothetical case, the forest recovered the next year and CCDC fit two nearly
identical models before and after the defoliation event. To remove this
distinct, but ephemeral event, one might compare if fitting a break point and
creating two segments is statistically different than ignoring the ephemeral
change and fitting one model using a Chow Test :cite:`Chow1960`. With this
ephemeral change event removed, long term mean phenology metrics, including
the starting and ending of the growing season, of this forest can be fit for
timeseries segments using an implementation of Melaas *et al*, 2013
:cite:`Melaas2013`.


The Yet Another TimeSeries Model (YATSM) algorithm is designed to monitor land
surface phenomena, including land cover and land use change, using timeseries
of remote sensing observations. The algorithm seeks to find distinct time
periods within the timeseries, or time segments, by monitoring for disturbances.
These time segments may be used to infer continuous periods of stable land
cover, with breaks separating the segments representing ephemeral disturbances
or permanent conversions in land cover or land use.

The "Yet Another..." part of the algorithm name is an acknowledgement of the
influence a previously published timeseries algorithm - the Continuous Change
Detection and Classification (CCDC) :cite:`Zhu2014152` algorithm. While YATSM
began as an extension from CCDC, it was never intended as a 1 to 1 port of
CCDC and will continue to diverge in its own direction.

This algorithm is also influenced by other remote sensing algorithms which,
like CCDC, are based in theory on tests for structural change from econometrics
literature
:cite:`Chow1960,Andrews1993,Chu1996,Zeileis2005`.
These other remote sensing algorithms include
Break detection For Additive Season and Trend (BFAST) :cite:`Verbesselt201298`
and LandTrendr :cite:`Kennedy20102897`.
By combining ideas from CCDC, BFAST, and LandTrendr, this "Yet Another..."
algorithm hopes to overcome weaknesses present in any single approach.


User Guide
----------

To get started with YATSM, please follow this user guide:

.. toctree::
   :maxdepth: 2

   guide/install
   guide/dataset
   guide/exploration
   guide/model_specification
   guide/configuration
   guide/batch_interface
   guide/map_static
   guide/map_changes
   guide/classification
   guide/phenology


Command Line Interface Utilities
--------------------------------

The Command Line Interface (CLI) for YATSM is built using
`click <http://click.pocoo.org/>`_ and is accessed using the ``yatsm`` command.
Documentation about the CLI is available below:

.. toctree::
   :maxdepth: 2

   scripts/scripts

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

References
----------

.. bibliography:: static/index_refs.bib
   :style: unsrt
   :cited:
