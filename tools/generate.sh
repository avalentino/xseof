#!/bin/sh

set -e

xsdata generate -p xseof.aux_orbdop.v01xx EE_CFI_SCHEMAS/EO_OPER_AUX_ORBDOP_0105.XSD
xsdata generate -p xseof.aux_orbdop.v02xx EE_CFI_SCHEMAS/EO_OPER_AUX_ORBDOP_0203.XSD
xsdata generate -p xseof.aux_orbdop.v03xx EE_CFI_SCHEMAS/EO_OPER_AUX_ORBDOP_0300.XSD

xsdata generate -p xseof.aux_orbdor.v01xx EE_CFI_SCHEMAS/EO_OPER_AUX_ORBDOR_0105.XSD
xsdata generate -p xseof.aux_orbdor.v02xx EE_CFI_SCHEMAS/EO_OPER_AUX_ORBDOR_0203.XSD
xsdata generate -p xseof.aux_orbdor.v03xx EE_CFI_SCHEMAS/EO_OPER_AUX_ORBDOR_0300.XSD

xsdata generate -p xseof.aux_orbres.v01xx EE_CFI_SCHEMAS/EO_OPER_AUX_ORBRES_0105.XSD
xsdata generate -p xseof.aux_orbres.v02xx EE_CFI_SCHEMAS/EO_OPER_AUX_ORBRES_0203.XSD
xsdata generate -p xseof.aux_orbres.v03xx EE_CFI_SCHEMAS/EO_OPER_AUX_ORBRES_0300.XSD

xsdata generate -p xseof.int_attref.v01xx EE_CFI_SCHEMAS/EO_OPER_INT_ATTREF_0104.XSD
xsdata generate -p xseof.int_attref.v02xx EE_CFI_SCHEMAS/EO_OPER_INT_ATTREF_0204.XSD
xsdata generate -p xseof.int_attref.v03xx EE_CFI_SCHEMAS/EO_OPER_INT_ATTREF_0301.XSD

xsdata generate -p xseof.mpl_orbpre.v01xx EE_CFI_SCHEMAS/EO_OPER_MPL_ORBPRE_0105.XSD
xsdata generate -p xseof.mpl_orbpre.v02xx EE_CFI_SCHEMAS/EO_OPER_MPL_ORBPRE_0203.XSD
xsdata generate -p xseof.mpl_orbpre.v03xx EE_CFI_SCHEMAS/EO_OPER_MPL_ORBPRE_0300.XSD

xsdata generate -p xseof.mpl_orbref.v01xx EE_CFI_SCHEMAS/EO_OPER_MPL_ORBREF_0106.XSD
xsdata generate -p xseof.mpl_orbref.v02xx EE_CFI_SCHEMAS/EO_OPER_MPL_ORBREF_0203.XSD
xsdata generate -p xseof.mpl_orbref.v03xx EE_CFI_SCHEMAS/EO_OPER_MPL_ORBREF_0300.XSD
