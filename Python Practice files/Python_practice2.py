# define the list 'counties' 
counties = ["Arapahoe", "Denver", "Jefferson"]

# Let's look at conditions and if statements
if counties [1] == 'Denver' :
        print (counties[1])

# To explain - == is used to denote Boolean operator = "equals to"
# == has to be used b/c '=' is already used when defining lists etc 
# : is used at the end of the condition 
# Also only one tick '' is used to define conditionals not two ""

# > greater than 
# >= greater than or equal to 
# < less than
# <= less than or equal to 
# == equal to 
# != not equal to 

# if counties [3]!='Jefferson':
  #      print(counties[2])
        # this will return as out of range because the len(counties)=3

# If-Else Statements
# This is used when we need an output for true and false conditions
# hence also reffered as **dual-alternative decision statement**


# if condition:
  # statement 1
  # statement 2
# else:
  # statement 1
  # statement 2

# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
  #  print("Turn on the AC.")
# else:
  #  print("Open the windows.")


# Nested IF STATEMENTS

# #What is the score?
# score = int(input("What is your test score? "))

# # Determine the grade.

# if score >= 90:                         # test the condition
#     print('Your grade is an A.')
# else:                                   # compound to make the elif statement
#     if score >= 80:
#         print('Your grade is a B.')
#     else:
#         if score >= 70:
#             print('Your grade is a C.')
#         else:
#             if score >= 60:
#                 print('Your grade is a D.')
#             else:
#                 print('Your grade is an F.')

if "El Paso" in counties:
        print("El Paso is in the list of counties.")
else:  
        print("El Paso is not in the list of counties.")



if "Arapahoe" in counties and "El Paso" in counties:
        print("Araphaoe and El Paso are in the list of counties")
else: 
        print("Arapahoe and El Paso are not in the list of counties")



