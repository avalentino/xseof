Version history
===============

xseof v1.1.2 (UNRELEASED)
-------------------------

* Re-generate the source code with xsdata v24.4.
* Move package metadata to `pyproject.toml`.


xseof v1.1.1 (27/12/2022)
-------------------------

* Improve robustness in EOF files detection.
* Improve support for element-tree imputs.


xseof v1.1.0 (23/12/2022)
-------------------------

* Fix loading of Sentine-1 orbit form string.
* New `strict` option (default: `False`) to enforce strict XML namespaces
  checking in `xseof.load` and `xseof.from_string`.
* Improve docstrings to clarify that `lxml` is needed to use an `ElementTree`
  as source for the `xseof.load` and `xseof.*.load` functions.
  A dedicated unit test has been added also.
* Test coverage improved.


xseof v1.0.0 (20/11/2022)
-------------------------

* Initial release.
