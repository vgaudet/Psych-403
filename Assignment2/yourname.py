# -*- coding: utf-8 -*-
"""
Gaudet, Vernon
ASSIGNMENT 2: LEVEL 0: "A NEW LANGUaGE"
"""
import numpy as np

global name
name = 'VERNON'

# Print Print Exercises
def printex(name):
    print("PRINT EXERCISES\nQ1-2) \n")
    # Print name char by char
    for char in name:
         print(char)
    print("\n\n")

    return name

# Operation Exercises: 
def opex():
    
    #Example operations
    opex1 = (5/2 , 5.0/2.0)
    opex2 = 5 % 2
    opex3 = (2 ** 3, 4 // 3)
    opex4 = 2 + 6 + 4 * 4 / 2
    
    return opex1, opex2, opex3, opex4

# Print results from operation exercises
def printopex(ex2):
    print("OPERATION EXERCISES\n Q1-4")
    for q, part in enumerate(ex2):
        print(('P' + str(q+1) + ') '), part)
    print('\n')
    
    return


# Variable Exercises
def varex():
    
    # Name letter variables
    letter1 = "V"
    letter2 = "E"
    letter3 = "R"
    letter4 = "N"
    letter5 = "O"
    letterX = letter1
    letter1 = "Z"
    
    return letter1, letter2, letter3, letter4, letter5, letterX

# Print results from variable exercises
def printvarex(ex3):
    print("VARIABLE EXERCISES\nQ1-6) \n")
    for part in ex3:
        print(part)
    print('\n')
    return

# Boolean Exercises:
def bolex():
    
    bolex1a = 1 == 1.0 
    bolex1b = "1" == "1.0"
    bolex2a = 5 == (3+2)
    
    # 5 different options to return true
    bolex3a = ([
        (1 == 1.0) and ("1" == "1.0") or (5 == (3+2)),
		(1 == 1.0) or ("1" == "1.0") or (5 == (3+2)),
		(1 == 1.0) and not ("1" == "1.0") or (5 == (3+2)),
		(1 == 1.0) or not ("1" == "1.0") or (5 == (3+2)),
		(1 == 1.0) and not ("1" == "1.0") or not (5 == (3+2))
        ])
    
    return bolex1a, bolex1b, bolex2a, bolex3a

# Print results from boolean exercises
def printbolex(ex4):
    print("BOOLEAN EXERCISES\nQ1-3")
    for q, part in enumerate(ex4):
        print(('P' + str(q+1) + ') '), part)
    print('\n')
    return

# List Exercises
def listex():
    
    # Odd number list and list of integers 1-99 (between 0 and 100)
    oddlist= [1,3,5,7,9]
    intlist= list(range(1, 100))
    oddlen = len(oddlist)
    oddtype = type(oddlist)
    
    return oddlist, oddlen, oddtype, intlist

# Print results from list exercises
def printlistex(ex5):
    print("LIST EXERCISES\nQ1-6")
    for q, part in enumerate(ex5):
        print(('P' + str(q+1) + ') '), part)
    print('\n')
    return
    
# Dictionary Exercises
def dictex():
    
    # Dictionary with personal information
    about_me = {
            'name': "Vernon Gaudet",
            'age': 24.7,
            'ystudy': 4,
            'ffoods': ["pumpkin pie", "dumpling chicken soup", "tonkotsu ramen"]
            }
    metype = type(about_me)
    melen = len(about_me)
    
    return about_me, metype, melen

# Print results from dictionary exercises
def printdictex(ex6):
    print("DICTIONARY EXERCISES\nQ1-3")
    for q, part in enumerate(ex6):
        print(('P' + str(q+1) + ') '), part)
    print('\n')
    return

# Array Exercises
def arrex():
    
    # Mixed int and float array
    mixnums = np.array([ 1, 2, 3, 1.0, 2.0, 3.0])
    
    # Mixed type array (int, float, str)
    mixtypes = np.array([1, 2, 1.0, 2.0, "1", "2" ])
    
    # Odd number array from 1 to 100
    oddarray = np.arange(1, 100, 2)
    
    # Log array from 1 to 5 evenly spaced for 16 numbers.
    logarray = np.array(np.logspace(np.log10(1), np.log10(5), 16))
    
    return mixnums, mixtypes, oddarray, logarray

# Print results from array exercises
def printarrex(ex7):
    print("ARRAY EXERCISES\nQ1-4")
    for q, part in enumerate(ex7):
        print(('P' + str(q+1) + ') '), part)
    print('\n')
    return

# Print menu for selecting exercise results to print
def selectionprint(ex1, ex2, ex3, ex4, ex5, ex6, ex7):
    
    options = ['1','2','3','4','5','6', '7', 'e']
    while True:
        
        print("SELECT OPTION TO PRINT:\n",
              "1. PRINT EXERCISES\n", 
              "2. OPERATION EXERCISES\n",
              "3. VARIABLE EXERCISES\n",
              "4. BOOLEAN EXERCISES\n",
              "5. LIST EXERCISES\n",
              "6. DICTIONARY EXERCISES\n",
              "7. ARRAY EXERCISES\n",
              "Press 'e' for exit.\n"
              )
        select = input() 
        print("\n")
        
        if select in options:
            if select == 'e':
                print("Goodbye!\n\n")
                break
            elif select == '1':
                printex(ex1)
            elif select == '2':
                printopex(ex2)
            elif select == '3':
                printvarex(ex3)
            elif select == '4':
                printbolex(ex4)
            elif select == '5':
                printlistex(ex5)
            elif select == '6':
                printdictex(ex6)
            elif select == '7':
                printarrex(ex7)
        else:
            print("Invalid or empty entry. Please try again.\n")
                
                
        select = input("Press any key to continue...\n")

        print("\n\n")
                    
    return

# Main function executing all exercises
def main():

    # Excecute exercise sections in following order: Print, Operations, Variables, 
    # Booleans, Variables, Dictionaries, Arrays
   
    ex1 = name
    ex2 = opex()
    ex3 = varex()
    ex4 = bolex()
    ex5 = listex()
    ex6 = dictex()
    ex7 = arrex()     
    
    # Display print menu
    selectionprint(ex1, ex2, ex3, ex4, ex5, ex6, ex7)
    
    print("Closing...")
    
    return ex1, ex2, ex3, ex4, ex5, ex6, ex7
         

if __name__ == "__main__":
    main()