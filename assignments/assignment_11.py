'''
The model is tested on 10 transactions, each independently predicted correctly with probability 0.8. 
Find the likelihood that the model is correct exactly 7 times. 
Find the expected number of correct predictions and how much this varies. 
Mention which Python module handles this type of calculation.'''


from scipy.stats import binom


p = 0.8
n = 10
k = 7
# Calculate probability of exactly 7 correct
prob = binom.pmf(k, n, p)

# Calculate mean and variance
mean, var = binom.stats(n, p, moments='mv')

print(f"The likelihood that the model is correct exactly 7 times is: {prob}")
print(f"Expected number of correct predictions (mean): {mean}")
print(f"Variance of the number of correct predictions: {var}")