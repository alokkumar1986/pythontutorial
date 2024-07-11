import pandas as pd

# df1 = pd.DataFrame({
#    "name" : ['ABC', 'PQR', 'XYZ'],
#    "age" : [30, 49, 61]
# })

df1 = pd.read_json('C:/Users/ISU_375/Desktop/pythontutorial/pandas/df1.json')
df2 = pd.DataFrame({
    "name" : ['ABC', 'RQP', 'ZYX'],
    "age" : [30, 44, 66]
})

print(df1)
print(df2)

ndf = df1.merge(df2, how='right')

# ndf = pd.read_json('C:/Users/ISU_375/Desktop/pythontutorial/pandas/CONTESTANT_LIST.json')

# df1.merge()

print(ndf)

# print(ndf.query("AGE < 30"))