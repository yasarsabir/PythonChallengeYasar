#import dependencies
import os
import csv
import pandas as pd

#assign file to read
csvpath = os.path.join('Resources', 'election_data.csv')

#set variables
count = 0
candidate_list = []
Votes_for_Charles = 0
Votes_for_Diana = 0
Votes_for_Raymon = 0


#open the file and read the data
with open(csvpath) as text: 
    data = csv.reader(text, delimiter=",")

#discard header
    header = next(data)
    first_row = next(data)

#1) COUNT the total number of votes, that is the number of rows in column 1 
    for row in data:
            count  += 1

# 2) Complete the candidate list, an empty candidate list has already been assigned above.
#assign a variable to look through Column C in the database
data_column = row[2]


# Iterate over each item in the data column
for item in data_column:
    # Check if the item is not already in the candidate_list
    if item not in candidate_list:
        # Add the item to the candidate_list
        candidate_list.append(item)

# Print the unique strings
print(candidate_list)
#for row[2] in data:
         #if candidate in row[2] != previous_row   :
            #candidate_list.append(row[2])

# 3) Cacluate the total number of candidates running by finding all the unique values in Column C not including the header.
    
if row[2] == "Charles Casper Stockham":
        Votes_for_Charles  += 1
elif row[2] == "Diana DeGette":
        Votes_for_Diana    += 1
elif row[2] == "Raymon Anthony Doane":
        Votes_for_Raymon   += 1
         
#3) Calculate the percentage of votes each candidate won AND the absolute value 
Percentage_votes_Charles = (Votes_for_Charles/count)*100
Percentage_votes_Diana = (Votes_for_Diana/count)*100
Percentage_votes_Raymon = (Votes_for_Raymon/count)*100

analysis = (f'''
Election Results
-------------------------
Total Votes:  {count}    
-------------------------
Charles Casper Stockham: {Percentage_votes_Charles}% ({Votes_for_Charles})
Diana DeGette: {Percentage_votes_Diana}% ({Votes_for_Diana}))
Raymon Anthony Doane: {Percentage_votes_Raymon}% ({Votes_for_Raymon}))
-------------------------
Winner: Diana DeGette
-------------------------''')
#print the analysis to the terminal
print(analysis)

#write the analysis to the text file
output_path = os.path.join('analysis.txt')
with open(output_path, 'w') as textfile:
    textfile.write(analysis)