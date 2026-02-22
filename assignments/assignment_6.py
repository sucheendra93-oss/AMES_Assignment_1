'''The model correctly predicts 90 out of 120 transactions.
Find the likelihood that the model makes a correct prediction. 
State whether this result summarizes past data or predicts unseen behavior. 
Mention which standard Python module supports such numeric calculations.'''

'''
We need to find the probability(P)
P = No of favourable outcomes / Total outcomes
'''

correct_prediction = 90
total_transactions = 120

p = correct_prediction / total_transactions
print("The likelihood that the model makes a correct prediction ",p)

'''
The results summarises the past data, because we already have the data about predictions, 
Its descriptive statistics

'''