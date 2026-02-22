''' Out of 300 transactions, 
50 were actually fraudulent and 40 of those were detected by the model. 
Find the likelihood that a transaction is flagged when it is truly fraudulent. 
Interpret this in terms of model reliability. 
Mention which library can be used for numerical probability.'''

'''This is a conditional probability problem. 
We need to find the probability of a transaction being flagged given that it is truly fraudulent. '''

def calculate_probability(num_fraudulent, num_flagged_fraudulent):
    if num_fraudulent == 0:
        return 0.0  # Avoid division by zero
    probability = num_flagged_fraudulent / num_fraudulent
    return round(probability, 4)

# Given data
total_transactions = 300
num_fraudulent = 50
num_flagged_fraudulent = 40
# Calculate the probability
probability = calculate_probability(num_fraudulent, num_flagged_fraudulent)
print(f"The likelihood that a transaction is flagged when it is truly fraudulent is: {probability}")