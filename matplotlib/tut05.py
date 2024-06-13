import matplotlib.pyplot as plt
import numpy as np

slice = np.array([25, 25, 35, 15])
labels= np.array(['HR', 'IT', 'Finance', 'Sales'])
colors = np.array(['red', 'green', 'yellow', 'blue'])

exp = [0, 0, 0.001, 0]

plt.title('Dept wise employee strength')
plt.pie(slice, labels=labels, colors=colors, startangle=90, explode=exp, shadow=False, autopct='%.1f%%')
plt.legend()
plt.show()