"""
File: truthtable.py

Project: Truth Table

Description: Generates a truth table for a user-defined boolean expression

Programmer: Amy Ariel
"""

def getOutput(a, b, c, d):
    f = (a and c) or (((not a) or b) and (not c) and (not d))
    
    print(f"{a} {b} {c} {d} | {int(f)}")

print(f"A B C D | F")
getOutput(0, 0, 0, 0)
getOutput(0, 0, 0, 1)
getOutput(0, 0, 1, 0)
getOutput(0, 0, 1, 1)
getOutput(0, 1, 0, 0)
getOutput(0, 1, 0, 1)
getOutput(0, 1, 1, 0)
getOutput(0, 1, 1, 1)
getOutput(1, 0, 0, 0)
getOutput(1, 0, 0, 1)
getOutput(1, 0, 1, 0)
getOutput(1, 0, 1, 1)
getOutput(1, 1, 0, 0)
getOutput(1, 1, 0, 1)
getOutput(1, 1, 1, 0)
getOutput(1, 1, 1, 1)
