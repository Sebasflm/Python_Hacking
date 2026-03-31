# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for

numeros = [10, 20, 30, 40, 50]
total_suma = 0

for num in numeros:
    total_suma += num
    
media = total_suma / len(numeros)

print(media)
