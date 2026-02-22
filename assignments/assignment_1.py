'''
You are working as a Machine Learning Engineer at a fintech company. 
Your team has built a fraud detection model that classifies transactions as fraud or legitimate. 
During development and deployment, you collect the following data: 
training time across runs, validation accuracy across folds, inference latency from production, 
loss values from training, prediction errors, and fraud labels and predictions. 
You must analyze this system statistically to understand performance, reliability, and risk.
Answer the following questions:
Q1. Training time (in minutes) from 10 independent model runs:
[42, 44, 45, 46, 44, 45, 47, 43, 100, 45]
-> Find three different measures that describe the “typical” training time. 
-> Determine whether the extreme value affects any of these measures. 
-> Describe the shape of the data distribution. 
-> State which Python library and module you would import to compute these measures.'''

from statistics import mean, median, mode
from scipy import stats

'''
    We would be using statistics module for mean, median and mode
    For skeweness we would use scipy as shown below
'''

arr = [42,44,45,46,44,45,47,43,100,45]
print('The mean is ',mean(arr)) #avg
print('The median is ',median(arr) ) #Middle value
print("The mode is ", mode(arr)) #Highest Freqency
print("The skewness is ",stats.skew(arr)) 
#if the skewness > 0 its right skewed!





