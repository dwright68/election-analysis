import csv
import os


#Assign a variable for the files to load/save and the path
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = "analysis\election_analysis.txt"
#create vote count variable and set to 0
total_votes = 0
#add candidate variable
candidate_options = []
#add empty dictionary 
candidate_votes ={}
#winning candidate and count tracker 
winning_count = 0
winning_percent = 0
winning_candidate =""

#Open the election results and read the file
with open(file_to_load) as election_data:
    #To do: read and analyze the election
    file_reader = csv.reader(election_data)
    #read the header row
    headers = next(file_reader)
    
    #add up total votes
    for row in file_reader:
        total_votes +=1
    
    #print the candidate name from each row, then add the candidate name to the list
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
             # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
            #start counting votes    
        candidate_votes[candidate_name] +=1

    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        #get vote count of each candidiate
        votes = candidate_votes[candidate_name]  
        #calculate the votes
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #determine winning candidate
        if (votes > winning_count) and (vote_percentage > winning_percent):
            winning_count = votes
            winning_percent = vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percent:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)