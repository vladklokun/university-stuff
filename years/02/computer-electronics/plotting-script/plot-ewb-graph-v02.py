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
	
def get_trace_count(f):
	with open(f, 'r') as infile:
		trace_count = 0
		
		for line in infile:
			if 'End Trace: ' in line:
				trace_count += 1
				
	# Account for 1 extra trace (Trigger Line)
	return trace_count
	
def main(args):
	plots = []
	
	trace_count = get_trace_count(args.input)
	
	# Iterates from 1 to trace_count EXCLUSIVELY
	for i in range(1, trace_count):
		current_plot = build_nth_plot_coordinates(args.input, i)
		plots.append(current_plot)

	coordinates = []
	for plot in plots:
		x, y = gen_plotdata(plot)
		coordinates.append((x, y))
	
	layout = (trace_count-1) * 100 + 11
	for x, y in coordinates:
		plt.subplot(layout)
		plt.plot(x, y)
		layout += 1
		
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
	parser.add_argument('--t1', type=float)
	parser.add_argument('--t2', type=float)
	
	args = parser.parse_args()
	
	main(args)