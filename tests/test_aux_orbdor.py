"""Unit tests for aux_orbdor functions."""

import pytest

import xseof
import xseof.aux_orbdor as mod

from .utils import (
    AUX_ORBDOR as DATAFILES,
    INT_ATTREF,
    get_header as _get_header,
)


@pytest.mark.parametrize("filename", DATAFILES)
def test_load(filename):
    obj = mod.load(filename)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", DATAFILES[:1])
def test_load_fd(filename):
    with open(filename) as fd:
        obj = mod.load(fd)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", DATAFILES[:1])
def test_load_xml(filename):
    etree = pytest.importorskip("lxml.etree")
    xmldoc = etree.parse(filename)
    obj = mod.load(xmldoc)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", INT_ATTREF[:1])
def test_load_invalid(filename):
    with pytest.raises(xseof.ParserError):
        mod.load(filename)


@pytest.mark.parametrize("filename", DATAFILES)
def test_from_string(filename):
    data = filename.read_text()
    obj = mod.from_string(data)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", DATAFILES)
def test_from_bytes(filename):
    data = filename.read_bytes()
    obj = mod.from_string(data)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem
