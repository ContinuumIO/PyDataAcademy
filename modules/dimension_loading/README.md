Dimension Loading and Slowly Changing Dimensions
================================================

Knowledge learned
-----------------

* how to load a dimension table from CSV file
* what are slowly changing dimensions
* how to handle the changes
* Type 1 change

Reusable utility functions
--------------------------

Here is a list of utility functions that you will create as excercise and you
might reuse in your code:

* `table_size(table)` - return number of rows in a table
* `dimension_file_reader(filename)` - read dimension file encoded as UTF-8
  from shared data source directory and yield dimension rows
* `load_dimension_table(table, filename, truncate)` - load data from
  `filename` into a `table`, delete all records in `table` if `truncate` is
  `True`
* `table_diff(left, right)` - provide row difference between tables
* `append_new()` - append new rows form one table to another
* `update_dimension()` - load data from a file into a dimension table through
  temporary table, apply *Type 1* change

Required knowledge 
------------------

* SQL basics

Software Requirements
---------------------

* sqlalchemy
