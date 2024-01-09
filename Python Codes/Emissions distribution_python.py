# dataset = pandas.DataFrame(Fiscal Year, Emissions)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(x = dataset['Emissions'],kde = True)
plt.show()
