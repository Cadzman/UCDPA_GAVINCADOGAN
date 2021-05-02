#purpose here is to use .loc without disrupting the rest of my code and using a double index

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
Netflix_ind = Netflix.set_index("show_id")
#Netflix_ind  =Netflix.set_index(["type", "title"])
#Netflix_ind  = Netflix.set_index(["director"])
#Netflix_ind  = Netflix.set_index(["type", "release_year"])
#Netflix_ind = Netflix.set_index(["release_year"])

print(Netflix_ind.index)


#indexing 1
#print(Netflix_ind.head(5),Netflix_ind.shape)


#sorting
netsorind = Netflix_ind.sort_values(["show_id"], ascending=[True])
#netsorind=Netflix_ind.sort_values(["type","release_year"], ascending=[True, True])
#netsorind = Netflix_ind.sort_values(["type", "release_year", "title",], ascending= [True, False, True,])

print(netsorind.head(10))

# Subset rows from India, Hyderabad to Iraq, Baghdad
print(netsorind.iloc[0,2000]


