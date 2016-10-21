#!/usr/bin/env python


import sys, numpy as np

def main():
	f = open(sys.argv[1], 'r')
	data = f.readlines()
	collect = False
	cindex = 0
	for i, line in enumerate(data):
		if not line.strip() and not collect:
			x, y, z = int(data[i+1].split()[0]), int(data[i+1].split()[1]), int(data[i+1].split()[2])
			good_data = data[i+2:]
			break
	distro = np.zeros(z)
	cindex = 0
	for line in good_data:
		if int(cindex / float(x * y)) == z:
			break
		for elem in line.split():
			distro[int(cindex / float(x * y))] += float(elem)
			cindex += 1
	for i, elem in enumerate(distro):
		print i * float(sys.argv[2]) / z, elem / z 
if __name__ == '__main__':
	main()
