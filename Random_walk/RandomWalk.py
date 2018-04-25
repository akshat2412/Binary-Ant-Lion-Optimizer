import numpy
import math



def transfer(ip_value):
		try:
			return 1/(1+math.exp(-10*ip_value))
		except:
			return 0

def stochasticThreshold(ip_value):
	if(ip_value>=numpy.random.uniform(0.0, 1.0)):
		return 0
	return 1


def randomWalk(dimensions, curr_iteration, max_iterations, antlion):
	# print(antlion)
	lb=numpy.ones((1, dimensions))
	ub=numpy.ones((1, dimensions))
	# print(lb)
	I=0.0
	# if curr_iteration<(max_iterations*0.1):
	# 	I=1
	# else:
	#     I=(1.0-max_iterations)/(curr_iteration-max_iterations)
	
	# print(curr_iteration/max_iterations)

	if curr_iteration>max_iterations/10:
	    I=1.0+100*(float(curr_iteration)/float(max_iterations))

	if curr_iteration>max_iterations/2:
	    I=1.0+1000*(float(curr_iteration)/float(max_iterations))
	

	if curr_iteration>max_iterations*(3/4):
	    I=1.0+10000*(float(curr_iteration)/float(max_iterations))
	

	if curr_iteration>max_iterations*(0.9):
	    I=1.0+100000*(float(curr_iteration)/float(max_iterations))
	

	if curr_iteration>max_iterations*(0.95):
	    I=1.0+1000000*(float(curr_iteration)/float(max_iterations))
	
	# print (I)

	lb=lb/I
	ub=ub/I
	# print(lb[0][0])
	# print(lb)
	if(numpy.random.uniform(0.0, 1.0)<0.5):
		lb=lb+antlion 
	else:
		lb=-lb+antlion

	if(numpy.random.uniform(0.0, 1.0)>=0.5):
		ub=ub+antlion 
	else:
		ub=-ub+antlion
	# print(antlion)
	# print(lb)
	RWs=numpy.empty([max_iterations, dimensions])
	# print(numpy.shape(RWs))
	for i in range(0, dimensions):
		X = numpy.array([numpy.cumsum(2*(numpy.random.uniform(0.0,1.0,(max_iterations,1))>0.5)-1)])
		# X=X.astype(float)
		a=(numpy.amin(X))
	# print(a)
		b=(numpy.amax(X))
	# print (b)
		c=lb[0][i]
		d=ub[0][i]
		# print (c)
		# print (d)
		# print (numpy.amin(X[0]))
		# print ((X-a))

		X_norm=(((X-a)*(d-c))/(b-a))+c
		RWs[:,i]=X_norm[0]
		
		sigmoid=numpy.vectorize(transfer)
		RWs=RWs-antlion
		RWs=sigmoid(RWs)

		threshold=numpy.vectorize(stochasticThreshold)
		RWs=threshold(RWs)

	# print(RWs)
	return RWs


# randomWalk(10, 798, 1000, numpy.random.randint(2, size=10))
