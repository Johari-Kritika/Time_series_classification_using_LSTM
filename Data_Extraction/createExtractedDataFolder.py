import getDataframe
import storeSegments
import pandas as pd
import numpy as np
from sklearn import preprocessing
from numpy import genfromtxt
normal = True
def create_Extracted_Data_Folder():
	raw_data_folder = "/home/epd/Project-Cognitive_load_level_prediction_using_pupil_data/Data/NoHeader/"
	for i in range(0,100):
		str1 = str2 + "KY"+"{0:03}".format(i) + ".csv"
		try:
			df = pd.read_csv(str1)
		except:
			normal = False
		if normal:
			df1 = getDataframe.extract_relevant_columns(df,i)
			df2 = getDataframe.make_it_periodic(df1,i)
			list_pupil_left,list_load_level = storeSegments.read_pupil_load(df1)	
			update_pupil_left = storeSegments.fill_missing_values(list_pupil_left,5)
			normalized_list_pupil_left= preprocessing.normalize(update_pupil_left)
			updated_load_level = storeSegments.rectify_response_status(list_load_level)
			storeSegments.extract_segments(list_load_level, normalized_list_pupil_left[0],x)
		else:
			continue
	
