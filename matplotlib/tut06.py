import matplotlib.pyplot as plt
age = [10, 5, 20, 14, 25, 21, 34, 32, 23, 22, 44, 42, 51, 64, 43, 59]
years = [0, 10, 20, 30, 40, 50, 60, 70]
plt.title('Age wise employees in Aptech')
plt.xlabel('Age')
plt.ylabel('No. of emp')
plt.hist(age, bins=years, color='blue', histtype='bar', rwidth=.8 )
# plt.legend()
plt.show()

