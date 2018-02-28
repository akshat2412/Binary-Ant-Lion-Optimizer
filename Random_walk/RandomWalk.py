import numpy
import Mutation
import math



def transfer(ip_value):
	return 1/(1+math.exp(-10*ip_value))



def stochasticMutation(ip_value, curr_iteration, max_iterations):
	mutation_rate=Mutation.rate(curr_iteration, max_iterations)
	
	if(numpy.random.uniform(0.0, 1.0)>=mutation_rate):
		return ip_value
	return numpy.random.uniform(0.0, 1.0)


def stochasticThreshold(ip_value):
	if(ip_value>=numpy.random.uniform(0.0, 1.0)):
		return 1
	return 0


def randomWalk(dimensions, curr_iteration, max_iterations, antlion):
	# array=[1,0,1,1,1,0,0,0]
	# for x in array:
		# print (x)
	lb=numpy.ones((1, dimensions))
	ub=numpy.ones((1, dimensions))
	# print(lb)
	# a=list(stochasticMutation(x, curr_iteration, max_iterations) for x in array)
	# a=list(map(transfer, a))
	# a=list(map(stochasticThreshold, a)) 
	# print(a)
	I=0.0
	if curr_iteration<(max_iterations*0.1):
		I=1
	else:
	    I=(1.0-max_iterations)/(curr_iteration-max_iterations)
	
	print(I)

	lb=lb/I
	ub=ub/I
	print(lb[0][0])

	if(numpy.random.uniform(0.0, 1.0)<0.5):
		lb=lb+antlion 
	else:
		lb=-lb+antlion

	if(numpy.random.uniform(0.0, 1.0)>=0.5):
		lb=ub+antlion 
	else:
		lb=-ub+antlion
	# print(lb)
	# print(ub)
	RWs=numpy.empty([max_iterations, dimensions])
	# print(RWs)
	for i in range(0, dimensions):
		X = numpy.array([numpy.cumsum(2*(numpy.random.uniform(0.0,1.0,(max_iterations,1))>0.5)-1)])
		X=X.astype(float)
		# print(X)
	# print (X)
	# for x in X:
		a=(numpy.amin(X))
	# print(a)
		b=(numpy.amax(X))
	# print (b)
		c=lb[0][i]
		d=ub[0][i]
		print (c)
		print (d)
		# print (numpy.amin(X[0]))
		# print ((X-a))

		X_norm=(((X-a)*(d-c))/(b-a))+c
		RWs[:,i]=X_norm[0]
		# print(X_norm)
		# print(RWs)

	return RWs
		# print(X_norm)
		# for i in range(0, 100):
		# 	# print (i)
		# 	num=float(X[0][i])
		# 	# print(num)
		# 	X_norm=(((num-a)*(d-c))/(b-a))+c
		# 	Y_norm=(((num-ay)*(d-c))/(by-ay))+c
		# 	# X_norm=stochasticMutation(X_norm, curr_iteration, max_iterations)
		# 	X_norm=transfer(X_norm)
		# 	Y_norm=transfer(Y_norm)
			
		# 	X_norm=stochasticThreshold(X_norm)
		# 	Y_norm=stochasticThreshold(Y_norm)
		# 	# print(X_norm)
		# 	X[0][i]=X_norm
		# 	Y[0][i]=Y_norm
		# # print (len(X[0]))
		# # print(X)
		# # print(Y)
		# a_list = list()
		# for i in range(0, 100):
		# 	num_x=X[0][i]
		# 	num_y=Y[0][i]
		# 	if(numpy.random.uniform(0.0, 1.0)>=0.5):
		# 		a_list.append(num_x)
		# 	else:
		# 		a_list.append(num_y)
