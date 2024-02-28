#Cierra Crosby
#Instructor Nathan Braun
#2/27/2024
#Module 7 Problem 1 
#This program write a Python function to check whether a number is in a given range. Use range(1,10). Print whether the number is in or not in the range.


def check_a_range(number):
    if number in range(1,10):
        print("This number is in the range.")
    else:
        print("This number is not in the range. Try again.")
        
num=13
check_a_range(num)

    