import math

#Enter a number and have the program
# generate PI up to that many decimal places. Keep a limit to how far the program will go
a = input("Enter a number: ")

def printPi(n):
    result = f"{math.pi:.{n}f}"
    return result

print("This is pi until decimal " + a + ": " + printPi(a))