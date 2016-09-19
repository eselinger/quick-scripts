#!/usr/bin/python

import sys
import numpy as np

def main():

    potential = "VEFFAVG.dx" #input dx file from paratec
    coordinates = "input" #input coordinates from paratec
    dx = open(potential,'r')
    infile = open(coordinates, 'r')

    readout = open("LOCPOT", 'w')
    readout.write("filename")
    readout.write("1.00000000")
    
    a = ""
    a = infile.readline()
    


    for i in range(100):
        if str(a) == "begin latticevecs":
            print a
        else: a = infile.readline()
    
    a = infile.readline()
    a = a.split()
    element = a[1]

"""    line1 = readin.readline() 
    line1 = line1.split()
    numpoints = int(line1[9]) #gets total number of points in grid (if needed)

    array = readin.readlines()
    readin.close()
    array = [[element for element in line.split()] for line in array[:]]

    xnum = int(array[-11][5])
    ynum = int(array[-11][6])
    znum = int(array[-11][7])

    xvec = float(array[-7][1])
    yvec = float(array[-8][2])
    zvec = float(array[-9][3])

    array = array[:(len(array)-17)] #taking only the data for plot

    pot = []

    #putting data in 1xN array

    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = float(array[i][j])
            pot.append(array[i][j])

    pot = np.array(pot) #1xN array

    pot_array = np.zeros(shape=(numpoints,4))
    n = 0

    for k in range(znum):
        for j in range (ynum):
            for i in range(xnum):
                pot_array[n][0] = float(i*xvec)
                pot_array[n][1] = float(j*yvec)
                pot_array[n][2] = float(k*zvec)
                pot_array[n][3] = pot[n]
                n = n+1
# pot_array is now array of x,y,z,pot explicitly


    x = pot_array[:,0]
    y = pot_array[:,1]
    z = pot_array[:,2]
    c = pot_array[:,3]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x,y,z,c=c, cmap=cm.Greys_r, edgecolors='none', alpha=0.1)

    plt.show()"""
main()
