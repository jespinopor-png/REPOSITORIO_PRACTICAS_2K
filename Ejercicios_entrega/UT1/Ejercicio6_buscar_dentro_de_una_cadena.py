texto = input("Ingrese una cadena de caracteres: ")

contador = texto.count("o")

contador_total = texto.lower().count("o")

print(f"Número de 'o' minúsculas: {contador}")
print(f"Número total de 'o' (mayúsculas y minúsculas): {contador_total}")

