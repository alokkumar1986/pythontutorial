import pandas as pd
# import numpy as np

data = [
   {
       "name" : "XYZ",
       "sugar" : 128,
       "gender" : "Male"
   }, 
   {
       "name" : "PQR",
       "sugar" : 138,
       "gender" : "Female"
   }
]

df = pd.DataFrame(data, index=['person1', 'person2'])

print(df.loc['person1'])

