import numpy as np
'''
Historical data shows that only 2% of all transactions are fraudulent, 
the model flags 95% of true frauds, and the model incorrectly flags 10% of legitimate transactions. 
A new transaction is flagged as fraud.
Compute the chance that the transaction is truly fraudulent. 
Explain why the result is much lower than expected. 
Mention which math or scientific library can perform this calculation.
'''


def get_fraud_probability(p_fraud, p_flag_given_fraud, p_flag_given_legit):
    # P(Legitimate)
    p_legit = 1.0 - p_fraud
    
    # P(Flag | Fraud) * P(Fraud) -> True Positives
    true_positives = p_flag_given_fraud * p_fraud
    
    # P(Flag | Legit) * P(Legit) -> False Positives
    false_positives = p_flag_given_legit * p_legit
    
    # Total Probability of a Flag: P(Flag)
    p_total_flag = true_positives + false_positives
    
    # Bayes' Theorem: P(Fraud | Flag)
    # The result is our "Posterior" probability
    p_fraud_given_flag = true_positives / p_total_flag
    
    return round(p_fraud_given_flag, 4)

# Inputs from your problem
prior_f = 0.02    # 2% Base rate
recall = 0.95     # 95% Sensitivity
fpr = 0.10        # 10% False Positive Rate

result = get_fraud_probability(prior_f, recall, fpr)

print(f"The probability that the flagged transaction is fraud is: {result}")