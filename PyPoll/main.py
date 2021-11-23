#PYPOLL

# Import the libraries
import csv
import os

# Files to load and output
file_to_load = os.path.join("../Resources/PyPoll_Resources_election_data.csv")

#Create variables and establish votes as a dictionary.
total_votes = 0

votes = {}

# Read CSV, and skip the header.
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)

#Create an if statement to accumulate/tally the votes for each candidate and find the total vote.
    for row in reader:
        
        if row[2] in votes: 
            votes[row[2]] += 1
        else: 
            votes[row[2]] = 1  
        
        total_votes += 1

#Create variables for the winner and highest vote count.        
winner = ""
highest_count = 0

print("Election Results")
print("----------------")
print(f"Total Votes: {total_votes}")
print("----------------")


#Create a conditional to find the winner and their vote count in the dictionaries.
for vote in votes:
      
    if votes[vote] > highest_count:
        winner = vote
        highest_count = votes[vote]

#Find what percentage of the total vote each candidate received and format accordingly.
#Indent the first f-string to ensure all of the information in the if statment flows to it.
    vote_ratio =  votes[vote]/total_votes
    vote_percent = "{:.3%}".format(vote_ratio)
    print(f"{vote}: {vote_percent}% ({votes[vote]})")

print("----------------")
print(f"Winner: {winner}")
