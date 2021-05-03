import pandas as pd

pd.set_option("set_max_rows",100)
pd.set_option("set_max_columns",100)
pd.set_option("set_width ",100)

stack overflow


data = pd.read_csv("****.csv")

print(data.head(5),data.shape)



house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs (5 items)
downstairs = areas[0:6]

# Use slicing to create upstairs (includes UPTO 10 BUT NOT 10 so really the 9th)
upstairs = areas[6:10]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
['hallway', 11.25, 'kitchen', 18.0, 'living room', 20.0]
['bedroom', 10.75, 'bathroom', 9.5]



If you can change elements in a list, you sure want to be able to add elements to it, right? You can use the + operator:

x = ["a", "b", "c", "d"]
y = x + ["e", "f"]


# Create the areas list (updated version)
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]

append(), that adds an element to the list it is called on,
remove(), that removes the first element of a list that matches the input, and
reverse(), that reverses the order of the elements in the list it is called on.

Use int() to convert var2 to an integer. Store the output as out2.

Call the type() function like this: type(var1)





# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])
****
# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])

US     United States
AUS        Australia
JPN            Japan




# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])
cars_per_cap      588
country         Japan
drives_right    False
Name: JPN, dtype: object

     cars_per_cap    country  drives_right
AUS           731  Australia         False
EG             45      Egypt          True



# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])


Print out a sub-DataFrame, containing the observations for Russia and Morocco and the columns country and drives_right


True
     country  drives_right
RU    Russia          True
MOR  Morocco          True



# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area > 10 :
    print("medium size, nice!")
else :
    print("pretty small.")






To subset rows at the outer level, use .loc["country1":"country2"].
To subset rows at the outer level, use .loc[("country1", "city1"):("country2", "city2")].
To subset in both directions, pass two arguments to .loc[]


# Subset for Egypt to India
temp_by_country_city_vs_year.loc["Egypt":"India"]

# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[("Egypt", "Cairo"):("India", "Delhi")]

# Subset in both directions at once
temp_by_country_city_vs_year.loc[("Egypt", "Cairo"):("India", "Delhi"), "2005":"2010"]

year                    2005    2006    2007    2008    2009    2010
country  city
Egypt    Cairo        22.006  22.050  22.361  22.644  22.625  23.718
         Gizeh        22.006  22.050  22.361  22.644  22.625  23.718




# Index temperatures by city
temperatures_ind = temperatures.set_index("city")

# Look at temperatures_ind
print(temperatures_ind)

# Reset the index, keeping its contents
print(temperatures_ind.reset_index()) ***???

# Reset the index, dropping its contents
print(temperatures_ind.reset_index(drop=True)) ***???


           date     city        country  avg_temp_c
0     2000-01-01  Abidjan  Côte D'Ivoire      27.293
1     2000-02-01  Abidjan  Côte D'Ivoire      27.685






# Index temperatures by country & city
temperatures_ind = temperatures.set_index(["country", "city"])  *****

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [("Brazil", "Rio De Janeiro"), ("Pakistan", "Lahore")]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])






5.3.2 - Subsetting with .loc[]

The killer feature for indexes is.loc[]: a subsetting method that accepts index values.When you pass it a single argument, it will take a subset of rows.

The code for subsetting using.loc[] can be easier to read than standard square bracket subsetting,
which can make your code less burdensome to maintain.

# Make a list of cities to subset on
cities = ["Moscow", "Saint Petersburg"]

# Subset temperatures using square brackets
print(temperatures[temperatures["city"].isin(cities)])

# Subset temperatures_ind using .loc[]  , AN EASIER WAY
print(temperatures_ind.loc[cities])




# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values("family_members", ascending=False)

# Print the top few rows
print(homelessness_fam.head())

Sort homelessness first by region (ascending), and then by number of family members (descending). Save this as homelessness_reg_fam.

# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(["region", "family_members"], ascending=[True, False])




 Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level=["country", "city"], ascending = [True, False]))