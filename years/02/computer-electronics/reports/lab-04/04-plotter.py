import argparse
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import re

def gen_plotdata(coordlist):
	x, y = zip(*(s.split('\t') for s in coordlist))
	
	return x, y
	
def build_nth_plot_coordinates(f, n):
	with open(f, 'r') as i:
		plot = []
		
		for line in i:
			if 'Trace: %d' % n in line:
				break
				
		for line in i:
			if re.search(r'^[0-9]', line): # match only numbers, since time is always > 0
				plot.append(line.strip())
				
			if 'End Trace: ' in line:
				break
				
	return plot
	
def main(args):
	plot1 = build_nth_plot_coordinates(args.input, 1)
	plot2 = build_nth_plot_coordinates(args.input, 2)
	plot3 = build_nth_plot_coordinates(args.output, 2)
	
	matplotlib.rcParams['font.family'] = 'serif'
	matplotlib.rcParams['font.serif'] = 'STIX Two Math, STIX Two Text'
	matplotlib.rc('mathtext', fontset='stix')
	
	x1, y1 = gen_plotdata(plot1) # Generate coordinates for the 1st plot
	x2, y2 = gen_plotdata(plot2) # Generate coordinates for the 2nd plot
	x3, y3 = gen_plotdata(plot3)
	
	plt.figure(1)
	
	# Input 1 voltage configuration
	plt.subplot(311)
	plt.plot(x1, y1)
	plt.xlabel('t, (с)')
	plt.ylabel(r'$U_{1ВХ}$, (В)')
	plt.grid()
	plt.xlim(args.t1, args.t2)
	ax1 = plt.gca()
	#ax1.ticklabel_format(axis='x', style='sci', useOffset=False, scilimits=(-2,2))
	
	# Input 1 voltage configuration
	plt.subplot(312)
	plt.plot(x2, y2)
	plt.xlabel('t, (с)')
	plt.ylabel(r'$U_{2ВХ}$, (В)')
	plt.grid()
	plt.xlim(args.t1, args.t2)
	ax1 = plt.gca()
	#ax1.ticklabel_format(axis='x', style='sci', useOffset=False, scilimits=(-2,2))
	
	#Plot the output voltage
	plt.subplot(313)
	plt.plot(x3, y3)
	
	#Output voltage plot configuration
	plt.xlabel('t, (с)')
	plt.ylabel(r'$U_{ВИХ}$, (В)')
	plt.grid()
	plt.xlim(args.t1, args.t2)
	ax2 = plt.gca()
	#ax2.ticklabel_format(axis='x', style='sci', useOffset=False, scilimits=(-2,2))
	
	plt.tight_layout()
	
	plt.show()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	
	# Parse file containing 2 input signals (required)
	parser.add_argument('--input', '-i', required = True)
	
	# Parse file containing 1 input and 1 output signals.
	# Only output signal is to be used.
	parser.add_argument('--output','-o', required = True)
	
	#Parse time constraints (optional)
	parser.add_argument('--t1', type=float, required = True)
	parser.add_argument('--t2', type=float, required = True)
	
	args = parser.parse_args()
	
	main(args)