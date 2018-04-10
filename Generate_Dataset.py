import csv
import pandas as pd
import numpy as np
def GenerateData1():
	data=pd.read_csv('Heart_data.csv')
	X=data.iloc[:,:44]
	y=data.iloc[:,44]
	X= np.array(X)
	y= np.array(y)
	return X,y	
	

