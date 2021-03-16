#Open election_results.csv
#Get the total number of votes
#complete list of candidates who received votes
#the percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular votes


import csv
import os
# Open the election results and read the file
file_to_load = os.path.join("Election Analysis","Resources", "election_results.csv")
with open(file_to_load) as election_data:
     # To do: perform analysis.
     print(election_data)