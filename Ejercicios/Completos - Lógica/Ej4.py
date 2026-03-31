"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

numeros = [4, 5, 6, 2]
gol = 8

def find_first_sum(nums, goal):

    for i,num in enumerate(nums):
        for j,num1 in enumerate(nums):
            if num + num1 == goal and i != j:
                return [i, j]
                

resultado = find_first_sum(numeros,gol)
print(resultado)
    