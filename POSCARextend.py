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

    old = [0,0,0]
    new = [0,0,0]

    for i in range(3):
        line = readin.readline() 
        old[i] = float(line.split()[i])
        line = [float(element)*n[i] for element in line.split()]
        readout.write(' '.join(map(str,line))+'\n')
        new[i] = line[i] #gets length in each direction, stored in length = [x,y,z]

    readout.write(readin.readline()) #elements
    line = [int(element)*n[0]*n[1]*n[2] for element in readin.readline().split()] #multiplies each type of atom by input amts
    readout.write(' '.join(map(str,line))+'\n') #write total # atoms

#just direct case for now, add for cartesian eventually
    readout.write(readin.readline())
    coords = readin.readlines()
    coords = [line.split()[0:3] for line in coords]
    cart = [[float(line[0])*old[0], float(line[1])*old[1], float(line[2])*old[2]] for line in coords] #puts data in cartesian

    data = list(cart)

    for line in cart:
        for z in range(n[2]):
            for y in range(n[1]):
                for x in range(n[0]):
                    data.append([line[0]+old[0]*(x+1), line[1]+old[1]*(y+1), line[2]+old[2]*(z+1)])

    for line in data:
        readout.write(' '.join(map(str,line))+'\n')
main()
