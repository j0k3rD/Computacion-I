# #-----------------------------------------------------------------------------------------------#

#Metodo Seleccion

lista = [5,7,3,1,8,4,9,2,6]

def selection(list):
    longitud = len(lista)

    for i in range(longitud-1):
        menor = i

        for j in range (i+1, longitud):
            if lista[j] < lista[menor]:
                menor = j
    
        temporal = lista[menor]
        lista[menor] = lista[i]
        lista[i] = temporal

    print(lista)

selection(lista)

# #-----------------------------------------------------------------------------------------------#

#Metodo Burbuja

lista = [5,7,3,1,8,4,9,2,6]

def burble(list):
    for i in range(len(lista)-1):
        for j in range(len(lista)-i-1):
            print("Comparando: ", lista[j], "con", lista[j+1])

            if lista[j] > lista[j+1]:

                temporal = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temporal

                print("Intercambio:", lista[j], "por", lista[j+1])
    print(lista)

burble(lista)

#-----------------------------------------------------------------------------------------------#

#Metodo QuickSort

nums = [8,12,3,11,5,9,10,4,15,7,8,11,6]

def part(lst):

    pivot = lst[0]
    minor = []
    bigger = []

    for i in range (1, len(lst)):
        if lst[i] < pivot:
            minor.append(lst[i])
        else:
            bigger.append(lst[i])

    return minor, pivot, bigger


def quicksort(lst):

    if len(lst) < 2:
        return lst

    minor, pivot, bigger = part(lst)

    return quicksort(minor) + [pivot] + quicksort(bigger)

print(quicksort(nums))

#-----------------------------------------------------------------------------------------------#

#Metodo Merge

def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        left = lista[:mid] #Copia los elementos de la mitad izquierda del arreglo
        right = lista[mid:] #Copiar los elementos de la mitad derecha del arreglo

        merge_sort(left) #Ordena la primera mitad
        merge_sort(right) #Ordena la segunda mitad

        i=0
        j=0
        k=0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lista[k] = left[i]
                i+=1
            else:
                lista[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            lista[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            lista[k] = right[j]
            j+=1
            k+=1
        
nums = [5,7,3,1,8,4,9,2,6]
print("Numeros desordenados: ", nums)

merge_sort(nums)
print("Numeros Ordenados:", nums)

# # #-----------------------------------------------------------------------------------------------#