tipo_pizza = input("¿Quieres una pizza vegetariana? (s/n): ").lower()
if tipo_pizza == 's':
    print("Ingredientes vegetarianos disponibles: ")
    print("1. Pimiento")
    print("2. Tofu")
    eleccion = input("Elige un ingrediente (1/2): ")
    if eleccion == '1':
        ingrediente = "Pimiento"
    elif eleccion == '2':
        ingrediente = "Tofu"
    else:
        ingrediente = "Ingrediente no válido"
    es_vegetariana = True
elif tipo_pizza == 'n':
    print("Ingredientes no vegetarianos disponibles: ")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")
    eleccion = input("Elige un ingrediente (1/2/3): ")
    if eleccion == '1':
        ingrediente = "Peperoni"
    elif eleccion == '2':
        ingrediente = "Jamón"
    elif eleccion == '3':
        ingrediente = "Salmón"
    else:
        ingrediente = "Ingrediente no válido"
    es_vegetariana = False
else:
    ingrediente = "Tipo de pizza no válido"
    es_vegetariana = None
if es_vegetariana is True:
    print(f"Has elegido una pizza vegetariana con {ingrediente}, mozzarella y tomate.")
elif es_vegetariana is False:
    print(f"Has elegido una pizza no vegetariana con {ingrediente}, mozzarella y tomate.")
else:
    print("No se pudo determinar el tipo de pizza.")

