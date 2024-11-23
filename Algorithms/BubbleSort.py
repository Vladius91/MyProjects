arr = [4,6,33,11,987,43,2131,66,321,1,90]

def bubblesort(lista):
    lenght = len(lista)

    for i in range(lenght):
        swapped = False

        for j in range(0,lenght-i-1):
            if lista[j] > lista[j+1]:
                lista[j],lista[j+1] = lista[j+1], lista[j]
                swapped = True
        if not swapped:
            break

bubblesort(arr)
print(arr)