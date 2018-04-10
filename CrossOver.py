import numpy

def crossover(curr_iteration,dimensions, RA, RE):
	co=numpy.empty([dimensions])

	for j in range(0, dimensions):
		if numpy.random.uniform(0.0, 1.0)>=0.5:
			co[j]=RE[curr_iteration-1][j]
		else:
			co[j]=RA[curr_iteration-1][j]

	# print(co)
	return co
	# if(rand_mat>0.5):
	# 	co=RA
	# else:
	# 	co=RE	