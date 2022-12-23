"""Tests for the xseof package."""

import io
import pathlib

import pytest

import xseof
import xseof.aux_orbdop
import xseof.aux_orbdor
import xseof.aux_orbres
import xseof.int_attref
import xseof.mpl_orbpre
import xseof.mpl_orbref


DATADIR = pathlib.Path(__file__).parent / "data"

AUX_ORBDOP = tuple(DATADIR.glob("v0?xx/*_AUX_ORBDOP_*.*"))
AUX_ORBDOR = tuple(DATADIR.glob("v0?xx/*_AUX_ORBDOR_*.*"))
AUX_ORBRES = tuple(DATADIR.glob("v0?xx/*_AUX_ORBRES_*.*"))
INT_ATTREF = tuple(DATADIR.glob("v0?xx/*_INT_ATTREF_*.*"))
MPL_ORBPRE = tuple(DATADIR.glob("v0?xx/*_MPL_ORBPRE_*.*"))
MPL_ORBREF = tuple(DATADIR.glob("v0?xx/*_MPL_ORBREF_*.*"))
S1X_XXXORB = tuple(DATADIR.glob("s1x/*_AUX_???ORB_*.EOF"))


def _get_header(obj):
    try:
        return obj.earth_observation_header
    except AttributeError:
        return obj.earth_explorer_header


# === High level functions ====================================================
@pytest.mark.parametrize("filename", AUX_ORBRES)
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


@pytest.mark.parametrize("filename", AUX_ORBRES)
def test_load_from_xmldoc(filename):
    etree = pytest.importorskip("lxml.etree")
    xmldoc = etree.parse(filename)
    obj = xseof.load(xmldoc)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", AUX_ORBRES)
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


# === aux_orbdop functions ====================================================
@pytest.mark.parametrize("filename", AUX_ORBDOP)
def test_load_aux_orbdop(filename):
    obj = xseof.aux_orbdop.load(filename)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", AUX_ORBDOP[:1])
def test_load_fd_aux_orbdop(filename):
    with open(filename) as fd:
        obj = xseof.aux_orbdop.load(fd)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", INT_ATTREF[:1])
def test_load_invalid_aux_orbdop(filename):
    with pytest.raises(xseof.ParserError):
        xseof.aux_orbdop.load(filename)


@pytest.mark.parametrize("filename", AUX_ORBDOP)
def test_from_string_aux_orbdop(filename):
    data = filename.read_text()
    obj = xseof.aux_orbdop.from_string(data)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", AUX_ORBDOP)
def test_from_bytes_aux_orbdop(filename):
    data = filename.read_bytes()
    obj = xseof.aux_orbdop.from_string(data)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


# === aux_orbdor functions ====================================================
@pytest.mark.parametrize("filename", AUX_ORBDOR)
def test_load_aux_orbdor(filename):
    obj = xseof.aux_orbdor.load(filename)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", AUX_ORBDOR[:1])
def test_load_fd_aux_orbdor(filename):
    with open(filename) as fd:
        obj = xseof.aux_orbdor.load(fd)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", INT_ATTREF[:1])
def test_load_invalid_aux_orbdor(filename):
    with pytest.raises(xseof.ParserError):
        xseof.aux_orbdor.load(filename)


@pytest.mark.parametrize("filename", AUX_ORBDOR)
def test_from_string_aux_orbdor(filename):
    data = filename.read_text()
    obj = xseof.aux_orbdor.from_string(data)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", AUX_ORBDOR)
def test_from_bytes_aux_orbdor(filename):
    data = filename.read_bytes()
    obj = xseof.aux_orbdor.from_string(data)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


# === aux_orbres functions ====================================================
@pytest.mark.parametrize("filename", AUX_ORBRES)
def test_load_aux_orbres(filename):
    obj = xseof.aux_orbres.load(filename)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", AUX_ORBRES[:1])
def test_load_fd_aux_orbres(filename):
    with open(filename) as fd:
        obj = xseof.aux_orbres.load(fd)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", INT_ATTREF[:1])
def test_load_invalid_aux_orbres(filename):
    with pytest.raises(xseof.ParserError):
        xseof.aux_orbres.load(filename)


@pytest.mark.parametrize("filename", AUX_ORBRES)
def test_from_string_aux_orbres(filename):
    data = filename.read_text()
    obj = xseof.aux_orbres.from_string(data)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", AUX_ORBRES)
def test_from_bytes_aux_orbres(filename):
    data = filename.read_bytes()
    obj = xseof.aux_orbres.from_string(data)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


# === int_attref functions ====================================================
@pytest.mark.parametrize("filename", INT_ATTREF)
def test_load_int_attref(filename):
    obj = xseof.int_attref.load(filename)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", INT_ATTREF[:1])
def test_load_fd_int_attref(filename):
    with open(filename) as fd:
        obj = xseof.int_attref.load(fd)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", AUX_ORBDOP[:1])
def test_load_invalid_int_attref(filename):
    with pytest.raises(xseof.ParserError):
        xseof.int_attref.load(filename)


@pytest.mark.parametrize("filename", INT_ATTREF)
def test_from_string_int_attref(filename):
    data = filename.read_text()
    obj = xseof.int_attref.from_string(data)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", INT_ATTREF)
def test_from_bytes_int_attref(filename):
    data = filename.read_bytes()
    obj = xseof.int_attref.from_string(data)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


# === mpl_orbpre functions ====================================================
@pytest.mark.parametrize("filename", MPL_ORBPRE)
def test_load_mpl_orbpre(filename):
    obj = xseof.mpl_orbpre.load(filename)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", MPL_ORBPRE[:1])
def test_load_fd_mpl_orbpre(filename):
    with open(filename) as fd:
        obj = xseof.mpl_orbpre.load(fd)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", INT_ATTREF[:1])
def test_load_invalid_mpl_orbpre(filename):
    with pytest.raises(xseof.ParserError):
        xseof.mpl_orbpre.load(filename)


@pytest.mark.parametrize("filename", MPL_ORBPRE)
def test_from_string_mpl_orbpre(filename):
    data = filename.read_text()
    obj = xseof.mpl_orbpre.from_string(data)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", MPL_ORBPRE)
def test_from_bytes_mpl_orbpre(filename):
    data = filename.read_bytes()
    obj = xseof.mpl_orbpre.from_string(data)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


# === mpl_orbref functions ====================================================
@pytest.mark.parametrize("filename", MPL_ORBREF)
def test_load_mpl_orbref(filename):
    obj = xseof.mpl_orbref.load(filename)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", MPL_ORBREF[:1])
def test_load_fd_mpl_orbref(filename):
    with open(filename) as fd:
        obj = xseof.mpl_orbref.load(fd)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", INT_ATTREF[:1])
def test_load_invalid_mpl_orbref(filename):
    with pytest.raises(xseof.ParserError):
        xseof.mpl_orbref.load(filename)


@pytest.mark.parametrize("filename", MPL_ORBREF)
def test_from_string_mpl_orbref(filename):
    data = filename.read_text()
    obj = xseof.mpl_orbref.from_string(data)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


@pytest.mark.parametrize("filename", MPL_ORBREF)
def test_from_bytes_mpl_orbref(filename):
    data = filename.read_bytes()
    obj = xseof.mpl_orbref.from_string(data)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


# === strict parameter ========================================================
@pytest.mark.parametrize("module", [
    xseof,
    xseof.aux_orbdop,
    xseof.aux_orbdor,
    xseof.aux_orbres,
    xseof.int_attref,
    xseof.mpl_orbpre,
    xseof.mpl_orbref,
])
def test_from_invalid_string(module):
    data = "dummy"
    with pytest.raises(xseof.ParserError):
        module.from_string(data)


# === no-strict parsing =======================================================
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
