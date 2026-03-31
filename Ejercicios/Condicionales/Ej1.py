#Ejercicio 1: Determinar el mayor de 2 numeros 
#Pide al usuario que introduzca 2 números y muestra un mensaje
#Indicando cual es el mayor de los números

a, b = input("Ingresa el primer y segundo número seguido de un espacio, es decir (num1) (num2)\n").split()


print(a)
print(b)

if int(a) > int(b):
    print("El número mayor es " + str(a))
elif int(b) > int(a):
    print("El número mayor es " + str(b))
else:
    print("Los números ingresados son iguales")



