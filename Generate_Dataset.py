import csv
import pandas as pd
import numpy as np
def GenerateData1():
	data=pd.read_csv('parkinsons2.csv')
	# ans = np.isnan(data).any()
	# print(data.shape)
	# data.dropna(inplace = True)
	print(data.shape)
	# data.fillna(0.9)
	X=data.iloc[:,:22]
	y=data.iloc[:,22]
	X= np.array(X)
	y= np.array(y)
	print(X.shape)
	# np.random.shuffle(X)
	print(X.shape)
	return X,y	
	

GenerateData1()