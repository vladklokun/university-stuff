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
	matplotlib.rcParams['font.family'] = 'serif'
	matplotlib.rcParams['font.serif'] = 'STIX Two Math, STIX Two Text'
	matplotlib.rc('mathtext', fontset='stix')
	
	plot1 = build_nth_plot_coordinates(args.input, 1)
	plot2 = build_nth_plot_coordinates(args.input, 2)
	plot3 = build_nth_plot_coordinates(args.input, 3)
	plot4 = build_nth_plot_coordinates(args.input, 4)
	plot5 = build_nth_plot_coordinates(args.input, 5)
	
	x1, y1 = gen_plotdata(plot1) # Generate coordinates for the 1st plot
	x2, y2 = gen_plotdata(plot2) # Generate coordinates for the 2nd plot
	x3, y3 = gen_plotdata(plot3)
	x4, y4 = gen_plotdata(plot4)
	x5, y5 = gen_plotdata(plot5)
	
	plt.figure(1)
	
	# Input 1 voltage configuration
	plt.subplot(511)
	plt.plot(x1, y1)
	plt.xlabel('t')
	plt.ylabel(r'$J$')
	#plt.grid()
	plt.xlim(0)
	if (args.t1 and args.t2):
		plt.xlim(args.t1, args.t2)
	plt.ylim(0)
	ax1 = plt.gca()
	ax1.spines['top'].set_visible(False)
	ax1.spines['right'].set_visible(False)
	
	start, end = ax1.get_xlim()
	#ax1.set_xticks(np.arange(start, end, 64))
	ax1.get_xaxis().set_ticks([])
	ax1.get_yaxis().set_ticks([])
	#ax1.ticklabel_format(axis='x', style='sci', useOffset=False, scilimits=(-2,2))
	
	# Input 1 voltage configuration
	plt.subplot(512)
	plt.plot(x2, y2)
	plt.xlabel('t')
	plt.ylabel(r'$K$')
	#plt.grid()
	plt.xlim(0)
	if (args.t1 and args.t2):
		plt.xlim(args.t1, args.t2)
	plt.ylim(0)
	ax1 = plt.gca()
	ax1.spines['top'].set_visible(False)
	ax1.spines['right'].set_visible(False)
	ax1.get_xaxis().set_ticks([])
	ax1.get_yaxis().set_ticks([])
	#ax1.ticklabel_format(axis='x', style='sci', useOffset=False, scilimits=(-2,2))
	
	#Plot the output voltage
	plt.subplot(513)
	plt.plot(x3, y3)
	
	#Output voltage plot configuration
	plt.xlabel('t')
	plt.ylabel(r'$C$')
	#plt.grid()
	plt.xlim(0)
	plt.ylim(0)
	if (args.t1 and args.t2):
		plt.xlim(args.t1, args.t2)
	ax1 = plt.gca()
	ax1.spines['top'].set_visible(False)
	ax1.spines['right'].set_visible(False)
	ax1.get_xaxis().set_ticks([])
	ax1.get_yaxis().set_ticks([])
	#ax2.ticklabel_format(axis='x', style='sci', useOffset=False, scilimits=(-2,2))
	
	plt.subplot(514)
	plt.plot(x4, y4)
	
	#Output voltage plot configuration
	plt.xlabel('t')
	plt.ylabel(r'$Q$')
	#plt.grid()
	plt.xlim(0)
	if (args.t1 and args.t2):
		plt.xlim(args.t1, args.t2)
	ax1 = plt.gca()
	ax1.spines['top'].set_visible(False)
	ax1.spines['right'].set_visible(False)
	ax1.get_xaxis().set_ticks([])
	ax1.get_yaxis().set_ticks([])
	#ax2.ticklabel_format(axis='x', style='sci', useOffset=False, scilimits=(-2,2))
	
	# Out 5
	plt.subplot(515)
	plt.plot(x5, y5)
	
	plt.xlabel('t')
	plt.ylabel(r'$\overline{Q}$')
	
	plt.xlim(0)
	if(args.t1 and args.t2):
		plt.xlim(args.t1, args.t2)
	ax1 = plt.gca()
	ax1.spines['top'].set_visible(False)
	ax1.spines['right'].set_visible(False)
	ax1.get_xaxis().set_ticks([])
	ax1.get_yaxis().set_ticks([])
	
	plt.tight_layout()
	
	plt.show()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	
	# Parse file containing 2 input signals (required)
	parser.add_argument('--input', '-i', required = True)
	
	# Parse file containing 1 input and 1 output signals.
	# Only output signal is to be used.
	# parser.add_argument('--output','-o', required = True)
	
	#Parse time constraints (optional)
	parser.add_argument('--t1', type = float)
	parser.add_argument('--t2', type = float)
	
	args = parser.parse_args()
	
	main(args)