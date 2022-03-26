# Pseudo coding is as follows: 

# The data we need to retrieve.

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes 
# 3. The percentage of votes each candidate won 
# 4. The total number of votes each candidate won 
# 5. The winner of the election based on popular vote
# ___________________________________________________________________________


# to open a file in python: 
# file_variable = open(filename,mode)
#     mode will denote what we will be doing with the file:
#     r - read 
#     w - open a file to write
#     x - exclusive creation 
#     a - append data to an existing file 
#     + - opens a file for reading and writing

# using DIRECT path to open the election results 
# file_to_load = 'Resources\election_results.csv'

# # Open the election results and read the file 
# electon_data = open(file_to_load, 'r')

# # to do: perform analysis

# # Close the file - important to do this to not alter text any furhter
# election_data.close()

# Instead of using open and close we can simply use the with statement 

# Open the election results and read the file 
# with open(file_to_load) as election_data:
#     #to do: perform analysis.
#     print(election_data)


# Using INDIRECT path to access the csv file using the os module which allows us to interact with our operating system
# import os 
# dir(os)
# dir(os.path)

#Import csv and os for commands
# ADD DEPENDENCIES 
# import csv
# import os 

#activate variable to reference the path to load the file
# file_to_laod=os.path.join("Resources","election_results.csv")

# with open(file_to_load) as election_data : 
#     #Print the file object NOTE: there must be an indent here o/w with won't work
#     print(election_data)

# To write the results of our analysis, we need to refer to a text file 
# Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Create a variable and then use the open() function with the "w" mode to write data to the file
# outfile = open(file_to_save, "w")

# Let's write some data 
# outfile.write("Hello World")

# Close out the file 
# outfile.close()

# Let's now instead use the with statement because why would you make things simpler from the beginngin

#Create a filename variable to connect to txt file 
# file_to_save = os.path.join("Analysis","election_analysis.txt")

# #Using with statment open the file as a text file
# with open(file_to_save,"w") as txt_file:
#     #Write some data to the file
#     txt_file.write("Counties in the Election\n--------------------------------\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson") #\n will push the next key to the next line when all data is combined


# _________________________________________________________________________________

# Now to read the election results 

#___________________________________________________________________________________

# Add dependencies
import csv
import os 

# Assign a variable to load the file from a path 
file_to_load=os.path.join("Resources","election_results.csv")

#Assign a variable to write data to txt 
file_to_save = os.path.join("Analysis","election_analysis.txt")

#Open the election results and READ 'r' the file
with open(file_to_load) as election_data: #Usually it would be with open(file, 'r') but instead
    #We will use the module for csv to read the file
    #Read the file object with the reader function for csv
    file_reader=csv.reader(election_data)

# Print each row in the csv file
    # for row in file_reader:
    #     print(row)

# For our analysis, we will NOT need the first row of the data because it is just the header 
# Use the next () function to skip over the first line 

    #Read and print the header row 
    headers = next(file_reader)
    print(headers)
    

