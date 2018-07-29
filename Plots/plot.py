# Input data file consist of 5 relevant columns
# Column 2 : PupilLeft
# Column 3 : PupilRight
# Column 4 : LoadLevel
# Column 5 : Time_in_sec
# Column 6 : Diff_in_time
import pandas as pd
from sklearn import preprocessing
folder_name = "E:/Kyanite/Data Analysis/Testing files/try"
normal = True
def read_pupil_load(dataframe):
		df = pd.read_csv(dataframe)
		countRow = df.shape[0]
		count = 0
		list_pupil_left = df['PupilLeft']
		list_load_level = df['LoadLevel']
		return list_pupil_left,list_load_level
  
def fill_missing_values(some_list,buffer_size):
		valid_values = []
		for i in range(0,len(some_list)):
			if some_list[i] != -1:	#Pupil size can't be -1
				valid_pupil_value = some_list[i]
				if len(valid_values) == buffer_size:	#Taking only the recent buffer_size values
					valid_values.pop(0)
				valid_values.append(valid_pupil_value)
			else:
				if len(valid_values) == buffer_size:
					mean_value = sum(valid_values)/buffer_size
					some_list[i] = mean_value	#Replace -1 with the mean of previous buffer_size values
    return some_list
          
def rectify_response_status(some_list):
		for i in range(0,len(some_list)):
			if some_list[i] != 0:
				count = count + 1
				value = some_list[i]
				if count == 1:
					first_value = value
				if value != first_value:
					some_list[i]=first_value
			else:
				count = 0
		return some_list
          
for i in range(1,5):
  filename = folder_name +str(i) +".csv"   #get the name of the .csv file
  print(filename)
  try:
    df = pd.read_csv(filename, header=None)
  except:
    normal = False
    print("Kritika")
    print("It still works")
  if normal:
    col_pupil_left,col_load_level = read_pupil_load(df)
    updated_col_pupil_left = fill_missing_values(col_pupil_left,5)
    rectify_response_status(col_load_level)
    normalized_col_pupil_left= preprocessing.normalize(updated_col_pupil_left)
  else:
    continue
