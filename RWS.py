import numpy

def rouletteWheelSelection(Weights):
	accumulation=numpy.cumsum(Weights)
	p=numpy.random.uniform(0.0, 1.0)*accumulation[-1]
	# print(p)
	chosen_index = -1;
	# print(Weights)
	# print(accumulation)
	for index in range(0, len(accumulation)):
	    if (accumulation[index] > p):
	    	chosen_index = index
	      	break
	# print(chosen_index)
	return chosen_index
# rouletteWheelSelection()