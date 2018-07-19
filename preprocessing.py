import pandas as pd
import numpy as np
str1 = "/home/sutdai/Data_Analysis/Timeseries_data/Timeseries"
for x in range(11,100):
	str2 = str1 + str(x) + ".csv"
	df = pd.read_csv(str2)
	countRow = df.shape[0]
	time_in_sec = []
	diff = []
	df['Time_in_sec'] = pd.Series(np.random.randn(countRow), index=df.index)
	for i in range(0,countRow):
		h,m,s = df.iloc[i,3].split(":")
		h = float(h)
		m = float(m)
		s = float(s)
		df.iloc[i,5] = h*3600 + m*60 + s
	value_to_be_subtracted = df.iloc[1,5]
	df['Time_in_sec'] = df['Time_in_sec']-value_to_be_subtracted
	df['Dif_in_time'] = df['Time_in_sec'] - df['Time_in_sec'].shift(-1)
	df = df[df.Dif_in_time != 0]
	df.to_csv("/home/sutdai/Data_Analysis/Timeseries_data_No_Duplicates/Timeseries"+str(x)+".csv")
 
