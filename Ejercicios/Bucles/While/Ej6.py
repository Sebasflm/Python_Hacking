# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
# Un número es primo si es divisible por sólo uno de los números enteros entre 1 y él mismo, incluido.


n = int(input("Introduce un número entero positivo N: "))

numero = 2

while numero <= n:

  es_primo = True  # Asumimos que el número es primo hasta que se demuestre lo contrario
  divisor = 2

  while divisor * divisor <= numero:  # Optimizamos: no es necesario probar divisores hasta numero
    if numero % divisor == 0:
      es_primo = False  # Si encontramos un divisor, no es primo
      break  # Salimos del bucle interior
    divisor += 1

  if es_primo:
    print(numero)

  numero += 1