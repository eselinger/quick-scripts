#!/bin/python

import sys

def main():
    f = open(sys.argv[1], "r") #name of input file in xyz
    types = sys.argv[2] #number of atom types
 
    outfile = open("comb.xyz", "w")
    outfile.write(str(f.readline()))
    outfile.write(str(f.readline()))

    infile = f.readlines()

    array_1 = []
    array_2 = []

    for line in infile:
        coord = [str(element) for element in line.split()]
        if str(coord[0]) == "H":
            array_1.append(coord)
        elif str(coord[0]) == "O":
            array_2.append(coord)

    for line in array_1:
        for element in line:
            outfile.write(str(element) + "  ")
        outfile.write("\n")
    for line in array_2:
        for element in line:
           outfile.write(str(element) + "  ")
        outfile.write("\n")
  
    outfile.close()

main()
