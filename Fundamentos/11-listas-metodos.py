lenguajes = ["Go", "Python", "Java", "PHP", "Ruby"]

#Insertar elementos en la lista
lenguajes.insert(3, "Ody")
#Eliminar objetos de la lista
lenguajes.remove("Python")
#Agregar un elemento al final de lista
lenguajes.append("Hola")
#Agregar varios elementos al final de la lista
lenguajes.extend(["1", "2", "3"])
#Borrar de ciertas parte del arreglo en adelante
#del lenguajes[3:]

ultimo = lenguajes.pop()

#Ordenar lista modificando la original (Sin poder guardar en una variable)
#lenguajes.sort()
#print(lenguajes)

#Ordenar lista modificando la original (Sin poder guardar en una variable)
lenguajes_sort = sorted(lenguajes)

print(lenguajes_sort)

print(ultimo) 
print("PHP" in lenguajes)
print(lenguajes)

lenguajes.clear()
print(lenguajes)




