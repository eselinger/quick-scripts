#!/usr/bin/python

import sys
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib.cm as cm

def main():

    infile = "LOCPOT" #input LOCPOT file from VASP output

    readin = open(infile,'r')
    readin.readline() #top two lines are comments
    readin.readline()

    length = [0,0,0]

    for i in range(3):
        line = readin.readline() 
        line = line.split()
        length[i] = float(line[i]) #gets length in each direction, stored in length = [x,y,z]

    readin.readline() #comment line

    line = readin.readline()
    line = line.split()
    numat = int(line[0]) + int(line[1]) + int(line[2]) #gets number of atoms in config

    for i in range(numat+2): #skipping over coordinates
        readin.readline()

    line = readin.readline()
    npts = [int(element) for element in line.split()] #gets npoints = [#x, #y, #z]

    xnum = npts[0]
    ynum = npts[1]
    znum = npts[2]

    xvec = length[0]/xnum
    yvec = length[1]/ynum
    zvec = length[2]/znum
    
    array = readin.readlines()
    readin.close()
    array = np.array([[float(element) for element in line.split()] for line in array[:]]) #taking pot data

#putting data in 1xN array
    pot = array.flatten()

#putting xy-planar avg'd pot data into Exz array
    pot_array = np.zeros(shape=(znum,2))
    n = 0

    for k in range(znum):
        pot_array[k][0] = float(k*zvec)
        for j in range (ynum):
            for i in range(xnum):
                pot_array[k][1] = pot_array[k][1] + pot[n]
                n = n+1

        pot_array[k][1] = pot_array[k][1]/(ynum*xnum)

# pot_array is now array of E(z)


    z = pot_array[:,0]
    E = pot_array[:,1]

    plt.plot(z,E)
    plt.xlabel('z(A)')
    plt.ylabel('<V>')


    plt.plot((17.21134205,17.3), (-40, 10), 'black') #extra line to show where interface is, coordinates are (x1,x2), (y1,y2)
    plt.plot((17.3668,17.4), (-40,10), 'red')

    plt.text(28,-5,'vacuum')
    plt.text(8,0,'Pt')

    plt.show()
main()
