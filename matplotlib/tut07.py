import matplotlib.pyplot as plt
import numpy as np

x = np.array([7,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,100,86,98,87,94,78,77,85,86])

a = np.array([5,17,18,17,12,57])
b = np.array([99,86,87,88,100,86])

colors = ['black', 'green', 'orange', 'blue', 'yellow', 'pink']

plt.xlabel('Marks')
plt.ylabel('No. of Students')
plt.title('No. of Students securing % marks')

plt.scatter(x, y, color='red')
plt.scatter(a, b, cmap='viridis', c=colors, alpha=0.5, s=[120, 230, 340, 450, 560, 70], plotnonfinite=True)

plt.colorbar()

plt.show()