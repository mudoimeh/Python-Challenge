import os
import csv

# Open the CSV File
election_csvpath = os.path.join("Resources", "election_data.csv")

  #Initialize variables
voter_id=[]
candidates=[]

#Read the CSV file
with open(election_csvpath, newline ='') as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter=",")

    print(csv_reader)

 # Read the header row first (skip this step if there is no header)
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

    #Count the Total number of voters
    for row in csv_reader:
        voter_id.append(row[0])
        candidates.append(row[2])

voter_count=len(voter_id)
candidates_names = set(candidates)
count_votes=0

#print(candidates_names)

candidates_list = list(candidates_names)
print(candidates_list)
counter_candidate=[]
perc_candidate=[]
for i in range(len(candidates_list)):
    counter_candidate.append(candidates.count(candidates_list[i]))
for i in range(len(candidates_list)):    
    perc_candidate.append(round(counter_candidate[i]*100/voter_count))
sorted_PERC=sorted(counter_candidate, reverse=True)

sorted_index=[]
for i in range(len(candidates_list)):
    for j in range(len(candidates_list)):
        if (sorted_PERC[i] == counter_candidate[j]):
           sorted_index.append(j)
           print(f"{candidates_list[j]} {perc_candidate[j]} ({counter_candidate[j]})")
           
print(candidates_list[sorted_index[0]])
#print(candidates_list[int(sorted_index)] )
#print(perc_candidate)  
#print(counter_candidate)    
#print(voter_count)
#print(candidates_list)