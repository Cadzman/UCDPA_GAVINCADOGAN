import pandas as pd



pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


Netflix = pd.read_csv("ucdprojectgc/netflix_titles.csv")

print(type(Netflix))
print(Netflix.head(5),Netflix.shape)



#set index

#Netflix_ind = Netflix.set_index("show_id")
Netflix_ind  =Netflix.set_index(["type", "title"])

#indexing 1
print(Netflix_ind.head(5),Netflix_ind.shape)


#sorting
netsorind = Netflix_ind.sort_values(["type","release_year","title"], ascending=[True, False,True])


print(netsorind.head(50))


#Subset 1 -  Subset of irish and UK movies
countries = [("Ireland", "United Kingdom")]
IrelandUK = netsorind[netsorind["country"].isin(countries)]
#print(IrelandUK)



IrelandUKMovies = netsorind[(netsorind["country"] == ["Ireland"]) or (netsorind["country"] == ["France"])]
#print(IrelandUKMovies)
#it works for first bit , is it that you cant filter by index, can do both seperately, what if do them one by one , & (netsorind["type"] == "Movie")]


df['country'].value_counts()

# Subset of irish and UK movies
#countries = [("Ireland", "United Kingdom")]
#Years = [(2006, 2007, 2008, 2009)]
#IrelandUK = netsorind[netsorind["country"].isin(countries)]
#IrelandUK = netsorind.loc[countries]
#Last15 =\
#print(netsorind.loc[Years])
#print(Last15)

#Print (IrelandUK)

# Subset temperatures_ind using .loc[]  , AN EASIER WAY
#***print(netsorind.loc[countries]).....

#groups - does this work because of the sort - use .agg ??

#NetM = netsorind[netsorind["type"]=='Movie'].groupby('release_year').count()
#Nettv = netsorind[netsorind['type']=='TV Show'].groupby('release_year').count()


#print(netsorind[NetM])


#Filtering data for information - all moved from the uk released in 2009
#IrelandUK = netsorind[(netsorind[])]






# Create indiv_per_10k col as homeless individuals per 10k state pop
#homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"] / homelessness["state_pop"]

# Subset rows for indiv_per_10k greater than 20
#high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]

# Sort high_homelessness by descending indiv_per_10k
#high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
#result = high_homelessness_srt[["state", "indiv_per_10k"]]

# See the result
#print(result)




# Subset of irish and UK movies
#countries = ["Ireland", "United Kingdom"]
#IrelandUK = netsorind[netsorind["country"].isin(countries)]
#print(IrelandUK)


# Subset temperatures_ind using .loc[]  , AN EASIER WAY
#***print(netsorind.loc[countries]).....


