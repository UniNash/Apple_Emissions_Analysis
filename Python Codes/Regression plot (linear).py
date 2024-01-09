# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(price_to_sales_ratio, gross_emissions_reduction_rate_baseline)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:

import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from scipy import stats

X1 = dataset[['price_to_sales_ratio']].iloc[[1,2,3,4,6,7]]
Y1 = dataset[['gross_emissions_reduction_rate_baseline']].iloc[[1,2,3,4,6,7]]

lm = LinearRegression()
lm.fit(X1,Y1)
Rsquared = lm.score(X1, Y1)
correlation_coefficient, p_value = stats.pearsonr(list(X1["price_to_sales_ratio"]), list(Y1["gross_emissions_reduction_rate_baseline"]))

a = lm.intercept_
b = lm.coef_

plt.figure(figsize=(9,7 ))

regression_plot = sns.regplot(x = X1, y = Y1)

#regression_plot.set_title('Price to Sales vs Gross Emission Reduction Rate (Baseline)', fontdict={'size': 15})

regression_plot.set_xlabel('Price-to-Sales (X)', fontsize=14)
regression_plot.set_ylabel('Gross Emission Reduction Rate - Baseline (Y)', fontsize=14)

plt.text(5, 56, "R:  "+ str(round(correlation_coefficient,2)), ha='center', va='center', fontsize=12)
plt.text(5, 54, "R_square:"+ str(round(Rsquared,2)), ha='center', va='center', fontsize=12)
plt.text(3.5, 45, "Y =" + str(round(a[0],3)) + " + "+ str(round(b[0][0],3)) + " X", ha='center', va='center', fontsize=12)
plt.text(5.5, 25, "for X = 6.9 we get Y =" + str(round(lm.predict([[6.9]])[0][0],2)), ha='center', va='center', fontsize=12)

plt.show()







