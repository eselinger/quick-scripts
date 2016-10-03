#!/usr/bin/python

import sys
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib.cm as cm

def main():

    infile = "POSCAR" #input POSCAR file
    n = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])] #number to replicate in each dir

    readin = open(infile,'r')
    readout = open("NEWPOSCAR",'w')
    readout.write(readin.readline()) #top two lines are comments)
    readout.write(readin.readline())

    length = [0,0,0]

    for i in range(3):
        line = readin.readline() 
        line = [float(element)*n[i] for element in line.split()]
        readout.write(' '.join(map(str,line))+'\n')
        length[i] = line[i] #gets length in each direction, stored in length = [x,y,z]

    readout.write(readin.readline()) #elements
    line = [int(element)*n[0]*n[1]*n[2] for element in readin.readline().split()] #multiplies each type of atom by input amts
    readout.write(' '.join(map(str,line)))

#just direct case for now, add for cartesian eventually
    readout.write(readin.readline())

    reading

main()
