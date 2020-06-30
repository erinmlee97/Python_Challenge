#What we want to find
    #The total number of votes cast
    #A complete list of candidates who recieved votes
    #The percentage of votes each candidate won
    #The total number of votes each candidate won
    #The winner of the election based on popular vote

#Import modules
import os
import csv

#My Variables
VoteTotal = 0

#Set path for files
csvpath = os.path.join("Resources", "election_data.csv")
writepath= os.path.join("analysis", "election_data.text")

#Open the CSV file
with open (csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

     #Skip the header
    csvheader = next(csvreader, None)

    #Loop through csv file
    for row in csvreader:

        #Find the total numbers of votes cast
        VoteTotal = VoteTotal + 1

        #List of candidates who received a vote


    print(f"Total Votes: {VoteTotal}")

