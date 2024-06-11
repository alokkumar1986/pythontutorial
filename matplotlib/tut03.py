import matplotlib.pyplot as plt
import numpy as np
plt.xlabel('Overs')
plt.ylabel('Scores')
plt.title('Overwise score of India vs Pakistan')
x = np.array([5, 10, 15, 20])
y = np.array([40, 65, 79, 119])
# plt.plot(x, y, color='green', linewidth=2, linestyle='dashed', marker='o', markersize=5, markeredgecolor='darkred')
plt.barh(x, y, color='red')
plt.show()
