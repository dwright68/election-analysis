import csv
import os


#Assign a variable for the files to load/save and the path
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = "analysis\election_analysis.txt"
#Open the election results and read the file
with open(file_to_load) as election_data:
    #To do: read and analyze the election
    file_reader = csv.reader(election_data)
    #print the header row
    headers = next(file_reader)
    #print reach row in the CSV file
    for row in file_reader:
        print(row)
