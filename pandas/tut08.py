import pandas as pd

data = pd.read_csv('C:/Users/ISU_375/Desktop/pythontutorial/pandas/data.csv')

# data1 = data.duplicated()

# print(data.duplicated().to_string())  #5 #36

# print(data.loc[5])

# print(data.loc[36])

data2 = data.drop_duplicates()

print(data2.loc[5])

print(data2.loc[36])

