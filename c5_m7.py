'''
---------------------------------------------------------------------------------------------------
#pseudocode
#1 importing csv module
#2 file = open ("file path")
#3 data of file which is read is Stored in a variable csv_file
#4  for loop :
     #making count of row
     #if > 1
     #masking the first 4 numbers with x
     #printing row
#5 else printing number without masking
----------------------------------------------------------------------------------------------------
'''
#importing csv
import csv
import hashlib
#open file
file = open('C:\\Users\\764024\\Desktop\\exercises\\Worksheet in Problems.csv')
#reading csv file variable name(file) 
csv_file = csv.reader(file)
generated_file = open("generated.csv","w")
hash_file = open("hash_file.csv","w")
count = -1
#for every row in csv file we run the loop
for row in csv_file:
            
    count = count+1
    #storing that row in variable a
    if count > 0:
        a = row[0]
    #printing the row details and replacing first 3 digits with x and displaying last four digits
        row[0] = (a[-4:].rjust(len(a),'x'))
        print(row,file = generated_file)
        row[0] = hashlib.sha256(str(a).encode('utf-8')).hexdigest()
        print(row,file = hash_file)
        
        
    else:
        print(row)
print("your hash and masking file has been generated!")
file.close()
