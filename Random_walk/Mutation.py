import math

def rate(curr_iteration, max_iterations):
	r=0.9+(-0.9*(curr_iteration-1))/(max_iterations-1);
	return r;