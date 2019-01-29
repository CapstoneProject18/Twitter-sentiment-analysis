import csv
import matplotlib.pyplot as pt

#file path
f_name = "C:\\Users\\764024\\Desktop\\exercises\\Worksheet in Problems2.csv"

fields = []
rows = []
onsite =[]
offshore = []
dates = []

ctr = 0

#reading csv file

with open(f_name,'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    fields = next(csv_reader)

    for row in csv_reader:
        rows.append(row)

    print("total no of rows: %d" %(csv_reader.line_num))


print('total fields are: '+','.join(field for field in fields))

for row in rows:
    if row[0] not in dates:
         dates.append(row[0])

for x in dates:
    offshore.append(0)
    onsite.append(0)

    for row in rows:

        if(row[4] == "Onsite") and (x == row[0]) and (row[3] != "Contractor" and row[3] != "intern"):
            onsite[ctr]+=1
        elif(row[4] == "Offshore") and (x == row[0]) and (row[3] != "Contractor" and row[3] != "intern"):
            offshore[ctr] += 1

    ctr += 1

print("{}  {}".format(onsite,offshore))


pt.bar(dates,offshore, width = 0.3, color = "green", label="Offshore")
pt.bar(dates,onsite,width = 0.3,color = "red", label = "Onsite")

pt.legend(loc ="best")
pt.title("Off/On")

pt.xlabel('dates')
pt.ylabel('off/on')

pt.show()
