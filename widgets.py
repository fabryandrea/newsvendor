import numpy as np
from scipy.stats import norm

# discrete case (uniform distribution)
widget_demand = np.array([1, 2, 3, 4, 5, 6, 7, 8])
order = 5
widget_prob = np.array([0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125])

# calculate expected demand
def calculate_expected_demand(demand, prob):
    exp_demand = np.sum(demand * prob)
    return exp_demand

exp_demand = calculate_expected_demand(widget_demand, widget_prob)
print(exp_demand)

# calculate expected sales
def calculate_expected_sales(demand, prob, order_size):
    exp_sales = [d * p if d <= order_size else order_size * p
    for d, p in zip(demand, prob)]
    return exp_sales

exp_sales = calculate_expected_sales(widget_demand, widget_prob, 5)
print(exp_sales)

# calculate expected units short
def calculate_expected_units(demand, prob, order_size):
    exp_units = [(d - order_size)* p if d >= order_size else 0
    for d, p in zip(demand, prob)]
    return exp_units

exp_units = calculate_expected_units(widget_demand, widget_prob, 5)
print(exp_units)

# continuous case (normal distribution)
q = 190
mu = 160
sigma = 45
k = (q - mu)/sigma
print(k)

gk = norm.pdf(k, 0, 1) - (k * norm.sf(k))
exp_us = gk * sigma
print(exp_us)
