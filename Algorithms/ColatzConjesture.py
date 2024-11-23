#- Start with a number n > 1. Find the number of steps it takes to reach one using the following process:
# If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

n = int(input("Enter one number bigger than 1 number: "))

def collatzconjecture(number):
    counter = 0
    if number < 1:
        raise ValueError("The number must be greater than 0.")

    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = (number * 3) + 1
        counter +=1
    return counter


print(collatzconjecture(n))
