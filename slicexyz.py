#!/usr/bin/python

import sys


def main():

    infile = sys.argv[1]
    atoms = int(sys.argv[2]) #number of atoms to be stretched. MAKE SURE THESE ARE AT BOTTOM OF .xyz FILE

    readin = open(infile,'r')
    readout = open('cut01_'+infile, 'w')

    numat = int(readin.readline())
    readout.write(str(numat) + '\n')
    readout.write(readin.readline())

#read all coordinates into an array
    coordinates = readin.readlines()
    coordinates = [[element for element in line.split()] for line in coordinates[:]]

    readin.close()

#using only MMCT unit coordinates
    mmct = coordinates[numat-atoms:numat]
    a = range(atoms) 
 
    for i in xrange(atoms):
        a[i] = mmct[i][3]

#find highest coordinate
    maxz = float(max(a))
    print maxz

    b = range(4)
    newnumat = 0

    for i in xrange(numat): #only keep atoms with z-coordinate lower than maxz (from mmct)
        if float(coordinates[i][3]) <= maxz:
            for j in xrange(4):
                b[j] = coordinates[i][j]
            for element in b: readout.write(str(element) + '     ')
            readout.write('\n')
            newnumat = newnumat+1

    print newnumat

    readout.close()

main()
