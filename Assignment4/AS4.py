# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 19:54:25 2022

@author: Vernon
"""

# Conditional exercises
def conex():
    
    # Input 1 or 2 or break
    # Condtional responses: 1, 2, empty, other
    options = ["1", "2"]
    while True:
         uinput= input("Please press 1 or 2:\n")
         if uinput in options:
             print("OK")
             if uinput== '1':
                 print("Correct!\n")
             elif uinput== '2':
                 print("Incorrect!\n")
             break
        
         elif uinput == '':
             print("Subject did not respond.")
             break
         else:
             print("Subject pressed the wrong key.")
             break
                 
    return


# For loop exercises
def forlex():
    mname = ("VERNON")
    namelist= ["Amy", "Rory", "River"]
    
    # Print my name (mname) letter by letter with index counter
    i = 0
    for letter in mname:
        print(i, letter)
        i = i + 1
    print()
    
    # Print names with per name index counter
    for name in namelist:
        i = 0
        for letter in name:
            print(i, letter)
            i = i + 1
        print()
        
    return


# While loop exercises part 1
# 20 image iterations (image1 10, image2 10)
def loopex1():
    i = 0
    while i < 20:
        if i < 10:
            print("image1.png")
        else:
            print("image2.png")
        i = i + 1
    print()
    
    return


# While loop exercises part 2
# While loop displaying image until valid response (1,2) or until 5 tries
def loopex2():
    
    
    # Display image
    # Conditional response: 1, 2, empty, other
    # 5 try break
    options = ["1", "2"]
    i = 0
    while True:
        i = i + 1
        print("Displaying image.png")
        uinput= input("Please press 1 or 2:\n")
        if uinput in options:
            print("OK")
            if uinput== '1':
                print("Correct!")
            elif uinput== '2':
                print("Incorrect!")
            break
        elif uinput == '':
            print("Subject did not respond.\n")
        else:
            print("Subject pressed the wrong key.\n")
            
        if i == 5:
            print("Response incomplete. Ending program.")
            break
        
    return


# Main function        
def main():
    
    # Conditionals
    conex()
    # For-loops
    forlex()
    
    # While-loops
    loopex1()
    loopex2()
    
    return

# Execution 
if __name__ == "__main__":
    main()
