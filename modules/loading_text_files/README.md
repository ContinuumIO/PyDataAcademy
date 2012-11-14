Loading Text Files into Numpy
=============================

To learn from this module, use ipython notebook::

    ipython notebook loading_text_files.ipynb

Data
====

External Sources
----------------

File: noaa-2012.op
Original name: 024530-99999-2012.op
Contents: Global Surface Summary of Day
Origin: ftp://ftp.ncdc.noaa.gov//pub/data/gsod/2012/024530-99999-2012.op.gz
Specification: ftp://ftp.ncdc.noaa.gov/pub/data/gsod/readme.txt
Info: http://www.ncdc.noaa.gov/cgi-bin/res40.pl?page=gsod.html
Organisation: National Climatic Datacenter of Natioanl Oceanic and Atmospheric Administration (NOAA)

Generated files
---------------

* numbers.csv: comma separated numerical values
* numbers.dat: numerical values separated by multiple spaces
* numbers_currency.dat: currency values with dollar sign
* numbers_localized.dat: localized numbers

Requirements
------------

* familiarity with numpy arrays and data types (dtype)

You will learn
--------------

* read csv
* delimiter
* fixed file
* converters

TODO: handle already opened file streams, such as URLs

