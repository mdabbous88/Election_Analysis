# Election_Analysis
1.Overiew of election audit:
The purpose of this analysis is to use election data provided in a CSV file to determine the total number of votes in 3 counties in Colorado (Denever, Arapahoe and Jefferson) , voter turnout for each county and their percentages, as well as the largest county turnout and each candidate percentage of votes and their percentages. Lastly, determine the results of the election (winning candidate, number of votes the winner scored and the percentage of the winner's votes). This analysis is required to be sent to the election commission.

2.Election outcomes:(link:https://github.com/mdabbous88/Election_Analysis/blob/main/Election%20Results.png)
* Number of votes casted in this election is 369,711
* County Votes:
    Jefferson: 10.5% (38,855)
    Denver: 82.8% (306,055)
    Arapahoe: 6.7% (24,801)
* County with the largest number of votes: Denver
* Number of votes each candidate received:
    Charles Casper Stockham: 23.0% (85,213)
    Diana DeGette: 73.8% (272,892)
    Raymon Anthony Doane: 3.1% (11,606)
* The winner candidate was Diana DeGette, she received 272,892 votes which represents 73.8% of total votes

3.Election-Audit Summary:
This script can be generalized for any other election. The script can be turned into a function with inputs that apply to any election. Name example could be election_analysis(input).
Example 1: The file to load can be as input, this input can be used in the code file_to_load = os.path.join("..","Resources", input).
Example 2: The output file can be also generalized for any district or state. This will be in the return of the function
return outputfile where output file is file_to_save

