#!/bin/bash

x=$(awk 'NR == 6 {print $4}' DOSCAR)
echo "EFERMI $x"
awk -v var="$x" '{ printf $1 " " "%.12g\n",($2 - var)}' z_LOCPOT.dat > hartree.dat
