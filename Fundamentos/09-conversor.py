
temperatura = float(input("Ingrese la temperatura: "))
tipo = input("Está en Farenheit(F) o Celsius(C): ")

if tipo == "F":
    resultado = float((temperatura - 32) * (5 / 9))
    print("La temperatura ingresada en Grados Celcius es " + str(resultado))
elif tipo == "C":
    resultado = float((temperatura * (9 / 5)) + 32)
    print("La temperatura ingresada en Grados Farenheit es " + str(resultado))
else: 
    print("Por favor ingrese una opción válida")
