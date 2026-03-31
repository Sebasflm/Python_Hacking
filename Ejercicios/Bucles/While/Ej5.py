# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.

try:
    num = int(input("Por favor ingrese un numero del 1 al 10: \n"))

    mul = 1
    while mul <= 10:
        print(f"{num}x{mul}={num*mul}")
        mul += 1
    
except ValueError: 
    print("Por favor ingresar un parametro valido")

