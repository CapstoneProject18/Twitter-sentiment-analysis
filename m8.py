import csv
file = open('C:\\Users\\764024\\Desktop\\exercises\\Worksheet in Problems2.csv')
csv_file = csv.reader(file)
onoff = []

for row in csv_file:
    onoff.append(row[4])
print(len(onoff))
print(onoff.count("Offshore"))
print(onoff.count("Onsite"))

day = []
for row in csv_file:
    day.append(row[0])
    if row == "1/2017":
        print(onoff.count("Offshore"))

    
    
#pending
        
