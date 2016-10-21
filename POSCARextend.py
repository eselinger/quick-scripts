#!/usr/bin/python

import sys

def main():

    infile = str(sys.argv[1]) #input POSCAR file
    n = [int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])] #number to replicate in each dir

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
        readout.write(' '.join('{:f}'.format(element) for element in line) +'\n')
        new[i] = line[i] #gets length in each direction, stored in length = [x,y,z]

    readout.write(readin.readline()) #elements
    line = [int(element)*n[0]*n[1]*n[2] for element in readin.readline().split()] #multiplies each type of atom by input amts
    readout.write(' '.join(map(str,line))+'\n') #write total # atoms

    ctype = readin.readline()
    if "S" in str(ctype):
        readout.write(ctype)
        ctype = readin.readline()
    readout.write(ctype)
    coords = readin.readlines()
    coords = [line.split()[0:3] for line in coords]
    cart = [[float(line[0])*old[0], float(line[1])*old[1], float(line[2])*old[2]] for line in coords] #puts data in cartesian

    data = []

    for line in cart:
        for z in range(n[2]):
            for y in range(n[1]):
                for x in range(n[0]):
                    if "Direct" in ctype or "direct" in ctype:
                        data.append([(line[0]+old[0]*x)/new[0], (line[1]+old[1]*y)/new[1], (line[2]+old[2]*z)/new[2]])
                    else:
                        data.append([line[0]+old[0]*x, line[1]+old[1]*y, line[2]+old[2]*z])

    for line in data:
        readout.write(' '.join('{:f}'.format(element) for element in line) + '\n')
main()
