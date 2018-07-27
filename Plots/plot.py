# Input data file consist of 5 relevant columns
# Column 2 : PupilLeft
# Column 3 : PupilRight
# Column 4 : LoadLevel
# Column 5 : Time_in_sec
# Column 6 : Diff_in_time
import pandas as pd
folder_name = ""
for i in range(0,100):
  filename = folder_name + str(i) +".csv"   #get the name of the .csv file
  try:
    df = pd.read_csv(filename, header=None)
    print(i)
  except:
    print("Kritika")
  print("It still works")
