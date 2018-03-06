from Initialize.Positions import initializePositions
from Random_walk.RandomWalk import randomWalk
import numpy
import RForest
import Generate_Dataset
def bALO(N, Max_Iterations):
	(X, y)=Generate_Dataset.GenerateData()
	# print(numpy.size(X, 0))
	Dim=numpy.size(X, 1)

	ant_position=initializePositions(N, Dim)
	antlion_position=initializePositions(N, Dim)

	Sorted_antlions=numpy.zeros((N,Dim))
	Elite_antlion_position=numpy.zeros((1,Dim))

	antlions_fitness=numpy.zeros((1,N))
	ants_fitness=numpy.zeros((1,N))

	# print (ant_position[0])
	# print (ant_position[0])
	# print(numpy.size(X, 1))
	# print(numpy.size(y))
	for i in range(0, N):
		a=list()	
		for j in range(0, 60):
		# print(ant_position[0][i])
			if(ant_position[i][j]==1):
				a.append(j)
	# print(a)
	# print(len(a))
		# if len(a)==0:
		print(RForest.Random_Forest(a, X, y)," for number of features = ",len(a))
		# 	continue
	# print(a)
bALO(50, 100)