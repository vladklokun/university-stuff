#/usr/bin/env python3

import argparse
import matplotlib.pyplot as plt
import numpy as np

def main(args):
	plt.figure(1)
	plt.subplot(211)
	
	#Plot the input voltage
	x, y = np.loadtxt(args.vin.name, unpack=True)
	plt.plot(x, y)
	
	#Input voltage plot configuration
	plt.xlabel('t, (с)')
	plt.ylabel(r'$V_{ВХ}$, (В)')
	plt.grid()
	plt.xlim(args.t1, args.t2)
	ax1 = plt.gca()
	ax1.ticklabel_format(axis='x', style='sci', useOffset=False, scilimits=(-2,2))
	
	#Plot the output voltage
	plt.subplot(212)
	x, y = np.loadtxt(args.vout.name, unpack=True)
	plt.plot(x, y)
	
	#Output voltage plot configuration
	plt.xlabel('t, (с)')
	plt.ylabel(r'$V_{ВИХ}$, (В)')
	plt.grid()
	plt.xlim(args.t1, args.t2)
	ax2 = plt.gca()
	ax2.ticklabel_format(axis='x', style='sci', useOffset=False, scilimits=(-2,2))
	
	#Set proper layout
	plt.tight_layout()
		
	if args.outfile:
		plt.savefig(args.outfile.name)
	else:
		plt.show()
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	
	#Parse input files (required)
	parser.add_argument('--vin', type=argparse.FileType('r', encoding='UTF-8'), required=True)
	parser.add_argument('--vout', type=argparse.FileType('r', encoding='UTF-8'), required=True)
	
	#Parse output file (optional)
	parser.add_argument('--outfile','-o', type=argparse.FileType('w', encoding='UTF-8'))
	
	#Parse time constraints (optional)
	parser.add_argument('--t1', type=float, required=True)
	parser.add_argument('--t2', type=float, required=True)
	
	#Parse voltage constraints (optional, not implemented)
	parser.add_argument('--vinmin', type=float)
	parser.add_argument('--vinmax', type=float)
	
	args = parser.parse_args()
	main(args)
	