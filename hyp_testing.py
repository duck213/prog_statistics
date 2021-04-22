import numpy as np
import scipy as sp
from scipy import stats

# 1. Binomial Hypothesis Testing
np.random.seed(seed=0)

random_ber = np.random.binomial(n=1,p=0.5,size=50)
n_ber = np.count_nonzero(random_ber)

# Hypothesis Testing
binom_test = sp.stats.binom_test(n_ber,50)
print('Binomial Testing:',binom_test)


# 2. Population Hypothesis Testing
np.random.seed(seed=1)
random_nor = np.random.normal(100, 10, 10) # mu, sigma, sample
nor_mean = np.mean(random_nor)


# The definition of Population hypothesis test function
def ztest(stat,mu,sigma):
    z = (stat.mean() - mu) / (sigma / np.sqrt(len(stat)))
    return (2 * (1-sp.stats.norm.cdf(z)))

# Hypothesis Testing
mu_test = ztest(random_nor, 100, 10)
print('mu Testing:',mu_test)



