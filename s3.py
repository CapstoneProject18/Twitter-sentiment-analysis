#function to generate list of duplicate values in the list 
def remove_Duplicate(list):
    final_list = []                                                                     
    for letter in list:                                                                 #empty final list to store duplicate values in list 
        if letter not in final_list:                                                    #if letter is not in the list it appends that letter to final list
            final_list.append(letter)
    return final_list                                                                   #it returns finalist 
list = ["a","v","q","d","a","w","v","m","q","v"]
print(remove_Duplicate(list))

