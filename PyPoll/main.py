# Import os and csv read modules
import os
import csv
from collections import Counter
import sys

# Define path to file locations
csv_path = os.path.join('Resources', 'election_data.csv')
csv_analysis = os.path.join('analysis', 'analysis.txt')

# Create separate lists to hold column data
ballotID = []
county = []
candidate = []

# Open csv file
with open(csv_path,'r') as election_file:
    election_data = csv.DictReader(election_file, delimiter=",")

# Loop through the data and append data from each column to its own list
    for record in election_data:
        ballotID.append(float(record["Ballot ID"]))
        county.append(str(record["County"]))
        candidate.append(str(record["Candidate"]))

    # Get a list of each unique candidate from the candidate list
    unique_candidate = set(candidate)
    candidate_list = (list(unique_candidate))

    # Print out the calculations
    with open(csv_analysis, 'w') as poll_analysis:
        for x in [sys.stdout, poll_analysis]:

            print("Election Results", file=x)
            print("--------------------------", file=x)
            print("Total Votes: ", len(ballotID), file=x)
            print("--------------------------", file=x)

# Loops through the list of unique candidates and calculates the percent of the vote and total votes
            for candidate_name in candidate_list:
                percent_of_vote = "{:.3%}".format(candidate.count(candidate_name) / len(ballotID), file=x) 

                print(candidate_name, ": ", str(percent_of_vote), "(" + str(candidate.count(candidate_name)) + ")", file=x)      

            print("--------------------------", file=x)

# Prints the candidates who got the most votes
            vote_count = Counter(candidate)
            print("Winner: ", vote_count.most_common(1)[0][0], file=x)
            print("--------------------------", file=x)