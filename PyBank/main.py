#PYBANK

#Import the libraries.
import os
import csv
import math

#Read the CSV file and skip the header.
with open('/Users/theluggage/Desktop/DataAnalyticsBootcampHomework/python-challenge/PyBank/Resources/budget_data 3.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)


#Create veriables. Denote the starting place and make a function where it counts/accumulates the total months.
    total_months = 0

    for row in csvreader:
        total_months += 1

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")

#Calculate the total profits in row 1
with open('/Users/theluggage/Desktop/DataAnalyticsBootcampHomework/python-challenge/PyBank/Resources/budget_data 3.csv', 'r') as fin:
    fin.__next__()
    profit_total = sum(int(r[1]) for r in csv.reader(fin))
    print(f"Total: ${profit_total}")
    
# Read the header row
with open('/Users/theluggage/Desktop/DataAnalyticsBootcampHomework/python-challenge/PyBank/Resources/budget_data 3.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    prev_row = next(csvreader)
    current_row = next(csvreader)

#Create variables for monthly change, the greatest increase/decrease, and their corresponding months.
    monthly_change = int(current_row[1]) - int(prev_row[1])
    greatest_increase = monthly_change   
    greatest_decrease = monthly_change
    greatest_increase_month = current_row[0]
    greatest_decrease_month = current_row[0]

#Create the variable for average change and make it so it started on Feb. 2010, so that we can subtract it from the first month, Jan. 2010.
    avg_total = monthly_change
    months = 2

# Read each row of data after the header.
    for row in csvreader:
        monthly_change = int(row[1]) - int(prev_row[1])
        prev_row = row

#Calculate the average change throughout the rows.
        avg_total += monthly_change
        months +=1
        average_change = int(avg_total)/int(total_months - 1)

#Create if statements to find the greatest increase and decrease and cite the corresponding month.
        if(monthly_change > greatest_increase):
            greatest_increase = monthly_change
            greatest_increase_month = row[0]


        if(monthly_change < greatest_decrease):
            greatest_decrease = monthly_change
            greatest_decrease_month = row[0]
        
print(f"Avg. Change:, ${average_change}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${greatest_increase})") 
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${greatest_decrease})")
