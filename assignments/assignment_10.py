'''The classifier predicts fraud with probability 0.4 for each transaction.
Write the function that assigns probabilities to both possible outcomes. 
Find the long-run average outcome and how much it varies. 
Mention which statistics library contains this distribution.'''

from scipy.stats import bernoulli

p = 0.4

# Calculate mean and variance
mean, var = bernoulli.stats(p, moments='mv')
print(f"Long-run average outcome (mean): {mean}")
print(f"Variance of the outcome: {var}")