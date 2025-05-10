#Este programa elimina el número más grande de la lista numeros utilizando la función max() 
# para encontrar el valor máximo y remove() para eliminarlo.
numeros = [8, 15, 3, 227]
numeros.remove(max(numeros))  # Elimina el valor máximo de la lista
print(numeros)  # Imprime la lista sin el número máximo (227)
