#What we want to find
    # Total months
    # Net total amount of Profit/Losses
    # Average change over entire period
    # Greatest increase in profits (date & amount) over entire period
    # Greatest decrease in profits (date & amount) over entire period

#Import Modules
import os
import csv

#My variables
Total_Months = 0
Total_Profit = 0
previousday = 0
PLchange = 0
Average_Change = 0
Dates = []
P_L = []

#Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

#Open the CSV file
with open (csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skip the header
    csvheader = next(csvreader, None)

    #Loop through the csv file
    for row in csvreader:

        #Find the total Profit
        Total_Profit = Total_Profit + int(row[1])

        #Find the total months
        Total_Months = Total_Months + 1 

        #Find the daily change in profits
        PLchange = int(row[1]) - previousday
        P_L.append(PLchange)
        previousday = int(row[1])
        Dates = Dates + [row[0]]

        #Find the greatest increase in profits
        


    print(int(Total_Months))
    print(int(Total_Profit))

    


