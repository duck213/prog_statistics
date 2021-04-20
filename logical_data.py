import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from statistics import variance, stdev



# 1. Measure of central tendency
# a example of caffeine to calculate many kinds of statistics skills

coffee = np.array([202,177,121,148,89,121,137,158])
'''
# average
cf_mean = np.mean(coffee)
print("Mean :", round(cf_mean,2))

# Median
cf_median = np.median(coffee)
print("Median :", round(cf_median,2))

# Mode
cf_mode = stats.mode(coffee)
print("Mode :", cf_mode)

# Variance
cf_var = variance(coffee)
print("Variance :", round(cf_var,2))

# Standard Deviation
cf_std = stdev(coffee)
print("Standard Deviation :", round(cf_std,2))

# Range
cf_range = np.max(coffee, axis=0) - np.min(coffee, axis=0)
print("Range :", cf_range)

# Percentile
cf_quant_20 = np.percentile(coffee,20)
cf_quant_80 = np.percentile(coffee,80)
print("20 Quantiles : ", cf_quant_20 )
print("80 Quantiles : ", cf_quant_80 )

# Interquartile range (IQR)
q75, q25 = np.percentile(coffee, [75, 25])
cf_IQR = q75-q25
print("Inter quartile range:",cf_IQR)

# Coefficient of variation (CV)
cf_cv = stdev(coffee) / np.mean(coffee)
cf_cv = round(cf_cv,2)
print("CV:", cf_cv)
'''

# 2. Numerical data
# 2-1 With a example of a cup of coffee

drink_cup = pd.DataFrame({'cup':[22,7,19,3,10,7,15,9,35,5],
                          'who': ['Dmitriy', 'Anton', 'Ivan', 'Sergey', 'Andrey',
                                  'Dmitriy','Ivan','Sergey', 'Andrey','Sergey']})

# Frequency Table
# Data divided 4 groups in factor_cup
factor_cup = pd.cut(drink_cup.cup,4)
group_cup = drink_cup['cup'].groupby(factor_cup)
count_cup = group_cup.agg(['count'])
print(count_cup)

# 2-2 box plot
plt.subplots()
plt.boxplot(coffee)
plt.show()

# 2-3 crosstab
mart = pd.read_csv("mart.csv")
# Preferred mart in region
region_crosstab = pd.crosstab(mart['region'],mart['mart'])
print(region_crosstab)
# Preferred mart in region with family members
famnum_crosstab = pd.crosstab(mart['family_num'],mart['mart'])
print(famnum_crosstab)

# 2-4 scatter about body figure
body = pd.read_csv("body.csv")

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

ax1.scatter(body['height'], body['weight'])
ax2.scatter(body['height'], body['body_fat'])
ax3.scatter(body['height'], body['leglen'])
ax4.scatter(body['height'], body['hair'])



# 2-5 covariance
cov_body = body.cov()
print(cov_body)

# 2-6 Correlation Coefficient
corr_body = body.corr()
print(corr_body)


plt.show()