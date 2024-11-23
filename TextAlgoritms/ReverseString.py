#Reverse a String - Enter a string and the program will reverse it and print it out.

cuvant = input("Introdu un cuvant: ")

def string_reverser(word):
    return word[::-1]

print(string_reverser(cuvant))