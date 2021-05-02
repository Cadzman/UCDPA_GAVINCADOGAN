import pandas as pd
import numpy as np
import numpy as np



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


print(Applesalesrevenue[["iPhone_SALES", "iPhone_REV", "YOY growth_REV"]].agg([iqr, np.median, np.mean, np.min, np.max]))

