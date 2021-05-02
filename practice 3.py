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
#print(IrelandUK.head(5))

northamerica_countries = ["Mexico" , "United States", "Canada"]
northamerica = netclean[(netclean["country"].isin(northamerica_countries)) & (netclean["type"]== 'Movie')]
northamerica = (northamerica.loc[2001:2021])
print(northamerica)


#print(northamerica.head(5))

Frenchcinema = ["France"]
Frenchmovies = netclean[(netclean["country"].isin(Frenchcinema)) & (netclean["type"]== 'Movie')]
#print(Frenchmovies.head(5))


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



#Merge Dataframes - rated 'R' after the release

#IrelandUK , northamerica , Frenchmovies

#irelanduk_northamerica = IrelandUK.merge(northamerica, how='inner', on=('rating'))

#print(irelanduk_northamerica)

# Merge sequels and financials on index id
#sequels_fin = sequels.merge(financials, on='id', how='left')

# Self merge with suffixes as inner join with left on sequel and right on id
#orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel',

