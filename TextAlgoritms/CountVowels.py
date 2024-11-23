# Enter a string and the program counts the number of vowels in the text.
# For added complexity have it report a sum of each vowel found.

global_name = input("Introdu un cuvant: ")
vowels = {
  "a": 0,
  "e": 0,
  "i": 0,
  "o": 0,
  "u": 0,
}

def vowel_counter(local_name):
    for letter in local_name:
        if letter in vowels:
            vowels[letter] += 1

vowel_counter(global_name)

print(vowels)