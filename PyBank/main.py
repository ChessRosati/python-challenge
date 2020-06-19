import os , csv

# relative path to find the csv file
os.chdir(os.path.abspath(os.path.dirname(__file__)))
path = os.getcwd()
my_path = os.path.join('.', 'Resources', 'budget_data.csv')

#defining our variables
totalMonths = 0
total = 0
averageChange = 0
greatestIncrease = 0
greatestDecrease = 0

#extra variables used during for loops
lastValue = 0
bigCheck = 0
smallCheck = 0

with open(my_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        #counts the number of rows
        totalMonths += 1
        #adds up total profit
        total += int(row[1])
        #if the difference between the current rows profit and that of the previous row is greater than the script has seen
        #it will save the pertinent information to the greatestIncrease variable and update the bigCheck variable
        if int(row[1]) - lastValue > bigCheck:
            greatestIncrease = row[0] + ' ($' + str(int(row [1]) - lastValue) +')'
            bigCheck = int(row[1]) - lastValue
        #Same except for small differences
        if int(row[1]) - lastValue < smallCheck:
            greatestDecrease = row[0] + ' ($' + str(int(row [1]) - lastValue) + ')'
            smallCheck = int(row[1]) - lastValue
        lastValue = int(row[1])
    
#Takes the final value for profit/losses and subtracts the first value from it, then divides that by the total months to find the average change
with open(my_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    test = list(csvreader)
    averageChange = (int(test[85][1]) - int(test[0][1])) / totalMonths

#prints out the analysis
print(f'''
Financial Analysis
----------------------
Total Months: {totalMonths}
Total: ${total}
Average  Change: ${averageChange}
Greatest Increase in Profits: {greatestIncrease}
Greatest Decrease in Profits: {greatestDecrease}
''')
#saves to a text document
file1 = open("./Analysis/analysis.txt", "w")
file1.write(f'''
Financial Analysis
----------------------
Total Months: {totalMonths}
Total: ${total}
Average  Change: ${averageChange}
Greatest Increase in Profits: {greatestIncrease}
Greatest Decrease in Profits: {greatestDecrease}
''')
