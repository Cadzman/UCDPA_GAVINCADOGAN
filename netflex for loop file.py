import pandas as pd

Netflix = pd.read_csv("ucdprojectgc/netflix_titles.csv")

print(type(Netflix))
print(Netflix.head(5),Netflix.shape)



Netclean= Netflix.dropna()
print(Netflix.shape,Netclean.shape)
missing_val_count2 = Netclean.isnull().sum()
print(missing_val_count2[0:12])



Netflix_ind = Netclean.set_index("release_year")
print(Netflix_ind.head(5),Netflix_ind.shape)


netsorind = Netflix_ind.sort_values(["type","release_year","title"], ascending=[True, False,True])
netsordinmovies = netsorind[(netsorind["type"] == 'Movie')]



for index , row in netsordinmovies.iterrows():
    print("In the year " + str(index),  row['title'] + " was released in ( ", row['country'], ") and was originally rated " ,row['rating'])






#netsorind["summary"] = netsorind.append(["summary"])
#print(netsorind.shape())

#get this into an additiona column
#remember that this still has tv shwos ....do i remove them before proceeding ?

#summary = []

#print("Median height of goalkeepers: " + str(np.median(gk_heights)))  ....row['rating']