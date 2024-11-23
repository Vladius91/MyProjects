import math

#Enter a number and have the program generate
# e up to that many decimal places. Keep a limit to how far the program will go.
number = input("Introduce one number: ")

def eDigit(n):
    result = f"{math.pi:.{n}f}"
    return result

print(eDigit(number))