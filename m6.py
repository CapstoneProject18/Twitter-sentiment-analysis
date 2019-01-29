import csv
fields = ['name','id','email','date of joining','city','state','country']
file = open(example.csv,'wb')
csv_file = csv.writer(file)

for row in csv_file:
    csv_file.writerow(fields)
    print(csv_file)

