import getDataframe
import storeSegments
import pandas as pd
import numpy as np
from sklearn import preprocessing
from numpy import genfromtxt

def create_Extracted_Data_Folder():
	for i in range(0,100):
		df = getDataframe.extract_relevant_columns("/home/kyanite/Documents/doc/Data Analysis/NoHeader/",i)
		df1 = getDataframe.make_it_periodic(df,i)
		list_pupil_left,list_load_level = storeSegments.read_pupil_load(df1)
		update_pupil_left = storeSegments.fill_missing_values(list_pupil_left,5)
		normalized_list_pupil_left= preprocessing.normalize(update_pupil_left)
		updated_load_level = storeSegments.rectify_response_status(list_load_level)
		storeSegments.extract_segments(list_load_level, normalized_list_pupil_left[0],x)
