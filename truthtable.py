"""
File: truthtable.py

Project: Truth Table

Description: Generates a truth table for a user-defined boolean expression

Programmer: Amy Ariel
"""

def getOutput(e, d='x', c='x', b='x', a='x'):   # LSB (e) first since we have optional arguments
    f = not(e)
    
    print(f"{a} {b} {c} {d} {e} | {int(f)}")

while(True):
    numVar = int(input("Number of variables? "))

    if numVar == 5:
        print(f"A B C D E | F")
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    for l in range(2):
                        for m in range(2):
                            getOutput(m, l, k, j, i)
        break

    elif numVar == 4:
        print(f"- A B C D | F")
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    for l in range(2):
                            getOutput(l, k, j, i)
        break

    elif numVar == 3:
        print(f"- - A B C | F")
        for i in range(2):
            for j in range(2):
                for k in range(2):
                            getOutput(k, j, i)
        break

    elif numVar == 2:
        print(f"- - - A B | F")
        for i in range(2):
            for j in range(2):
                            getOutput(j, i)
        break

    elif numVar == 1:
        print(f"- - - - A | F")
        for i in range(2):
                            getOutput(i)
        break
    
    else:
        print(f"Enter a number 1 thru 5.")