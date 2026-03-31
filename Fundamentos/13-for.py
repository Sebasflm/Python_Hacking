# Iterar por elemenmtos
lenguajes = ["Go", "Python", "Java", "PHP", "Ruby"]

for lenguaje in lenguajes: 
    print(lenguaje)

##Iterar caracter por caracter
numeros = 12345678

for numero in str(numeros):
    nuevo_numero = int(numero) * 2
    print(nuevo_numero)

#Recuperar indice de objetos

frutas = ["Pera", "Manzana", "Pina", "Frutilla", "Banana"]
for index, fruta in enumerate(frutas):
    if fruta == "Manzana":
        print(index)

##Bucles anidados

letras = ["a", "b", "c"]
valores = [1,2,3]


for letra in letras:
    for valor in valores:
        print(letra + " x " + str(valor))

#Break

print("\nBreak:")
animales = ["loro", "perro", "gato", "conejo", "caballo", "gaviota"]
for index, animal in enumerate(animales):
    print(animal)
    if animal == "perro":
        break

print("\nContinue:")
animales = ["loro", "perro", "gato", "conejo", "caballo", "gaviota"]
for index, animal in enumerate(animales):
    if animal == "perro":
        continue
    print(animal)

#Compresión de Listas (List Comprehesion)
animales = ["loro", "perro", "gato", "conejo", "caballo", "gaviota"]
animales_mayus = [animal.upper() for animal in animales]
print("\n" + str(animales_mayus) + "\n")


pares = [num for num in [1,2,3,4,5,6] if num % 2 == 0]
print(str(pares) + "\n")
