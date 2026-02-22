'''
alidation accuracy (%) across 8 cross-validation folds:
[85, 86, 84, 87, 85, 86, 88, 84]
-> Compute two numerical values that describe how spread out the accuracies are. 
-> Explain what small values of these measures imply about the model. 
-> Mention which numerical Python library you would use.
'''

import numpy as np
from statistics import mean
from math import sqrt
data = [85, 86, 84, 87, 85, 86, 88, 84]

'''
Compute two numerical values that describe how spread out the accuracies are.  (Range)
Formula for range is range = max_value - min_value
'''


'''
    I am doing it without using any libraries first, and in the end, ill be using 
    numpy module
'''

#sort the array
data.sort()

max_value = max(data)
min_value = min(data)

range = max_value - min_value
print('The range is ',range)

'''
Explain what small values of these measures imply about the model. (SD and Variance)
'''
#calculate mean
mean_value = mean(data)

#finding (xi - mean)

res = sum(list(map(lambda x: pow((x-mean_value),2),data )))
variance = res/len(data)
print('The variance is ',variance)
print('Standard deviation is ',sqrt(variance))



'''
Using numpy
'''
#==========================================#


#To calculate the range we use ptp method from numpy
range = np.ptp(data)
print("The range is ",range)

#To calculate the standard deviation we use std method from numpy

std_dev = np.std(data)
print("The std deviation is ",std_dev)
