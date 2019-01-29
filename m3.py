'''
----------pseudocode---------------------------------------------------------------------------
1. defining the function to check whether the given strings are anagrams or not Anagram()
2. n1 = length of string1
3. n2= length of string 2
4. if condition to check two are same or not
5. for loop will iterate through 0 to len(n1) o len(2)
6. found equal then returns func
7. taking input from console seperated with comas
8. printing answers
------------------------------------------------------------------------------------------------

'''
def Anagram(str1, str2):  
    # Get lengths of both strings  
    n1 = len(str1)  
    n2 = len(str2)  
  
    # If lenght of both strings is not same, then  
    # they cannot be anagram  
    if n1 != n2:  
        return 0
  
    # Sorting both strings  
    str1 = sorted(str1) 
    str2 = sorted(str2) 
  
    # Comparing sorted strings  
    for i in range(0, n1):  
        if str1[i] != str2[i]:  
            return 0
  
    return 1

  #taking inputs of strings from console
str1,str2 = input("enter str1 and str2").split(',')
if Anagram(str1, str2):  
    print ("two strings are anagrams") 
else:  
    print ("two strings are not anagrams") 
