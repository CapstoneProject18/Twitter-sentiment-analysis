
#input from console is taken for numbers in list
print("enter the numbers in the list:")
#input is split and given data type to int and maps to list (list())
a = list(map(int,input().split()))               
number = len(a)+1
#taking sum of all integers in list and substracting it from orginal list 
sum_all = (number*(number+1))/2                  
sum_of_list = sum(a)
print("missing number is :",(sum_all - sum_of_list))
