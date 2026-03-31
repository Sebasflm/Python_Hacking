def suma_en_rango(a, b):
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    # 1. Validar que ambos sean positivos
    if a < 0 or b < 0:
        return -1
    # 2. Validar orden
    if a >= b:
        return 0
    

    suma = 0

    # 3. Sumar elementos dentro del rango
    for num in arr:
        if a <= num <= b:
            suma += num
    # 4. Si no se sumó nada
    if suma == 0:
        return 0
    return suma


print("El resultado de la suma es: " + str(suma_en_rango(120, 10)))
