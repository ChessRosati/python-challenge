import os , csv

os.chdir(os.path.abspath(os.path.dirname(__file__)))
path = os.getcwd()
my_path = os.path.join('.', 'Resources', 'budget_data.csv')

totalMonths = 0
total = 0
averageChange = -867884
greatestIncrease = 0
greatestDecrease = 0

lastValue = 0
bigCheck = 0
smallCheck = 0

with open(my_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        totalMonths += 1
        total += int(row[1])
        if int(row[1]) - lastValue > bigCheck:
            greatestIncrease = row[0] + ' ($' + str(int(row [1]) - lastValue) +')'
            bigCheck = int(row[1]) - lastValue
        if int(row[1]) - lastValue < smallCheck:
            greatestDecrease = row[0] + ' ($' + str(int(row [1]) - lastValue) + ')'
            smallCheck = int(row[1]) - lastValue
        lastValue = int(row[1])
    

with open(my_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    test = list(csvreader)
    averageChange = (int(test[85][1]) - int(test[0][1])) / totalMonths


print(f'''
Financial Analysis
----------------------
Total Months: {totalMonths}
Total: ${total}
Average  Change: ${averageChange}
Greatest Increase in Profits: {greatestIncrease}
Greatest Decrease in Profits: {greatestDecrease}
''')

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