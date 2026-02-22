'''
Q5. Prediction errors from a noisy validation batch:
[2, 3, 2, 3, 100, 2, 3, 2]
i)Compute the average error using all values.
ii)Recompute the average after removing the highest and lowest 20% of values.
iii)Explain why the second average better reflects model behavior.
State which scientific Python library provides trimmed statistics.
'''

'''First ill solve this without library, later ill use library'''
from scipy import stats
import numpy as np 
data = [2, 3, 2, 3, 100, 2, 3, 2]
data.sort()

mean_of_all_values = np.mean(data)
print("Mean of all values ",mean_of_all_values) #14.625

#removing 20% from beginning and ending
items_to_remove = int(len(data) * 0.2)
print('items to remove',items_to_remove)

#removing items from data
data.pop()
data.pop(0)

print(data)

#calculate after removing 20% of values from beginning and end

trimmed_mean_value = np.mean(data)
print("Trimmed ",trimmed_mean_value) #2.5



'''Using the library, we can use the stats.trim_mean()'''
data = [2, 3, 2, 3, 100, 2, 3, 2]
trimmed_mean = stats.trim_mean(data,proportiontocut=0.2)
print("Trimmed mean using library ",trimmed_mean)