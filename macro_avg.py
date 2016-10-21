#!/usr/bin/python

import sys
import numpy as np

def main():
    f = open(sys.argv[1],"r")
    infile = f.readlines()
    nb = int(sys.argv[2]) #number of blocks to split data into

    data = []

    for line in infile:
        data.append([float(element) for element in line.split()])

    data = np.array(data).reshape((len(data),2))

    emax = data[len(data)-1][0]
    totE = 0
    totP = 0
    count = 0
    AVGS = []

    for i in range(nb):
        for j in range(len(data)):
            if data[j][0] > (emax/nb)*i and data[j][0] < (emax/nb)*(i+1):
                count +=1
                totE = totE + data[j][1]
                totP = totP + data[j][0]
        AVGS.append([totP/count, totE/count])
        print count, totE
        count = 0
        totE = 0
        totP = 0

    outfile = open("avg" + str(nb) + ".dat", "w")
    for line in AVGS:
            outfile.write(str(line[0]) + " " + str(line[1]) + "\n")
    
    outfile.close()

main()
