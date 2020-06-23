import numpy as np
from numpy.random import uniform
from scipy.stats import binom

np.random.seed(0)

p_H1 = p_H2 = 0.5
p_data_given_H1 = binom.pmf(28, 40, 0.5)

p_data_given_H2 = 0.0
for i in range(10000):
    pi = uniform(low=0.5, high=1.0)
    p_data_given_H2 += binom.pmf(28, 40, pi) * 1.0 / (1.0 - 0.5)

p_data_given_H2 = p_data_given_H2 / 10000

print(p_data_given_H1)
print(p_data_given_H2)


p_H1_given_data = (p_data_given_H1 * p_H1) / (p_data_given_H1 * p_H1 + p_data_given_H2 * p_H2)
p_H2_given_data = (p_data_given_H2 * p_H2) / (p_data_given_H1 * p_H1 + p_data_given_H2 * p_H2)

print(p_H1_given_data)
print(p_H2_given_data)
