#!/bin/sh

set -e

TOOLSDIR=$(dirname $0)

sh ${TOOLSDIR}/generate-aux-orbdop.sh
sh ${TOOLSDIR}/generate-aux-orbdor.sh
sh ${TOOLSDIR}/generate-aux-orbres.sh
sh ${TOOLSDIR}/generate-int-attref.sh
sh ${TOOLSDIR}/generate-mpl-orbpre.sh
sh ${TOOLSDIR}/generate-mpl-orbref.sh
