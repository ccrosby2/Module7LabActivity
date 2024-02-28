#Cierra Crosby
#Instructor Nathan Braun
#2/27/2024
#Module 7 Problem 1 
#This program write a Python function to check whether a number is in a given range. Use range(1,10). Print whether the number is in or not in the range. Write a Python function to multiply all the numbers in a list. 
#Use list [5, 2, 7,-1].

def multi_a_list(numbers):
    
    result=1
    
    for num in numbers:
        result*=num
        
    return result
    
my_list=[5, 2, 7,-1]
print (multi_a_list(my_list))
