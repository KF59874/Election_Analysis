# Repetition structure or 'Loops'

# While loops - example: 'Do you want to continue shopping after adding an item to the basket?'
x=0 
while x<= 5:
    print(x)
    x=x+1

# For loops 
# run through a program a specific number of times before they stop
# for loops can be written as if and if else statements

counties = ["Arapahoe", "Denver", "Jefferson"]
for county in counties:
    print(county)

numbers =[0,1,2,3,4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

# indexing can also be used, but we must change the string data type to integers
for i in range(len(counties)):
    print(counties[i])

#defining a dictionary 
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438} 

#to iterate throuhg a dictionary and get the keys of a dictionary 
for county in counties_dict:
    print(county)

# Get values of a dictionary

for voters in counties_dict.values():
    print(voters)

# To have keys and values printed in the same line, use the following script
for county, voters in counties_dict.items():
    print(county, voters)

