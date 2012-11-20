ETL Basics
==========

Objective of this tutorial is to learn basics of ETL and to prepare simple
star schema for aggregated browsing with Cubes. Data source is denormalized
table, originally stored in a CSV file.

All transformations and data preparation is being done purely in Python. SQL
library is used only for storing the data in a relational database. Note that
some cells might contain intentionally faulty code. Read following cells for
more information about the error.


Skills gained
-------------

* working with CSV file
* working with database schema (creation and deletion of tables)
* loading of data into a database
* data transformations
* normalization
* surroage keys (basics)
* how to make process reproducible and extensible
* how to maintain data provenance

Required knowledge
------------------

* relational database basics
* regular expression bacisc

Other requirements
------------------

* [sqlalchemy](http://www.sqlalchemy.org) - SQL/relational database framework

Utility functions
-----------------

This module provides following reusable utility functions:

* `distinct(rows, column)` - get distinct values of a column from list of rows
* `transform(row, transformation, index_map)` - transforms row according to transformation (see the module)

Data
----

* Source: [World Bank](https://finances.worldbank.org/Procurement/Major-Contract-Awards-FY2010-FY2012-Beta-version/kdui-wcs3)
* File name: `Major_Contract_Awards_FY2010_-_FY2012_-_Beta_version.csv`
* Date of download: 2012-10-11

