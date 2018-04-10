from Initialize.Positions import initializePositions
from Random_walk.RandomWalk import randomWalk
import numpy
import RForest
import Generate_Dataset
import RWS
from CrossOver import crossover 
def bALO(N, Max_Iterations):
	(X, y)=Generate_Dataset.GenerateData1()
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
		for j in range(0, 44):
		# print(ant_position[0][i])
			if(antlion_position[i][j]==1):
				a.append(j)
	# print(a)
	# print(len(a))
		if len(a)==0:
			continue
		antlions_fitness[0, i]=(RForest.Random_Forest(a, X, y))

	# print(antlions_fitness)
	I = numpy.argsort(antlions_fitness)
	Sorted_antlions=antlion_position[I]
	Sorted_antlions=Sorted_antlions[0]
	sorted_antlion_fitness=numpy.sort(antlions_fitness)

	Elite_antlion_position=Sorted_antlions[0]
	Elite_antlion_fitness=sorted_antlion_fitness[0][0]
	# print(antlions_fitness)
	# print(sorted_antlion_fitness)
	# print(Elite_antlion_fitness)
	# print(Elite_antlion_position)

	curr_iteration=2
	# RouletteIndex=RWS.rouletteWheelSelection(1/sorted_antlion_fitness)
	# if RouletteIndex==-1:
	# 	RouletteIndex=0

	# RA=randomWalk(60, curr_iteration, 100, antlion_position[RouletteIndex])
	# RE=randomWalk(60, curr_iteration, 100, Elite_antlion_position)
	
	# crossover(N, RA, RE)

	while curr_iteration<=Max_Iterations:
		for i in range(0, N):
			RouletteIndex=RWS.rouletteWheelSelection(1/sorted_antlion_fitness)
			if RouletteIndex==-1:
				RouletteIndex=0

			RA=randomWalk(60, curr_iteration, Max_Iterations, antlion_position[RouletteIndex])
			RE=randomWalk(60, curr_iteration, Max_Iterations, Elite_antlion_position)
			# print(numpy.shape(RA))
			ant_position[i]=crossover(curr_iteration,60, RA, RE)
		# print(co)
		# ant_position=co
		# print(ant_position)
		for i in range(0, N):
			a=list()	
			for j in range(0, 60):
				if(ant_position[i][j]==1):
					a.append(j)

			if len(a)==0:
				continue
			ants_fitness[0, i]=(RForest.Random_Forest(a, X, y))

		# print("*****************************************************")
		double_population=numpy.append(Sorted_antlions, ant_position, axis=0)
		# print(Sorted_antlions)
		# print(ant_position)
		# print(double_population)
		# print(numpy.shape(double_population))
		double_fitness=numpy.append(sorted_antlion_fitness, ants_fitness)
		# print(double_fitness)
		double_fitness_sorted=numpy.sort(double_fitness)
		I = numpy.argsort(double_fitness)

		double_sorted_population=double_population[I]
		# numpy.sort(antlions_fitness)
		# print(double_sorted_population)
		# print("total fitnedouble_sorted_puss sorted")
		print(curr_iteration)
		# print(double_fitness_sorted)
		antlions_fitness=double_fitness_sorted[0:N]
		Sorted_antlions=double_sorted_population[0:N]
		print(Elite_antlion_fitness)
		# print(antlions_fitness[0])
		# print(Elite_antlion_position)
		if(antlions_fitness[0]<Elite_antlion_fitness):
			Elite_antlion_fitness=antlions_fitness[0]
			Elite_antlion_position=Sorted_antlions[0]
		# print(Elite_antlion_position)

		print(antlions_fitness[0])
		print(Elite_antlion_fitness)
		print(Elite_antlion_position)
		print("\n")

		Sorted_antlions[0]=Elite_antlion_position
		antlions_fitness[0]=Elite_antlion_fitness
		curr_iteration=curr_iteration+1
		# print(antlions_fitness)
		# print(type(Sorted_antlions[0][N-1]))
		# [sorted_antlion_fitness,sorted_indexes]=sort(antlions_fitness);
		# print(max_so_far)
		# index=RWS.rouletteWheelSelection(1/sorted_antlion_fitness)
	a=list()
	b=list()	
	for j in range(0, 60):
		if(Elite_antlion_position[j]==1):
			a.append(j)
		b.append(j)
	if len(a)==0:
		pass
	print("classification accuracy = ",RForest.Random_Forest(a, X, y, 1)*100, "for number of features = ", len(a))
	print("classification accuracy = ",RForest.Random_Forest(b, X, y, 1)*100, "for number of features = ", len(b))
bALO(20, 40)