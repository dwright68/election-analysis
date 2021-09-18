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
            
    
    #print vote count
    print(candidate_votes)
