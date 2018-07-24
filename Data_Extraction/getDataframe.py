class Get_Dataframe(object):

	def __init__(self, data_folder):
		self.data_folder = data_folder

	def extract_relevant_columns(no_header_data_folder,userid):
		str2 = no_header_data_folder
		str1 = str2 + "KY"+"{0:03}".format(userid) + ".csv"
		try:
			df = pd.read_csv(str1)
		except:
			continue
    		df1 = df[['PupilLeft','PupilRight']]
    		df1['TimeStamp'] = df.iloc[:,19]
    		df1['TaskId'] = df.iloc[:,106]
    		df1['RobotName'] = df.iloc[:,109]
    		df1['ResponseStatus'] = df.iloc[:,110]
   		df1['TaskId'].fillna(0, inplace=True)
    		df1['RobotName'].fillna(0, inplace=True)
    		z = {0:0,"A1":1,"A2":2,"B1":2,"A3":1,"A4":2,"B2":2,"V1":3,"A5":3,"B3":3,"B4":3,"A6":3,"V2":3,"B5":1,"A7":3,"B6":3,"V3":3,"B7":2,"V4":2,"A8":3,"B8":3,"V5":3,"B9":2,"V6":2,"A9":3,"B10":3,"V7":3,"B11":1,"B12":1,"A10":1,"A11":2,"B13":2,"A12":2,"V8":2,"V9":1,"B14":1,"A13":2,"V10":2,"B15":1,"A14":1,"A15":1,"A16":3,"B16":3,"V11":3,"B17":1,"A17":1,"A18":2,"B18":2}
    		status_map = {"start" : 0, "attempt" : 1,"expire" : 1}
    		taskNumMap = {0:0,"A1":1,"A2":2,"B1":2,"A3":3,"A4":4,"B2":4,"V1":5,"A5":5,"B3":5,"B4":6,"A6":6,"V2":6,"B5":7,"A7":8,"B6":8,"V3":8,"B7":9,"V4":9,"A8":10,"B8":10,"V5":10,"B9":11,"V6":11,"A9":12,"B10":12,"V7":12,"B11":13,"B12":14,"A10":15,"A11":16,"B13":16,"A12":17,"V8":17,"V9":18,"B14":19,"A13":20,"V10":20,"B15":21,"A14":22,"A15":23,"A16":24,"B16":24,"V11":24,"B17":25,"A17":26,"A18":27,"B18":27}
    		df1['ResponseStatus'] = df1['ResponseStatus'].map(status_map)
    		df1['ResponseStatus'].fillna(0, inplace=True)
    		y = df1['TaskId']
    		load_level = y.map(z)
    		df1['LoadLevel']=load_level
    		df1['TaskNum'] = df1['TaskId'].map(taskNumMap)
    		countRow = df1.shape[0]
    		tempNum = 0
    		subfactor = 0
		for i in range(0,countRow):
			if df1['ResponseStatus'].iloc[i]==1:
			    taskNum = df1['TaskNum'].iloc[i]
			    k = df1['TaskId'].iloc[i]
			    robotName = k[0]
			    if taskNum == tempNum:
				if robotName != tempName:
				    subfactor = subfactor + 1
			    else:
				subfactor = 1
			    tempNum = taskNum
			    tempName = robotName
			    df1['LoadLevel'].iloc[i] = df1['LoadLevel'].iloc[i]-subfactor
			    if df1['LoadLevel'].iloc[i] < 0:
				df1['LoadLevel'].iloc[i] = 0
		training_set = df1[['PupilLeft','PupilRight','TimeStamp','LoadLevel']]
		return df


	def make_it_periodic(self, relevant_columns_data,userid):
		df = relevant_columns_data
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
		return df
