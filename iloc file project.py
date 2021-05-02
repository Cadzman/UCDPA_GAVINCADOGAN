import pandas as pd


pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 12)
pd.set_option('display.width', 1000)


Netflix = pd.read_csv("ucdprojectgc/netflix_titles.csv")


Netflix_ind = Netflix.set_index("show_id")

print(Netflix_ind.index)

print(Netflix_ind.head(10))

print(Netflix_ind.iloc[0:200])

What if i put this into the original before i set index to year ?