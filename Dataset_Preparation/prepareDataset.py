import getDataframe
import storeSegments
import pandas as pd
import numpy as np
from sklearn import preprocessing
from numpy import genfromtxt
def get_size_data(extracted_data_folder):
	total_row_size  = 0
	max_column_size = 0
	str2 = extracted_data_folder + "Timeseries"
	for x in range(0,100):
		str1 = str2 + str(x)+ ".csv"
		try:
			df = pd.read_csv(str1, header=None)
		except:
			continue
		current_row_size = df.shape[0]
		current_column_size = df.shape[1]
		total_row_size = total_row_size + current_row_size
		if current_column_size > max_column_size:
			max_column_size = current_column_size
	return total_row_size,max_column_size

def merge_extracted_data():
	row_size,column_size = get_size_data()
	empty_data = np.zeros([1,column_size-1])
	str2 = extracted_data_folder + "Timeseries"
	for x in range(0,100):
		str1 = str2 + str(x)+ ".csv"
		try:
			df = pd.read_csv(str1, header=None)
		except:
			continue
		df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
		combined_data = np.zeros([df.shape[0],column_size-1])
		combined_data[:df.shape[0],:df.shape[1]] = df
		empty_data = np.concatenate((empty_data,combined_data))
		print(empty_data.shape)
	print(empty_data.shape)
	np.savetxt("/home/sutdai/Data_Analysis/Extracted_data/combined_data.csv",empty_data,delimiter=",")

merge_extracted_data()
