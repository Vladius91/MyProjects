#Pig Latin - Pig Latin is a game of alterations played on the English language game.
# To create the Pig Latin form of an English word the initial consonant sound
# is transposed to the end of the word and an ay is affixed
# (Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules.
from linecache import cache

consoane = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
     'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

vocale = ['a', 'e', 'i', 'o', 'u']


cuvant = input("introdu un cuvant: ")


def pig_latin_transformer(word):
    if word[0] in consoane:
        counter = 0
        for letter in range(len(word)):
            if word[letter] in consoane:
                counter += 1
            else:
                break
        if counter > 0:
            word = word[counter:] + word[:counter] + "ay"
            return word
    else:
        word = word + "ay"
        return word

print(pig_latin_transformer(cuvant))