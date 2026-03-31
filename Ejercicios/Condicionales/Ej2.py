##Ejercicio 2: Calculadora Simple
##Pide al usuario 2 números y una operación (+, -, *, /)
##Realiza la operación y muestra el resultado (maneja la divión entre zero )

num1, num2 = input("Por favor ingresa los numeros a operar\n").split()
operacion = input ("Ahora ingresa el tipo de operación que deseas realizar\n" +
                   "[1] Suma\n" +
                   "[2] Resta\n" +
                   "[3] Multiplicación\n" + 
                   "[4] División\n" 
                   )

if int(operacion) == 1:
    resultado = float(num1) + float(num2)
    print("El resultado de la operación es: " + str(resultado))
elif int(operacion) == 2:
    resultado = float(num1) - float(num2)
    print("El resultado de la operación es: " + str(resultado))
elif int(operacion) == 3:
    resultado = float(num1) * float(num2)
    print("El resultado de la operación es: " + str(resultado))
elif int(operacion) == 4:
    resultado = float(num1) / float(num2)
    print("El resultado de la operación es: " + str(resultado))
else:
    print("Ingrese una opción válida")

