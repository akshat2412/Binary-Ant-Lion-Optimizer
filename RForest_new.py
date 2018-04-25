
import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd

def Random_Forest(r,X,y,dim, flag=0):
	X = X[:,r]
	y = y
	from sklearn.cross_validation import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


	from sklearn.preprocessing import StandardScaler
	sc = StandardScaler()
	X_train = sc.fit_transform(X_train)
	X_test = sc.transform(X_test)


	from sklearn.neighbors import KNeighborsClassifier
	neigh = KNeighborsClassifier(n_neighbors=5)
	neigh.fit(X_train,y_train) 
	y_pred = neigh.predict(X_test)

	from sklearn.metrics import confusion_matrix
	cm = confusion_matrix(y_test, y_pred)

	from sklearn.metrics import accuracy_score
	acc = accuracy_score(y_test,y_pred)

	if(flag):
		return acc
	
	alpha=0.01
	beta=1-alpha
	fitness=alpha*(1.0-acc)+beta*(len(r)/dim)
	# fitness=1/acc
	# print(acc)
	# print(str(fitness)+"\n")
	return fitness