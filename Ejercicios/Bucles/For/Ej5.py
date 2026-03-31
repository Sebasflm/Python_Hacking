# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).

print("Primera solucion\n")

palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra_inicial = input("Por favor ingrese una letra: \n").lower()
contador = 0 


for palabra in palabras:
        if palabra[0].lower() == letra_inicial:
            contador += 1

print(f"La cantidad de palabras que tenían la letra {letra_inicial} como inicial fue de {contador}\n")

##############################################################################################


print("Segunda solucion\n")

palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra = input("Introduce una letra: ").lower()  # Convertimos la letra a minúscula
contador = 0

for palabra in palabras:
  
  if palabra.lower().startswith(letra):  # Comparamos en minúsculas
    contador += 1

print(f"Hay {contador} palabras que empiezan con la letra {letra}")

