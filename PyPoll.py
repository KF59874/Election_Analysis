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

# 1. Initialize the total vote counter. (Look for #2.)
total_votes=0 

# A. Declare new list 
candidate_options=[]

#B. Declar the empty dictionary 
candidate_votes={} 

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and READ 'r' the file
with open(file_to_load) as election_data: #Usually it would be with open(file, 'r') but instead
    #We will use the module for csv to read the file
    #Read the file object with the reader function for csv
    file_reader=csv.reader(election_data)

# For our analysis, we will NOT need the first row of the data because it is just the header 
# Use the next () function to skip over the first line 

    #Read and print the header row 
    headers = next(file_reader)
    #print(headers)
    
    # Print each row in the csv file
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

        #Print the candidate name from each row
        candidate_name=row[2]

        if candidate_name not in candidate_options:

           # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that condidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)