"""Tests for the xseof package."""

import io

import pytest

import xseof
import xseof.aux_orbdop
import xseof.aux_orbdor
import xseof.aux_orbres
import xseof.int_attref
import xseof.mpl_orbpre
import xseof.mpl_orbref

from .utils import (
    AUX_ORBRES,
    INT_ATTREF,
    get_header as _get_header,
)


all_modules = [
    xseof,
    xseof.aux_orbdop,
    xseof.aux_orbdor,
    xseof.aux_orbres,
    xseof.int_attref,
    xseof.mpl_orbpre,
    xseof.mpl_orbref,
]


# === High level functions ====================================================
@pytest.mark.parametrize("filename", AUX_ORBRES + INT_ATTREF)
def test_load_from_filename(filename):
    obj = xseof.load(str(filename))
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", AUX_ORBRES)
def test_load_from_path(filename):
    obj = xseof.load(filename)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", AUX_ORBRES)
def test_load_from_fd(filename):
    with open(filename, "rb") as fd:
        obj = xseof.load(fd)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", AUX_ORBRES)
def test_load_from_bytesio(filename):
    stream = io.BytesIO(filename.read_bytes())
    obj = xseof.load(stream)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", AUX_ORBRES + INT_ATTREF)
def test_load_from_xmldoc(filename):
    etree = pytest.importorskip("lxml.etree")
    xmldoc = etree.parse(filename)
    obj = xseof.load(xmldoc)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", AUX_ORBRES + INT_ATTREF)
def test_load_from_xmldoc_strict(filename):
    etree = pytest.importorskip("lxml.etree")
    xmldoc = etree.parse(filename)
    obj = xseof.load(xmldoc, strict=True)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", AUX_ORBRES + INT_ATTREF)
def test_from_string(filename):
    data = filename.read_text()
    obj = xseof.from_string(data)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", AUX_ORBRES)
def test_from_bytes(filename):
    data = filename.read_bytes()
    obj = xseof.from_string(data)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


# === invalid input ===========================================================
@pytest.mark.parametrize("module", all_modules)
def test_from_invalid_string(module):
    data = "dummy"
    with pytest.raises(xseof.ParserError):
        module.from_string(data)


@pytest.mark.parametrize("module", all_modules)
def test_from_invalid_string_type(module):
    data = 13
    with pytest.raises(ValueError):
        module.from_string(data)


@pytest.mark.parametrize("module", all_modules)
def test_from_invalid_xmldoc(module):
    etree = pytest.importorskip("lxml.etree")
    xmldoc = etree.fromstring("<dummy><a>empty</a></dummy>")
    with pytest.raises(xseof.ParserError):
        module.load(xmldoc)
