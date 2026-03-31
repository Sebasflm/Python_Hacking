
##Principios de lista


lenguajes = [["Go", "Python"], ["Java", "PHP"], ["Ruby", "SQL"], ["Django", "Rust"], ["Aguacate", "Jira"]]

print(lenguajes[3][1])
print(lenguajes[1::2])



#Concatenar Listas#

lista1= [1,2,3,4,5,6,7,8,9,10]

print(max(lista1))

print(lista1)

## Forma1 (Menos eficiente)
lista1= lista1 + [11,12,13,14,15]

##Forma 2 (Más eficiente)
lista1 += [16,17,18,19,20] 

print(lista1)

## Recuperar longitud de una
print(len(lista1))
