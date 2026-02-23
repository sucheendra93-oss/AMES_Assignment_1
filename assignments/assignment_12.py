'''The system logs show that errors occur on average 3 times per day.
Find the probability that exactly 2 errors occur tomorrow. 
Compute the average and variability. Mention which Python library models event counts.'''

from scipy.stats import poisson

# Given data
lambda_ = 3  # average number of errors per day
k = 2  # number of errors we want to find the probability for
# Calculate probability of exactly 2 errors
prob = poisson.pmf(k, lambda_)
# Calculate mean and variance
mean, var = poisson.stats(lambda_, moments='mv')
print(f"The probability that exactly 2 errors occur tomorrow is: {prob}")
print(f"Average number of errors (mean): {mean}")
print(f"Variance of the number of errors: {var}")