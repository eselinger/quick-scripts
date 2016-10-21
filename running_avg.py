#!/usr/bin/python

import sys
import numpy as np

def main():
    f = open(sys.argv[1],"r")
    infile = f.readlines()
    window = int(sys.argv[2]) #size of window, in data points

    data = []

    for line in infile:
        data.append([float(element) for element in line.split()])

    data = np.array(data).reshape((len(data),2))

    emax = data[len(data)-1][0]
    totE = 0
    totP = 0
    AVGS = []

    for j in range(len(data)-window):
        for i in range(window):
            totE = totE + data[j+i][1]
            totP = totP + data[j+i][0]
        AVGS.append([totP/window, totE/window])
        #print window, totE
        totE = 0
        totP = 0

    outfile = open("ravg" + str(window) + ".dat", "w")
    for line in AVGS:
            outfile.write(str(line[0]) + " " + str(line[1]) + "\n")
    
    outfile.close()

main()
