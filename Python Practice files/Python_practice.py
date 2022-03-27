print("Hello World")

# help("keywords") will show all the pre-programmed keywords in Python

# Important Note: Lists are mutable -- can be adjusted/changed

# define the list 'counties' 
counties = ["Arapahoe", "Denver", "Jefferson"]

# an empty list would be as follows: my_list = []

print(counties)

# the order of the items depend on their starting number, the first item is always denoted as (0). So here (0) = "Araphoe"
print (counties [0])

# you can also get the position of the item from the last item in the list using negative indexed. (-1) = "Jefferson" 
# Indexes are used to identify the last item's position relative to the end of the list 
print (counties[-1])

# 2nd last item in the list = [-2]
print (counties[-2])

#Length of a list 
print(len(counties))

# Slicing = list[start:end]
print (counties[0:-2])
print(counties[:-1])
print(counties[:3])

#Add items to a list by using append(). This will add the new item to the end of the list.
counties.append("El Paso")

print(counties)

# To add an item to a list but NOT at the end, use: list.insert(index,obj)
counties.insert(2, "El Paso")
print(counties)
print(len(counties))

# To remove an item from a list 
counties.remove("El Paso") 
#this gets rid of the first item that matches the exact spelling of the item
# El Paso is still in the list b/c there are two exact same items

print(counties)

# Remove using pop () method -- good for when need to know which position was removed
counties.pop(3)
print(counties)

#To change an element in the list -- use the position of the item you'd like to replace
counties[2]="El Paso"
print(counties)

# Moving on to tuples -- These CANNOT be adjusted/changed -- they are immutable

counties_tuple =("California", "Virginia", "New York")

print(len(counties_tuple))

# Slicing and indexing is the same as for lists - use [] to denote the position number
# Remember: first position = 0

#Creating a dictionary 
counties_dict={}

# adding amount of voters for each county 
counties_dict["Arapahoe"]= 422829

print(counties_dict)

#SIDENOTE: {} - integers, () tuple, [] for string 

counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

print(counties_dict)

print(len(counties_dict))

#items in a DICTIONARY = CANNOT use items() in a list  
print(counties_dict.items())

# Get all values 
print(counties_dict.values())

#Getting a specific value
print(counties_dict.get("Denver"))

# key feature to get a value 
print(counties_dict["Arapahoe"])

# List of dictionaries 
voting_data =[]
voting_data.append({"county":"Arapahoe", "registered_voters":422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

print(voting_data)

voting_data.insert(1, {"county":"El Paso","registered_voters":461149})
voting_data.remove({"county":"Arapahoe", "registered_voters":422829})

print(voting_data)


# Hello this is a test run to see if I can push to Git 