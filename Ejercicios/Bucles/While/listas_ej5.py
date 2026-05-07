print("\nEjercicio 4:")

contrasena = ""
while len(contrasena) < 8:
  contrasena = input("Introduce una contraseña (al menos 8 caracteres): ")
  if len(contrasena) < 8:
    print("La contraseña debe tener al menos 8 caracteres. Inténtalo de nuevo.")

print("Contraseña válida")