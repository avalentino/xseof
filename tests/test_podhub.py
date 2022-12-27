"""Unit tests for non strict loading with orbits coming form podhub."""

import pytest

import xseof.aux_orbdop

from .utils import (
    S1X_XXXORB,
    get_header as _get_header,
)


@pytest.mark.parametrize("filename", S1X_XXXORB)
def test_load_s1_orb(filename):
    pytest.importorskip("lxml")
    obj = xseof.load(filename)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", S1X_XXXORB)
def test_load_s1_orb_strict(filename):
    pytest.importorskip("lxml")
    with pytest.raises(xseof.ParserError):
        xseof.load(filename, strict=True)


@pytest.mark.parametrize("filename", S1X_XXXORB)
def test_load_s1_orb_from_string(filename):
    pytest.importorskip("lxml")
    xml_string = filename.read_text()
    obj = xseof.from_string(xml_string)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", S1X_XXXORB)
def test_load_s1_orb_from_string_strict(filename):
    pytest.importorskip("lxml")
    xml_string = filename.read_text()
    with pytest.raises(xseof.ParserError):
        xseof.from_string(xml_string, strict=True)


@pytest.mark.parametrize("filename", S1X_XXXORB)
def test_load_s1_orb_from_bytes(filename):
    pytest.importorskip("lxml")
    xml_bytes = filename.read_bytes()
    obj = xseof.from_string(xml_bytes)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", S1X_XXXORB)
def test_load_s1_orb_from_bytes_strict(filename):
    pytest.importorskip("lxml")
    xml_bytes = filename.read_bytes()
    with pytest.raises(xseof.ParserError):
        xseof.from_string(xml_bytes, strict=True)


def test_load_s1_orb_from_invalid_bytes():
    pytest.importorskip("lxml")
    xml_bytes = "<dummy><dummytag>aaa</dummytag></dummy>"
    with pytest.raises(xseof.ParserError):
        xseof.from_string(xml_bytes)


@pytest.mark.parametrize("filename", S1X_XXXORB)
def test_load_s1_orb_from_xml(filename):
    lxml = pytest.importorskip("lxml")
    xmldoc = lxml.etree.parse(filename)
    xseof.load(xmldoc)


@pytest.mark.parametrize("filename", S1X_XXXORB)
def test_load_s1_orb_from_xml_strict(filename):
    lxml = pytest.importorskip("lxml")
    xmldoc = lxml.etree.parse(filename)
    with pytest.raises(xseof.ParserError):
        xseof.load(xmldoc, strict=True)
