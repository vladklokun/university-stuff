import argparse
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def main(args):
	matplotlib.rcParams['font.family'] = 'serif'
	matplotlib.rcParams['font.serif'] = 'STIX Two Math, STIX Two Text'
	matplotlib.rc('mathtext', fontset='stix')
	
	x, y = np.loadtxt(args.input1, unpack=True)
	
	fig, ax = plt.subplots()
	
	ax.plot(x, y)
	
	ax.set_ylim(ymin=0)
	ax.set_xlim(xmin=0)
	
	ax
	
	ax.set(xlabel=r'$R_Н$ (Ом)')
	
	if (args.ylabel):
		ax.set(ylabel=args.ylabel)
		
	if (args.xlabel):
		ax.set(xlabel=args.xlabel)
	
	ax.grid()
	
	plt.tight_layout()
	
	plt.show()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	
	# Parse input files (required)
	parser.add_argument('--input1', '-i1', required=True)
	
	# Parse xlabel
	parser.add_argument('--ylabel', '-yl')
	
	# Parse ylabel
	parser.add_argument('--xlabel', '-xl')
	
	args = parser.parse_args()
	
	main(args)