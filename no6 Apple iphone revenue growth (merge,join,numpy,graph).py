import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt



pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 12)
pd.set_option('display.width', 1000)


Applesales = pd.read_csv("ucdprojectgc/apple--iphone-unit-sales (1) copy.csv")
Applerevenue = pd.read_csv("ucdprojectgc/apple--iphone-revenue.csv")





Applesalesrevenue = Applesales.merge(Applerevenue, on="Category", suffixes=('_SALES','_REV'))
Applesalesrevenue = Applesalesrevenue.set_index(["Category"])
print(Applesalesrevenue)




def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
#hue="location"

print(Applesalesrevenue[["iPhone_SALES", "iPhone_REV", "YOY growth_REV"]].agg([iqr, np.median, np.mean, np.min, np.max]))




#sns.regplot(data=Applesalesrevenue, - couldnt get regplot to work
#            x="Category",
#            y="YOY growth_SALES")

#sns.set_style('whitegrid')

sns.set_context('notebook')
sns.set_style('dark')
sns.set(color_codes=True)
for p in['bright', 'colorblind']:
    sns.set_palette(p)

fig, ax = plt.subplots()

sns.scatterplot(data=Applesalesrevenue,
            x="Category",
            y="iPhone_REV", color ='m')

ax.set(xlabel="Financial Quarter",
       ylabel = "Iphone Revenue - $hundred millions",
       title = "Growth in iphone Revenue"
       )

plt.xticks(rotation=90)
sns.despine()
plt.show()


