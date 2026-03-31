def findMinMaxSums(n, arr, k):
    # Calcular máximo: eliminar k elementos más pequeños
    arr_copy = arr[:]
    
    # Encontrar los k elementos más pequeños (selección directa)
    for i in range(k):
        min_idx = i
        for j in range(i + 1, n):
            if arr_copy[j] < arr_copy[min_idx]:
                min_idx = j
        arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
    
    # Sumar los n-k elementos más grandes
    max_sum = 0
    for i in range(k, n):
        max_sum += arr_copy[i]
    
    # Calcular mínimo: eliminar k elementos más grandes
    arr_copy2 = arr[:]
    
    # Encontrar los k elementos más grandes (selección directa)
    for i in range(k):
        max_idx = i
        for j in range(i + 1, n):
            if arr_copy2[j] > arr_copy2[max_idx]:
                max_idx = j
        arr_copy2[i], arr_copy2[max_idx] = arr_copy2[max_idx], arr_copy2[i]
    
    # Sumar los n-k elementos más pequeños
    min_sum = 0
    for i in range(k, n):
        min_sum += arr_copy2[i]
    
    return [max_sum, min_sum]

# ===== EJECUCIÓN DE EJEMPLOS =====
# Ejemplo 1
n = 5
arr = [1, 2, 3, 4, 5]
k = 1
resultado = findMinMaxSums(n, arr, k)
print(resultado[0], resultado[1])  # Output: 14 10

# Ejemplo 2
n = 3
arr = [5, 6, 7]
k = 2
resultado = findMinMaxSums(n, arr, k)
print(resultado[0], resultado[1])  # Output: 7 5

# Ejemplo 3
n = 6
arr = [1, 1, 1, 1, 1, 1]
k = 3
resultado = findMinMaxSums(n, arr, k)
print(resultado[0], resultado[1]) 