import pandas as pd

data = pd.read_csv('C:/Users/ISU_375/Desktop/pythontutorial/pandas/data.csv')

mean = data['Calories'].mean()

median = data['Calories'].median()

mode = data['Calories'].mode()[0]

# print(mode)



# data1= data['Calories'].fillna(round(mean, 1)).to_string()

# print(data1)


# data2= data['Calories'].fillna(round(median, 1)).to_string()

# print(data2)


data3= data['Calories'].fillna(round(mode, 1)).to_string()

print(data3)
