import getDataframe
import storeSegments
import pandas as pd
import numpy as np
from numpy import genfromtxt

def plot_raw_data(some_list,some_list_1):
	plt.plot(some_list)
	plt.plot(some_list_1)
	plt.title('Plot of filled missing value, sampling rate=16ms data')
	plt.show()
	plt.savefig('Pupil_Dilation_Cognitive_Load_Sampling_rate_16ms.png')

def one_sec_data(some_list,some_list_1):
	count_samples = len(some_list)	#Total number of samples
	count_load = len(some_list_1)
	if count_samples != count_load:
		print("There is some error in the code")
	sum_pupil_data = 0
	list_one_sec_pupil_data = []		#The list with sampling rate 1 sec
	list_one_sec_load_data = []
	for i in range(0,count_samples):
		if (i+1)%60==0:									#Looking for every 60th sample
			avg_pupil_data = sum_pupil_data/60
			list_one_sec_pupil_data.append(avg_pupil_data)
			sum_pupil_data = 0
		else:
			sum_pupil_data = sum_pupil_data + some_list[i]
	for i in range(0,count_load):
		if (i+1)%60==0:
			list_one_sec_load_data.append(some_list_1[i])
	return list_one_sec_pupil_data,list_one_sec_load_data

def plot_one_sec_data(some_list, some_list_1):
	#what if the transition in load is lost due to averaging
	one_sec_pupil,one_sec_load = one_sec_data(some_list,some_list_1)
	plt.plot(one_sec_pupil)
	plt.plot(one_sec_load)
	plt.title('Plot of filled missing value, sampling rate=1sec data')
	plt.show()

def plot_contraction_expansion(some_list, some_list_1):
	count_samples = len(some_list)	#Total number of samples
	count_load = len(some_list_1)
	normal_pupil_size = 0 		#Trying to get the pupil size when there is no task
	count_no_task = 0
	sum_normal_pupil_size = 0
	for i in range(0,count_load):
		if some_list_1[i]==0:
			count_no_task = count_no_task + 1
			sum_normal_pupil_size = sum_normal_pupil_size + some_list[i]
	normal_pupil_size = sum_normal_pupil_size/count_no_task
	for i in range(0,count_samples):
		some_list[i] = some_list[i]-normal_pupil_size
	plt.plot(some_list)
	plt.plot(some_list_1)
	plt.title('Plot of filled missing value, sampling rate=16ms, contraction/expansion data')
	plt.show()

def plot_one_sec_contraction_expansion(some_list, some_list_1):
	one_sec_pupil,one_sec_load = one_sec_data(some_list,some_list_1)
	plot_contraction_expansion(one_sec_pupil, one_sec_load)

def make_Plots():
	raw_data_folder = "/home/epd/Project-Cognitive_load_level_prediction_using_pupil_data/Data/NoHeader/"
	for i in range(1,6):
		str1 = raw_data_folder + "KY"+"{0:03}".format(i) + ".csv"
		print(str1)
		df = pd.read_csv(str1)
		df1 = getDataframe.extract_relevant_columns(df)
		df2 = getDataframe.make_it_periodic(df1,i)
		list_pupil_left,list_load_level = storeSegments.read_pupil_load(df2)	
		update_pupil_left = storeSegments.fill_missing_values(list_pupil_left,5)
		updated_load_level = storeSegments.rectify_response_status(list_load_level)
		update_pupil_left = np.asarray(update_pupil_left)
		updated_load_level = np.asarray(updated_load_level)
		file_1 = "update_pupil_left"+str(i)+".csv"
		file_2 = "update_load_level"+str(i)+".csv"
		np.savetxt(file_1, update_pupil_left, delimiter=",")		#Saving pupil dilation data as a csv file
		np.savetxt(file_2, updated_load_level, delimiter=",")	#Saving cognitive load data as a csv file

