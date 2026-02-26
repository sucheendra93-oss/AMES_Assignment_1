'''The prediction error of the model is centered around 0 with spread 4.
Find the probability that the error is greater than 3. Explain what this means for model reliability. 
Mention which Python library supports continuous distributions.'''


from scipy.stats import norm

# Given data
mean = 0
std_dev = 4
x = 3

cdf_value = norm.cdf(x, loc=mean, scale=std_dev)
print(f"The probability that the error is lesser than 3 is: {cdf_value}")
# Calculate the probability that the error is greater than 3
prob = 1 - cdf_value
print(f"The probability that the error is greater than 3 is: {prob}")
