'''
Inference time (ms) observed in production:
[120, 130, 125, 140, 150, 110, 115, 145, 135, 200]
Divide the data into positions that represent the lower, middle, and upper performance boundaries. 
Explain what the upper boundary means for user experience. 
Mention which library supports percentile calculations.
'''

import numpy as np

data = [120, 130, 125, 140, 150, 110, 115, 145, 135, 200]


# q1 = np.percentile(data,25)
# q2 = np.percentile(data,50)
# q3 = np.percentile(data,75)



#We can also do it using one liner syntax like this
q1,q2,q3 = np.percentile(data,[25,50,75])
print('Lower bound is ',q1)
print('Median is ',q2)
print("Upper bound is ",q3)

'''
Lower Boundary (25th Percentile): These are your "power users" or those on the fastest connections. 
Their experience is seamless.
Upper Boundary (75th Percentile): This is the threshold for "slow" performance.

UX Impact: In fintech, 
if the upper boundary (143.75 ms) is significantly higher than the median (132.5 ms), 
it indicates jitter. Users might perceive the app as "laggy" or "unstable." 
The outlier at 200 ms is particularly dangerous; 
if a user is trying to authorize a payment and it takes 200 ms while they are used to 110 ms, 
they may click "submit" twice, potentially causing duplicate transactions.
'''