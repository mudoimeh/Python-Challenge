import os
import csv

# Open the CSV File
budget_csvpath = os.path.join("Resources", "budget_data.csv")

    #Initialize variables
month_counter=0
profit_loss_total=0
profit_loss_change=[]
profit=[]
profit_date=[]

#Read the CSV file
with open(budget_csvpath, newline ='') as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter=",")

    print(csv_reader)

 # Read the header row first (skip this step if there is no header)
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")
   


# Read each row of data after the header
    #for row in csv_reader:
    #    print(row)

    #Determine number of months from Count the Total number of rows
    for row in csv_reader:
        month_counter = month_counter + 1
        profit_loss_total += int(row[1])
        profit_date.append(row[0])
        profit.append(row[1])
       # profit_loss_change = int(profit_loss_change) + int(row[1])-int(row[1]+[1])

     #Determine Total Profit Loss from Count the Profit and Loss
        #profit_loss_total = int(profit_loss_total) 

sum_profit_change = 0
profit_change=[]
#print(profit_date)

for i in range(len(profit)-1):
    profit_change.append(int(profit[i+1]) - int(profit[i]) )
    
for i in range(len(profit_change)):
    sum_profit_change= sum_profit_change + profit_change[i]
#print(sum_profit_change/(len(profit)-1))
#print(profit_change) 

max_increase = max(profit_change)
#print(max_increase)
min_increase = min(profit_change)

for i in range(len(profit_change)):
    if (max_increase == profit_change[i]):
        index_max = i
    if (min_increase == profit_change[i]):
        index_min = i
#print(max_increase,profit_date[index_max+1], profit_change[index_max])
#print(min_increase,profit_date[index_min+1], profit_change[index_min])


#print(min_increase)
   # print(row)
   # break
 



print(month_counter)
print(profit_loss_total)   
print(sum_profit_change/(len(profit)-1))
print(max_increase)
print(min_increase)
print(max_increase,profit_date[index_max+1], profit_change[index_max])
print(min_increase,profit_date[index_min+1], profit_change[index_min])
