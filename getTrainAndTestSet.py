import getDataframe
import storeSegments
import pandas as pd
import numpy as np
from sklearn import preprocessing
from numpy import genfromtxt
def split_dataset(train_ratio):
	dataset = genfromtxt("/home/sutdai/Data_Analysis/Extracted_data/combined_data.csv", delimiter=',')
	labels = genfromtxt("/home/sutdai/Data_Analysis/Extracted_data/label_data.csv", delimiter=',')
	total_samples = dataset.shape[0]
	train_samples = np.floor(train_ratio*total_samples)
	X_train = dataset[1:train_samples,:]
	Y_train = labels[1:train_samples,:]
	X_test = dataset[train_samples:dataset.shape[0],:]
	Y_test = labels[train_samples:dataset.shape[0],:]
	return X_train,Y_train,X_test,Y_test

def strip_off_labels():
	label_data = np.zeros([1,])
	for files in filenames:
		str3 = files + ".csv"
		df2 = pd.read_csv(str3, header=None)
		user_label_data = np.asarray(df2.iloc[:,-1])
		label_data = np.concatenate((label_data,user_label_data))
	np.savetxt("/home/sutdai/Data_Analysis/Extracted_data/label_data.csv",label_data,delimiter=",")
	return label_data


