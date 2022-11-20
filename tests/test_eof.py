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


@pytest.mark.parametrize("filename", AUX_ORBDOP)
def test_load_aux_orbdop(filename):
    obj = xseof.aux_orbdop.load(filename)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


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


@pytest.mark.parametrize("filename", AUX_ORBDOR)
def test_load_aux_orbdor(filename):
    obj = xseof.aux_orbdor.load(filename)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


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


@pytest.mark.parametrize("filename", AUX_ORBRES)
def test_load_aux_orbres(filename):
    obj = xseof.aux_orbres.load(filename)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


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


@pytest.mark.parametrize("filename", INT_ATTREF)
def test_load_int_attref(filename):
    obj = xseof.int_attref.load(filename)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


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


@pytest.mark.parametrize("filename", MPL_ORBPRE)
def test_load_mpl_orbpre(filename):
    obj = xseof.mpl_orbpre.load(filename)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


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


@pytest.mark.parametrize("filename", MPL_ORBREF)
def test_load_mpl_orbref(filename):
    obj = xseof.mpl_orbref.load(filename)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem


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


@pytest.mark.parametrize("filename", S1X_XXXORB)
def test_load_s1_orb(filename):
    pytest.importorskip("lxml")
    obj = xseof.load(filename)
    header = _get_header(obj)
    assert header.fixed_header.file_name == filename.stem
