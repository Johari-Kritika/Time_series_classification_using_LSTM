class Store_Segments(object):
	def __init__(self, dataframe):
		self.data_folder = dataframe

	def read_pupil_load(self, dataframe):
		df = pd.read_csv(dataframe)
		countRow = df.shape[0]
		count = 0
		list_pupil_left = df['PupilLeft']
		list_load_level = df['LoadLevel']
		return list_pupil_left,list_load_level

	def fill_missing_values(some_list,buffer_size):
		valid_values = []
		for i in range(0,len(some_list)):
			if some_list[i] != -1:
				valid_pupil_value = some_list[i]
				if len(valid_values) == buffer_size:
					valid_values.pop(0)
				valid_values.append(valid_pupil_value)
			else:
				if len(valid_values) == buffer_size:
					mean_value = sum(valid_values)/buffer_size
					some_list[i] = mean_value

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

	def max_timestep_taken(some_list):
		max_ = 0
		for j in range(0,len(some_list)-1):
			if j%2 ==0:
				timestep_taken = some_list[j+1] -some_list[j]
				if timestep_taken > max_:
					max_  = timestep_taken

	def extract_segments(some_list,some_list_1,userid):
		list_diff_load = some_list - some_list.shift(-1)
		k = list_diff_load.nonzero()
		k1 = k[0]
		num_of_tasks = (len(k1)-1)/2
		max_ = max_timestep_taken(k1)
		extracted_data_middle = np.zeros([num_of_tasks, max_+1])
		for l in range(0,len(k1)-1):
			if l%2 ==0:
				num_of_timestep = k1[l+1] - k1[l]-1
				extracted_data_middle[l/2,0:num_of_timestep] = some_list_1[k1[l]+1:k1[l+1]]
				extracted_data_middle[l/2,max_] = some_list[k1[l]+1]
		np.savetxt("/home/sutdai/Data_Analysis/Extracted_data/Timeseries"+str(userid)+".csv",extracted_data_middle,delimiter=",")
