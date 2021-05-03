import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt



pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 12)
pd.set_option('display.width', 1000)


Netflix = pd.read_csv("ucdprojectgc/netflix_titles.csv")

#set index
#Netflix_ind = Netflix.set_index("show_id")
#Netflix_ind  =Netflix.set_index(["type", "title"])
#Netflix_ind  =Netflix.set_index(["type", "release_year"])
Netflix_ind = Netflix.set_index(["release_year"])

print(Netflix_ind.index)


#indexing 1
#print(Netflix_ind.head(5),Netflix_ind.shape)


#sorting
#netsorind = Netflix_ind.sort_values(["show_id"], ascending=[True])
netsorind=Netflix_ind.sort_values(["release_year"], ascending=[True])
#netsorind = Netflix_ind.sort_values(["type", "release_year", "title",], ascending=[True, False, True,])

#print(netsorind.head(10))



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


#print(northamerica.head(5))

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


plt.figure(figsize = (35,10))
#sns.countplot(x="type", data= netclean)
#plt.show()


#*****sns.countplot(x="release_year", data=Netflixmovies)
#*****plt.xticks(rotation=90)

#sns.countplot(x="release_year", data= )

#fig, ax = plt.subplots()

#netclean[(netclean["country"].isin(countries)) & (netclean["type"]== 'Movie')].hist()


#sns.catplot(x="type", data= netclean)
#plt.show()

#sns.catplot(x='release_year', data= netclean, kind= "count")

#ax2....index
sns.countplot(y='country',data=Netflixmovies, order = Netflixmovies['country'].value_counts().head(5).index)
plt.title("Number of movies produced by each country")

plt.show()


#sns.catplot(x="type" )


# Create a point plot with subgroups
#[sns.catplot(x="romantic", y="absences",
#			data=student_data,
 #           kind="point",
  #          hue="school")

# Show plot
#plt.show()

# Turn off the confidence intervals for this plot
#sns.catplot(x="romantic", y="absences",
	#		data=student_data,
     #       kind="point",
      ##      hue="school",
        #    ci=None)]

