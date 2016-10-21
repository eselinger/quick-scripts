#!/usr/bin/python

import sys
import numpy as np

def main():
    f = open(sys.argv[1],"r")
    infile = f.readlines()
    intz = float(sys.argv[2]) #point of interface

    data = []

    for line in infile:
        data.append([float(element) for element in line.split()])

    data = np.array(data).reshape((len(data),2))

    water = 0
    Pt = 0
    countwater = 0
    countPt = 0

    for j in range(len(data)):
        if data[j][0] < intz:
            countPt += 1
            Pt = Pt + data[j][1]
        else:
            countwater += 1
            water = water + data[j][1]

    outfile = open("hartreeref.dat", "w")
    outfile.write(str(Pt/countPt) + " " + str(water/countwater))
    outfile.close()

main()
