a = 123456
b = str(a)                          #converting integer to String 
c = []

for digit in b:
    c.append (int(digit))           #here every digit in string is stored into list

print(c)                           #printing list
