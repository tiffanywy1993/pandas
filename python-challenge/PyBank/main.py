
import os
import csv



csvpath = os.path.join('budget_data.csv')


total_months = 0
total_profit = 0
greatest_inc = ["",0]
greatest_inc_date = ""
greatest_dec = ["",9999999999999]
greatest_dec_date = ""
preRev= 0
revChange = 0
monthlyrevchange =[]

with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)


    for row in csvreader:
        total_months += 1
        total_profit += int(row[1])
        revChange= int(row[1]) - preRev
        preRev = int(row[1])


        if (revChange > greatest_inc[1]):
            greatest_inc[1] = revChange
            greatest_inc[0]= row[0]

        if (revChange < greatest_dec[1]):
            greatest_dec[1] = revChange
            greatest_dec[0] = row[0]

    monthlyrevchange.append(int(row[1]))

average_change = (monthlyrevchange[-1] - monthlyrevchange[0]) / total_months


print("Financial Analysis")
print("--------------------------------------------")
print("Total Months: " + str(total_months))
print("Total Profit: $" + str(total_profit))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + greatest_inc_date + " ($" + str(greatest_inc) + ")")
print("Greatest Decrease in Profits: " + greatest_dec_date + " ($" + str(greatest_dec) + ")")

new_file = open("Output/analysis_1.txt", "w")


new_file.write("Financial Analysis \n")
new_file.write("-------------------------------------------- \n")
new_file.write("Total Months: " + str(total_months) + "\n")
new_file.write("Total Profit: $" + str(total_profit) + "\n")
new_file.write("Average Change: $" + str(average_change) + "\n")
new_file.write("Greatest Increase in Profits: " + greatest_inc_date + " ($" + str(greatest_inc) + ")" + "\n")
new_file.write("Greatest Decrease in Profits: " + greatest_dec_date + " ($" + str(greatest_dec) + ")" + "\n")
