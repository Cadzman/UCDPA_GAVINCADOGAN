import pandas as pd





pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 12)
pd.set_option('display.width', 1000)


Netflix = pd.read_csv("ucdprojectgc/netflix_titles.csv")


#Netflix["duration"] = pd.to_numeric(Netflix["duration"])
#Netflix[['Minutes','minutes2']] = Netflix['duration'].split(" ")

#df['principal_country'] = df['country'].apply(lambda x: x.split(",")[0])
#df['principal_country'].head()

#Netflix['minutes'] = Netflix["duration"].apply(lambda x: x.split(" ")[0])
#print(Netflix['minutes'])
#Netflix['movie_duration'] = Netflix['minutes'](Netflix['minutes'] == "movie").astype(int)


#print(type(Netflix))
#print(Netflix.head(5),Netflix.shape,Netflix.info(),Netflix.describe())

#pd.to_numeric('duration')
#Netflix["duration"] = pd.to_numeric(Netflix["duration"])


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


#Cleaning data- count missing values in each column  -
missing_val_count = netsorind.isnull().sum()
print(missing_val_count[0:12])
#drop rows where data is missing
#droprows= netsorind.dropna()
#print(netsorind.shape,droprows.shape) #is this too many rows
# Cleaning data fill missing values with 0 - didnt want to
netclean = netsorind.fillna(method='bfill', axis=0).fillna("0")
#Cleaning data- count missing values in each column after filling blanks
missing_val_count2 = netclean.isnull().sum()
print(missing_val_count2[0:12])


#creation of seperate dataframes - North america, europe english speaking
countries = ["Ireland", "United Kingdom"]
IrelandUK = netclean[(netclean["country"].isin(countries)) & (netclean["type"]== 'Movie')]
IrelandUK = (IrelandUK.loc[2001:2021])
#print(IrelandUK.head(5))

northamerica_countries = ["Mexico" , "United States", "Canada"]
northamerica = netclean[(netclean["country"].isin(northamerica_countries)) & (netclean["type"]== 'Movie')]
northamerica = (northamerica.loc[2001:2021])
#print(northamerica)


#print(northamerica.head(5))

Frenchcinema = ["France"]
Frenchmovies = netclean[(netclean["country"].isin(Frenchcinema)) & (netclean["type"]== 'Movie')]
Frenchmovies = (Frenchmovies.loc[2001:2021])
print(Frenchmovies.head(5))


#Frenchmovies2 =


#print(netclean.loc[2001:2021])

#print(northamerica.loc[2001:2021])


# Subset temperatures using square brackets
#print(temperatures[temperatures["city"].isin(cities)])

# Subset temperatures_ind using .loc[]  , AN EASIER WAY
#print(temperatures_ind.loc[cities])


#Slicing, loc or iloc

#print(IrelandUK.loc[2001:2021]








#netclean['newminutes'] = netclean(netclean["minutes"] + 5)

#movies_length = netclean[(netclean["duration"] + 1)]
#print(movies_length)

#int(x)


#longmovies = netclean[(netclean["minutes"] > 100)]
#Longmoviessrt = longmovies.sort_values("minutes", ascending = False)
#print(netclean['longmovies'])
#print(longmovies)
#print(netclean.dtype(netclean['minutes'])




#nethcedn = netclean[["director", "release_year"]]
#print(nethcedn)  #result is type titlle director year - Successful

#IrelandUK = netclean[(netclean["country"] == "Ireland") | (netclean["country"] == "United Kingdom")]  #THIS WORKS - SUCCESSFUL, but why cant this be done in one ?
#IrelandUKMovie = IrelandUK[(IrelandUK["type"] == "Movie")]
#print(IrelandUKMovie)






# The Mojave Desert states  ****** creation of a list
#canu = ["California", "Arizona", "Nevada", "Utah"]
#countries = [("Ireland", "United Kingdom")]
# Filter for rows in the Mojave Desert states
#mojave_homelessness = homelessness[homelessness["state"].isin(canu)]
#IrelandUK2 = netclean[[netclean["country"].isin(countries)]

#print(IrelandUK2.head())


#colors = ["brown", "black", "tan"]
#condition = dogs["color"].isin(colors)
#dogs[condition]


#print(netsorind[IrelandUK])
#this is returning blank values across other columns not having desired filter effect

#south_mid_atlantic = homelessness[(homelessness["region"] == "South Atlantic") | (homelessness["region"] == "Mid-Atlantic")]

# Subset for rows in South Atlantic or Mid-Atlantic regions
#south_mid_atlantic = homelessness[(homelessness["region"] == "South Atlantic") | (homelessness["region"] == "Mid-Atlantic")]

# The Mojave Desert states  ****** creation of a list
#canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
#mojave_homelessness = homelessness[homelessness["state"].isin(canu)]


#countries = [("Ireland", "United Kingdom")]
#Years = [(2006, 2007, 2008, 2009)]
#IrelandUK = netsorind[netsorind["country"].isin(countries)]
#IrelandUK = netsorind.loc[countries]


#•	Use functions to create reusable code. [1]
#•	Numpy. [1]
#•	Dictionary or Lists. [1]

practice_list = [1,2,3,3,4,5,5,5,5,5,12]
median1 = np.median(practice_list)
print(median1)

release_yearnp = netclean['release year'].to_list()
print(release_yearnp)

#release_year_array = release_year.values
#median = np.median(release_year_array)
#print(median)

#print(np.median(release_year))

# Print out the median height of goalkeepers. Replace 'None'
#print("Median year of movie releases: " + str(np.median(netclean['release_year'])))



Movies= netclean[netclean['type']=='Movie'].groupby('release_year').count().sum()
#Movies= netclean[netclean['type']=='Movie'].groupby('release_year').count()
TV_Show = netclean[netclean['type']=='TV Show'].groupby('release_year').count().sum()

print(Movies)
print(TV_Show)
print(TV_Show["show_id"])
print(Movies["show_id"])
Movie_total = Movies["show_id"]
Tv_Total = TV_Show["show_id"]

gap = Movie_total - Tv_Total
print(gap)

#def difference(column):
  #  return Movie_total - Tv_Total

#print(netclean['release_year'].difference)

# Print out the median height of goalkeepers. Replace 'None'
#print("Median height of goalkeepers: " + str(np.median(gk_heights)))


# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
#print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))

#etflix_stats = netclean.groupby("type")[["release_year"]].agg([difference(), np.median])


#Getting empty dataframe for tv
#Netflix_stats = netclean.groupby("type")[["release_year"]].agg([np.min, np.max, np.mean, np.median])
#print(Netflix_stats)

#Instead of passing just iqr to .agg(), pass a list of functions without parentheses to .agg().

# Import NumPy and create custom IQR function  ****1 create function 2
import numpy as np

#def iqr(column):
#    return column.quantile(0.75) - column.quantile(0.25)




# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
#print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))

 #       temperature_c  fuel_price_usd_per_l  unemployment
#iqr            16.583                 0.073         0.565
#median         16.967                 0.743         8.099

#get that iqr shite aswell

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median  ****** what grouping  by , what basing it off , and then the calculations
#unemp_fuel_stats = sales.groupby("type")[["unemployment", "fuel_price_usd_per_l"]].agg([np.min, np.max, np.mean, np.median])

# Print unemp_fuel_stats
#print(unemp_fuel_stats)



