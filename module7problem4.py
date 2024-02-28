#Cierra Crosby
#Instructor Nathan Braun
#2/27/2024
#Module 7 Problem 1 
#This program write a Python function that takes a list of numbers and returns a new list with unique elements of the first list. Use list [1, 3, 3, 3, 6, 2, 3, 5].
#This program use the append function.

def unique_elements(input_list):
    unique_list=[]
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
            
    return unique_list

original_list = [1, 3, 3, 3, 6, 2, 3, 5]
print(unique_elements(original_list))