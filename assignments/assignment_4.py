'''
 Training loss values from multiple epochs:
[0.45, 0.48, 0.46, 0.44, 0.47, 0.49, 0.46, 1.20]
Find values that split the data into four equal parts. 
Use these values to measure how wide the middle region of data is. 
Decide whether the extreme value should be considered abnormal. 
Mention which numerical library can compute these.
'''

import numpy as np

data = [0.45, 0.48, 0.46, 0.44, 0.47, 0.49, 0.46, 1.20]
q1,q2,q3 = np.percentile(data,[25,50,75])
print('Lower bound is ',q1)
print('Median is ',q2)
print("Upper bound is ",q3)

#Calculate  how wide the middle region of data is (IQR)
iqr = q3-q1
print('Middle region width is ',iqr)

'''
Is the extreme value abnormal?? We should find step
The formula is 1.5 x IQR
'''

step = 1.5 * iqr
print('Step value is ',step)

max_upper_limit = q3 + step
print('max upper limit is ',max_upper_limit)

if max(data) > max_upper_limit:
    print(f"Max value {max(data)} is an outlier")
else:
    print("The data is not an outlier and extreme value is not abnormal")