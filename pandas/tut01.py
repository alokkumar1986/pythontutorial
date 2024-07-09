import pandas as pd
import numpy as np

# print(np.__version__)
# print(pd.__version__)

# s1 = pd.Series()

# data = np.array([1, 3, 5, 7, 9])

# s2 = pd.Series(data, index=['A', 'B', 'C', 'D','E'])

# print(s1)

# print(s2)

# print(s2['D'])

sugarlevel = {
    "day1" : 120,
    "day2" : 125
}

s3= pd.Series(sugarlevel)
print(s3)

