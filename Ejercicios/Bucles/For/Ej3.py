# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.

numeros = [15, 5, 25, 10, 20, 40, 70]
mayor = 0

for num in numeros:
    if num > mayor:
        mayor = num

print(f"El numero mayor es {mayor}")
