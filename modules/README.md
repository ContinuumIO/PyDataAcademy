PyData Academy Modules
======================

This directory contains individual modules. Each module directory usualy
contains:

* ipython notebook
* python sources
* datasets in data/ subfolder

Module Development
------------------

Module directories should contain special medatada file and optional files
required for module development. The metadata is stored in `module.json`.
Other files/directories:

* `module.json` - module metadata (see below)
* `data` – module's datasets
* `preparation` - directory containing scripts that prepare datasets for the
  course, in case preparation is necessay. For example if a curated dataset
  needs to be treated for the purpose of module, split into multiple pieces,
  intetionaly degraded quality or introduce noise for further processing in the
  module.

the `module.json` file contains:

* `name` - module identifier
* `label` - human readable module name

* `category` - module category (1)
* `level` – module level: beginner, advanced, expert
* `required` – list of modules from which knowledge is required to sucessfully
  follow current module
* `recommended` – recommendations for further modules
* `authors` – list of module authors
* `required_packages` – list of python packages that are required for
  execution of module's content 


(1) – not stabilized yet
