"""Unit tests for mpl_orbref functions."""

import pytest

import xseof
import xseof.mpl_orbref as mod

from .utils import (
    INT_ATTREF,
    MPL_ORBREF as DATAFILES,
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
