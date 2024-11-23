#Checks if the string entered by the user is a palindrome.
# That is that it reads the same forwards as backwards as “racecar”

global_word: str = input("introdu un cuvant:")

def palindrom_checker(local_word):
    if local_word == local_word[::-1]:
        return True
    else:
        return False

if palindrom_checker(global_word) == True:
    print(f"cuvantul {global_word} este Palindrom")
else:
    print(f"cuvantul {global_word} NU este Palindrom")

