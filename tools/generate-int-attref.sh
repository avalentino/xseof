#!/bin/sh

set -e

TOOLSDIR=$(dirname $0)

FTYPE=INT_ATTREF
PKG=xseof.int_attref
PKG_PATH=$(echo ${PKG} | sed 's:\.:/:g')


for VERSION in 0101 0102 0103 0104 0200 0201 0202 0203 0204 0300 0301
do    
    XSDROOT=EE_CFI_SCHEMAS/${FTYPE}_${VERSION}

    xsdata download -o ${XSDROOT} http://eop-cfi.esa.int/CFI/EE_CFI_SCHEMAS/EO_OPER_${FTYPE}_${VERSION}.XSD
    for f in ${XSDROOT}/*.XSD
    do
        if [ ! -f $(dirname $f)/$(basename $f .XSD).xsd ]
        then
            ln -s $(basename $f) $(dirname $f)/$(basename $f .XSD).xsd
        fi
    done
    xsdata generate -ss filenames -p ${PKG} ${XSDROOT}
done
python3 ${TOOLSDIR}/fix-names.py ${PKG_PATH}
python3 ${TOOLSDIR}/move-to-common.py ${PKG_PATH}
