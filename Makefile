#!/usr/bin/make -f

PYTHON=python3
TARGET=xseof

.PHONY: default help dist check fullcheck coverage lint clean cleaner distclean update

default: help

help:
	@echo "Usage: make <TARGET>"
	@echo "Available targets:"
	@echo "  help      - print this help message"
	@echo "  dist      - generate the distribution packages (source and wheel)"
	@echo "  check     - run a full test (using pytest)"
	@echo "  fullcheck - run a full test (using tox)"
	@echo "  coverage  - run tests and generate the coverage report"
	@echo "  lint      - perform check with code linter (flake8, black)"
	@echo "  api       - update the API source files in the documentation"
	@echo "  docs      - generate the sphinx documentation"
	@echo "  clean     - clean build artifacts"
	@echo "  cleaner   - clean cache files and working directories of al tools"
	@echo "  distclean - clean all the generated files"

dist:
	$(PYTHON) -m build
	$(PYTHON) -m twine check dist/*.tar.gz dist/*.whl

check:
	$(PYTHON) -m pytest --doctest-modules

fullcheck:
	$(PYTHON) -m tox run

coverage:
	$(PYTHON) -m pytest --cov=$(TARGET) --cov-report=html --cov-report=term

lint:
	$(PYTHON) -m flake8 --count --statistics --select=E9,F63,F7,F82 --show-source $(TARGET) tests
	$(PYTHON) -m flake8 --count --statistics $(TARGET) tests tools
	# $(PYTHON) -m isort --check $(TARGET) tests
	$(PYTHON) -m black --check $(TARGET) tests
	# $(PYTHON) -m mypy --check-untyped-defs --ignore-missing-imports $(TARGET)
	# ruff check $(TARGET)

clean:
	$(RM) -r *.*-info build
	find . -name __pycache__ -type d -exec $(RM) -r {} +
	# $(RM) -r __pycache__ */__pycache__ */*/__pycache__ */*/*/__pycache__
	$(RM) $(TARGET)/*.c $(TARGET)/*.cpp $(TARGET)/*.so $(TARGET)/*.o
	if [ -f docs/Makefile ] ; then $(MAKE) -C docs clean; fi
	$(RM) -r docs/_build

cleaner: clean
	$(RM) -r .coverage htmlcov
	$(RM) -r .pytest_cache .tox
	$(RM) -r .mypy_cache .ruff_cache
	$(RM) -r .ipynb_checkpoints

distclean: cleaner
	$(RM) -r dist

update:
	$(RM) xseof/*/[!_]*.py
	sh tools/generate.sh