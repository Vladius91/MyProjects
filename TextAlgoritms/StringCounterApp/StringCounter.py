#Count Words in a String - Counts the number of individual words in a string.
# For added complexity read these strings in from a text file and generate a summary.


content_dictionary= {}
with open("input.txt", "r") as file:
    content = file.read().split()

def list_to_dictrionary(lista):
    for word in lista:
        if word in content_dictionary:
            content_dictionary[word] += 1
        else:
            content_dictionary[word] = 1

list_to_dictrionary(content)

print(content_dictionary)


