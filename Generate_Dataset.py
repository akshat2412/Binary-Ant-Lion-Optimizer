import csv
import pandas as pd
def GenerateData1():
	data=pd.read_csv('Heart_data.csv')
	X=data.iloc[:,:44]
	y=data.iloc[:,44]
	return X,y	
	
