
#Get the total number of votes
#complete list of candidates who received votes
#the percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular votes


import csv
import os
# Open the election results and read the file
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")
total_votes = 0
candidate_options = []
candidate_votes= {}
vote_percentage = []
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(file_to_load) as election_data:
     file_reader = csv.reader(election_data)

     #Read the header row.
     headers = next(file_reader)

     #Print each row in the CSV file
     for row in file_reader:
          candidate_name = row[2]
          total_votes = total_votes+1
          if candidate_name not in candidate_options:
               candidate_options.append(candidate_name)
               candidate_votes [candidate_name] = 0
               candidate_votes [candidate_name] +=1
          candidate_votes [candidate_name] +=1
with open(file_to_save,"w") as txt_file:
     election_results = (
          f"\nElection Results\n"
          f"-------------------\n"
          f"Total Votes: {total_votes:,}"
          f"\n-------------------\n")
     print(election_results, end="")
     txt_file.write(election_results)
     for candidate_name in candidate_votes:
          votes = candidate_votes[candidate_name]
          vote_percentage = float(votes)/float(total_votes)*100
          candidate_results = (f"\n{candidate_name}: received {vote_percentage:.1f}% of the vote.\n")
          if (votes > winning_count) and (vote_percentage>winning_percentage):
               winning_count = votes
               winning_percentage = vote_percentage
               winning_candidate = candidate_name
          winning_candidate_summary = (f"\n The winner of the election is {winning_candidate}" f" and the winner scored {winning_count} votes " 
          f"which consists {vote_percentage} % of the results")
          txt_file.write(candidate_results)
     txt_file.write(winning_candidate_summary)
     #print(f"{winning_candidate}: wins and have received {winning_percentage:.1f}% of the vote.")
#print(candidate_votes)
#print(candidate_options)
#print(candidate_votes)

     candidate_votes[candidate_name]+=1