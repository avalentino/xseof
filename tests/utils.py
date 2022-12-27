"""Common test utilities."""

import pathlib


DATADIR = pathlib.Path(__file__).parent / "data"

AUX_ORBDOP = tuple(DATADIR.glob("v0?xx/*_AUX_ORBDOP_*.*"))
AUX_ORBDOR = tuple(DATADIR.glob("v0?xx/*_AUX_ORBDOR_*.*"))
AUX_ORBRES = tuple(DATADIR.glob("v0?xx/*_AUX_ORBRES_*.*"))
INT_ATTREF = tuple(DATADIR.glob("v0?xx/*_INT_ATTREF_*.*"))
MPL_ORBPRE = tuple(DATADIR.glob("v0?xx/*_MPL_ORBPRE_*.*"))
MPL_ORBREF = tuple(DATADIR.glob("v0?xx/*_MPL_ORBREF_*.*"))
S1X_XXXORB = tuple(DATADIR.glob("s1x/*_AUX_???ORB_*.EOF"))


def get_header(obj):
    try:
        return obj.earth_observation_header
    except AttributeError:
        return obj.earth_explorer_header
