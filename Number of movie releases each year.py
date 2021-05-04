import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt



pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 12)
pd.set_option('display.width', 1000)


Netflix = pd.read_csv("ucdprojectgc/netflix_titles.csv")


Netflix_ind = Netflix.set_index(["release_year"])

print(Netflix_ind.index)



netsorind=Netflix_ind.sort_values(["release_year"], ascending=[True])


missing_val_count = netsorind.isnull().sum()
print(missing_val_count[0:12])
netclean = netsorind.fillna(method='bfill', axis=0).fillna("0")
missing_val_count2 = netclean.isnull().sum()
print(missing_val_count2[0:12])


#creation of seperate dataframes - North america, europe english speaking
countries = ["Ireland", "United Kingdom"]
IrelandUK = netclean[(netclean["country"].isin(countries)) & (netclean["type"]== 'Movie')]
#IrelandUK = (IrelandUK.loc[2001:2021])
#print(IrelandUK.head(5))

northamerica_countries = ["Mexico" , "United States", "Canada"]
northamerica = netclean[(netclean["country"].isin(northamerica_countries)) & (netclean["type"]== 'Movie')]
northamerica = (northamerica.loc[2001:2021])
#print(northamerica)



Frenchcinema = ["France"]
Frenchmovies = netclean[(netclean["country"].isin(Frenchcinema)) & (netclean["type"]== 'Movie')]
Frenchmovies = (Frenchmovies.loc[2001:2021])
#print(Frenchmovies.head(5))




country_count = netclean['country'].value_counts().to_frame()
print(country_count)

netclean['date_added'] = pd.to_datetime(netclean['date_added'])
netclean["year_added"] = netclean["date_added"].dt.year
netclean["year_added"].astype('int')


Netflixmovies= Netflix[Netflix["type"]== 'Movie']



sns.set_context('notebook')
sns.set_style('dark')
sns.set(color_codes=True)
for p in['bright', 'colorblind']:
    sns.set_palette(p)

fig, ax = plt.subplots()





plt.figure(figsize = (35,10))
sns.countplot(x="release_year", data=Netflixmovies)
plt.xticks(rotation=90)


plt.suptitle("Films released each year (1942-2021)", fontsize = 18, fontweight='bold')
plt.xlabel("Year", size=14)
plt.ylabel("Number of Titles", size=14)

plt.show()


