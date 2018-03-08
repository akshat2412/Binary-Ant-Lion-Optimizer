def GenerateData():	
	from sklearn.datasets import make_classification
	X, y = make_classification(n_samples=10000, n_features=60,n_informative=20,n_redundant=10,random_state=42)
	return X,y
