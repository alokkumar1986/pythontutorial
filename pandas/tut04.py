import pandas as pd

df = pd.read_json('C:/Users/ISU_375/Desktop/pythontutorial/pandas/CONTESTANT_LIST.json')

# print(df)

# print(df.NAME)
# print(df.head(10))

# print(df.loc[151])

print(df.tail())

print(df.info())