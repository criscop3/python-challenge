# Import os and csv read modules
import os
import csv
import sys

# Define path to file locations
csv_path = os.path.join('Resources', 'budget_data.csv')
csv_analysis = os.path.join('analysis', 'analysis.txt')

# Create lists to hold data
profits = []
months = []
profits_change = []
profits_average = []

# Open csv file
with open(csv_path,'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')

    # Loop through the data and append it to the lists
    for record in csv_reader:
       profits.append(float(record["Profit/Losses"]))
       months.append(str(record["Date"]))


    # Loop through profits list to determine differences by month and append to new lists
    for x in range(0, len(profits)):
        profits_change.append(float(profits[x] - profits[x-1]))
    for y in range(1, len(profits)):
        profits_average.append(float(profits[y] - profits[y-1]))

# File to write the output to
with open(csv_analysis, 'w') as bank_analysis:
    for x in [sys.stdout, bank_analysis]:

        # Print the calculations and export
        print()
        print("Financial Analysis", file=x)
        print("----------------------------------", file=x)
        print("Total Months: ", len(profits), file=x)
        print("Total: $", int(sum(profits)), file=x)
        print("Average Change: $", "%.2f" % (sum(profits_average) / len(profits_average)), file=x)
        print("Greatest Increase in Profits: ", months[profits_change.index(max(profits_change))] + str(" ($") + str(max(profits_change))+ str(")"), file=x)
        print("Greatest Decrease in Profits: ", months[profits_change.index(min(profits_change))] + str(" ($") + str(min(profits_change))+ str(")"), file=x)



    
        