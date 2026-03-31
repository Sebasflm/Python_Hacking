a = 4  # prueba con 4, 3, 7, 10, etc.

print(f"a = {a}")
print(f"a % 2 = {a % 2}")
print()

# CON not (equivalente al ! de C)
if not (a % 2):
    print("CON not: Es EVEN (par) ✅")
else:
    print("CON not: No entró al if")

# SIN not
if a % 2:
    print("SIN not: Entró al if → lógica invertida ❌")
else:
    print("SIN not: No entró al if")