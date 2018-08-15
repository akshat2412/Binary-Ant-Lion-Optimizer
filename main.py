from Initialize.Positions import initializePositions
from Random_walk.RandomWalk import randomWalk
import numpy
import RForest_new
import Generate_Dataset
import RWS
from CrossOver import crossover 

def bALO(N, Max_Iterations):
	print("Number of Antlions : " + str(N))
	print("Number of Iterations : " + str(Max_Iterations))

	(X, y)=Generate_Dataset.GenerateData1()
	Dim=numpy.size(X, 1)
	# print(Dim)
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
		for j in range(0, Dim):
		# print(ant_position[0][i])
			if(antlion_position[i][j]==1):
				a.append(j)
	# print(a)
	# print(len(a))
		if len(a)==0:
			continue
		antlions_fitness[0, i]=(RForest_new.Random_Forest(a, X, y, Dim))

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
		print("-------------------------------------------------------")
		print("\nIteration Number : " + str(curr_iteration))
		for i in range(0, N):
			RouletteIndex=RWS.rouletteWheelSelection(1/sorted_antlion_fitness)
			if RouletteIndex==-1:
				RouletteIndex=0

			RA=randomWalk(Dim, curr_iteration, Max_Iterations, antlion_position[RouletteIndex])
			RE=randomWalk(Dim, curr_iteration, Max_Iterations, Elite_antlion_position)
			# print(numpy.shape(RA))
			ant_position[i]=crossover(curr_iteration,Dim, RA, RE)
			# print(ant_position[i])
			# print(Elite_antlion_position)
			# print(antlion_position[RouletteIndex])
			# print("\n\n")
		# print(co)
		# ant_position=co
		# print(ant_position)
		for i in range(0, N):
			a=list()	
			for j in range(0, Dim):
				if(ant_position[i][j]==1):
					a.append(j)

			if len(a)==0:
				continue
			ants_fitness[0, i]=(RForest_new.Random_Forest(a, X, y, Dim))

		# print("*****************************************************")
		double_population=numpy.append(Sorted_antlions, ant_position, axis=0)
		# print(Sorted_antlions)
		# print(ant_position)
		# print(double_population)
		# print(numpy.shape(double_population))
		double_fitness=numpy.append(sorted_antlion_fitness, ants_fitness)
		# print(sorted_antlion_fitness)
		# print(ants_fitness)
		# print(double_fitness)
		double_fitness_sorted=numpy.sort(double_fitness)
		I = numpy.argsort(double_fitness)

		double_sorted_population=double_population[I]
		# numpy.sort(antlions_fitness)
		# print(double_fitness_sorted)
		# print("total fitnedouble_sorted_puss sorted")
		print("\nFitnesses of Antlions in current Iteration\n")
		print(double_fitness_sorted)
		print("")
		antlions_fitness=double_fitness_sorted[0:N]
		Sorted_antlions=double_sorted_population[0:N]
		print("\nElite Antlion Fitness   :   " + str(Elite_antlion_fitness))
		# print(antlions_fitness[0])
		# print(Elite_antlion_position)
		if(antlions_fitness[0]<Elite_antlion_fitness):
			Elite_antlion_fitness=antlions_fitness[0]
			Elite_antlion_position=Sorted_antlions[0]
		# print(Elite_antlion_position)

		print("\nCurrent Elite Antlion Fitness   :   " + str(antlions_fitness[0]))
		print("\nUpdated Elite Antlion Fitness   :   " + str(Elite_antlion_fitness))
		print("\nCurrent Selected Features \n")
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
	for j in range(0, Dim):
		if(Elite_antlion_position[j]==1):
			a.append(j)
		b.append(j)
	if len(a)==0:
		pass
	
	import time

	start = time.time()
	print("classification accuracy = ",RForest_new.Random_Forest(a, X, y,Dim, 1)*100, "for number of features = ", len(a))
	end = time.time()
	print("Calculated in " + str(end-start) + " seconds\n")
	start = time.time()
	print("classification accuracy = ",RForest_new.Random_Forest(b, X, y,Dim, 1)*100, "for number of features = ", len(b))
	end = time.time()
	print("Calculated in " + str(end-start) + " seconds")


bALO(25, 25)