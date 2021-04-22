import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats


# 1. Binomial Distribution
n, p = 10, 0.3
stat_bin = sp.stats.binom(n,p)

fig = plt.figure(figsize=(16,8))
ax1 = fig.add_subplot(2,4,1)
ax2 = fig.add_subplot(2,4,2)
ax3 = fig.add_subplot(2,4,3)
ax4 = fig.add_subplot(2,4,4)
ax5 = fig.add_subplot(2,4,5)
ax6 = fig.add_subplot(2,4,6)
ax7 = fig.add_subplot(2,4,7)
ax8 = fig.add_subplot(2,4,8)
x_axis = np.arange(n+1)

# Probability Mass Function(pmf)
ax1.bar(x_axis, stat_bin.pmf(x_axis))
ax1.title.set_text("Binomial Distribution pmf")

# Cumulative Distribution Function(cdf)
ax2.bar(x_axis, stat_bin.cdf(x_axis))
ax2.title.set_text("Binomial Distribution cdf")

# random seed & sample extraction
np.random.seed(seed=0)
random_bin = np.random.binomial(n=10, p=0.3, size=50)
bin_mean = np.mean(random_bin)
print('Binomial Average:',bin_mean)


# 2. Hypergeometric Distribution
[M,n,N] = [30,5,10]
stat_hyp = sp.stats.hypergeom(M,n,N)

# Probability Mass Function(pmf)
ax3.bar(x_axis, stat_hyp.pmf(x_axis))
ax3.title.set_text("Hypergeometric Distribution pmf")

# Cumulative Distribution Function(cdf)
ax4.bar(x_axis, stat_hyp.cdf(x_axis))
ax4.title.set_text("Hypergeometric Distribution cdf")

# random seed & sample extraction
np.random.seed(seed=0)
random_hyp = np.random.hypergeometric(ngood=5, nbad=25, nsample=10, size=50)
hyp_mean = np.mean(random_hyp)
print('Hypergeometric Average:',hyp_mean)


# 3. Uniform Distribution
[M,n,N] = [30,5,10]
stat_uni = sp.stats.uniform()
x_axis = np.linspace(0,1,100)

# Probability Distribution Function(pdf)
ax5.bar(x_axis, stat_uni.pdf(x_axis))
ax5.title.set_text("Uniform Distribution pdf")

# Cumulative Distribution Function(cdf)
ax6.bar(x_axis, stat_uni.cdf(x_axis))
ax6.title.set_text("Uniform Distribution cdf")

# random seed & sample extraction
np.random.seed(seed=0)
random_uni = np.random.uniform(0,1,100)
uni_mean = np.mean(random_uni)
print('Uniform Average:',uni_mean)


# 4. Normal Distribution
stat_nor = sp.stats.norm()
x_axis = np.linspace(-3,3,100)

# Probability Distribution Function(pdf)
ax7.bar(x_axis, stat_nor.pdf(x_axis))
ax7.title.set_text("Normal Distribution pdf")

# Cumulative Distribution Function(cdf)
ax8.bar(x_axis, stat_nor.cdf(x_axis))
ax8.title.set_text("Normal Distribution cdf")

# random seed & sample extraction
np.random.seed(seed=0)
random_nor = np.random.normal(0,1,100)
nor_mean = np.mean(random_nor)
print('Normal Average:',nor_mean)


plt.tight_layout()
plt.show()