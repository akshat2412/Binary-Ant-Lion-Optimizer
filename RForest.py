
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def Random_Forest(r):
	dataset = pd.read_csv('Social_Network_Ads.csv')
	X = dataset.iloc[:, r].values
	y = dataset.iloc[:, 4].values


	from sklearn.cross_validation import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


	from sklearn.preprocessing import StandardScaler
	sc = StandardScaler()
	X_train = sc.fit_transform(X_train)
	X_test = sc.transform(X_test)


	from sklearn.ensemble import RandomForestClassifier
	classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
	classifier.fit(X_train, y_train)

	y_pred = classifier.predict(X_test)


	from sklearn.metrics import confusion_matrix
	cm = confusion_matrix(y_test, y_pred)

	from sklearn.metrics import accuracy_score
	return accuracy_score(y_test,y_pred)
