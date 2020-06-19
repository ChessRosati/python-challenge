import os , csv, operator

os.chdir(os.path.abspath(os.path.dirname(__file__)))
path = os.getcwd()
my_path = os.path.join('.', 'Resources', 'election_data.csv')

candidateList = {}
total = 0

with open(my_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        total += 1
        if row[2] not in candidateList:
            candidateList[row[2]] = 1
        else:
            candidateList[row[2]] += 1
    

print(f'''
Election Results
-------------------------
Total Votes: {total}
-------------------------
Khan: {candidateList["Khan"] / total * 100}% ({candidateList["Khan"]})
Correy: {candidateList["Correy"] / total * 100}% ({candidateList["Correy"]})
Li: {candidateList["Li"] / total * 100}% ({candidateList["Li"]})
O'Tooley: {candidateList["O'Tooley"] / total * 100}% ({candidateList["O'Tooley"]})
-------------------------
Winner: {max(candidateList.items(), key=operator.itemgetter(1))[0]}
-------------------------
''')

file1 = open("./Analysis/analysis.txt", "w")
file1.write(f'''
Election Results
-------------------------
Total Votes: {total}
-------------------------
Khan: {candidateList["Khan"] / total * 100}% ({candidateList["Khan"]})
Correy: {candidateList["Correy"] / total * 100}% ({candidateList["Correy"]})
Li: {candidateList["Li"] / total * 100}% ({candidateList["Li"]})
O'Tooley: {candidateList["O'Tooley"] / total * 100}% ({candidateList["O'Tooley"]})
-------------------------
Winner: {max(candidateList.items(), key=operator.itemgetter(1))[0]}
-------------------------
''')