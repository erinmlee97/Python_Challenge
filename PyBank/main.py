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
Dates = []
P_L = []
maxprofitchange = 0
maxprofitmonth = 0
minprofitchange = 0
minprofitmonth = 0
AveragePL = 0

#Set path for files
csvpath = os.path.join("Resources", "budget_data.csv")
writepath= os.path.join("analysis", "fianacial_analysis.text")

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
        if (PLchange > maxprofitchange):
            maxprofitchange = PLchange
            maxprofitmonth = row[0]

        #Find the greatest decrease in profits
        if (PLchange < minprofitchange):
            minprofitchange = PLchange
            minprofitmonth = row[0]

    #Find the average change over entire period
    AveragePL = round((sum(P_L)/len(P_L)),2)

    #Print Analysis
    print("Financial Analysis")
    print("-------------------------------------------------------")
    print(f"Total Months: {Total_Months}")
    print(f"Total:  ${Total_Profit}")
    print(f"Average Change: ${AveragePL}")
    print(f"Greatest Increase in Profits: {maxprofitmonth} ${maxprofitchange}")
    print(f"Greatest Decrease in Profits: {minprofitmonth} ${minprofitchange}")

#Add analysis to financial_analysis text file
with open (writepath, "w", newline='') as txtfile:
    
    txtfile.write(f"Fianancial Analysis\n")
    txtfile.write(f"-------------------------------------------------------------------\n")
    txtfile.write(f"Total Months: {Total_Months}\n") 
    txtfile.write(f"Total:  ${Total_Profit}\n")
    txtfile.write(f"Average Change: ${AveragePL}\n")
    txtfile.write(f"Greatest Increase in Profits: {maxprofitmonth} ${maxprofitchange}\n")
    txtfile.write(f"Greatest Decrease in Profits: {minprofitmonth} ${minprofitchange}\n")




    


