# ---------------------------------------------------------------------------- #
#                                    Import                                    #
# ---------------------------------------------------------------------------- # 
import numpy as np
import os


# ---------------------------------------------------------------------------- #
#                                   Constants                                  #
# ---------------------------------------------------------------------------- #
STACK_SIZE = 100
WORD_SIZE = 20

# ---------------------------------------------------------------------------- #
#                                   Variables                                  #
# ---------------------------------------------------------------------------- #
top = 0
stack = []



# ---------------------------------------------------------------------------- #
#                                   Functions                                  #
# ---------------------------------------------------------------------------- #

# ------------------------- Push a word to the stack ------------------------- #
def push(word):
  
    global top
    res = True
    
    temp_array = []


    # Check if stack is full
    if top < STACK_SIZE :
        # Check if word is within word size
        if len(word) <= WORD_SIZE:
            # Insert word char by char
            for i in word:
                temp_array.append(i)

            top += 1    
            stack.append(temp_array)
        else:
            res = False
            print("Word too long")
    else:
        res = False
        print("Stack full")

    return res

# ------------------------- Pop a word from the stack ------------------------ #
def pop():
    global top
    temp_array = False
    
    # Check if stack is empty
    if not isEmpty():
        temp_array = []

        top += -1

        # Pop the word character by character
        for i in stack[top]:
            temp_array.append(i)
        
        # Delete the popped word
        del stack[top]
    
    
    return temp_array
    
# -------------------------- Check if stack is empty ------------------------- #
def isEmpty():
    return top == 0


# ---------------------------------------------------------------------------- #
#                                     Main                                     #
# ---------------------------------------------------------------------------- #
def main():
    


    filename = input("Enter the filename: ")

    try:
        with open(filename, "r") as f:
            str = ""
            for line in f:
                str += line.strip() + " "
            list_str = str.split()
    
            for word in list_str:
                push([*word])

            print(stack)

            
    except FileNotFoundError:
        msg = "Sorry, the file "+ filename + " does not exist."
        print(msg) # Sorry, the file John.txt does not exist.

    
    
    while not isEmpty():
        word = pop()
        for char in word:
            print(char, end = '')

        print(' ',end='')
 





    





if __name__ == "__main__":
    main()