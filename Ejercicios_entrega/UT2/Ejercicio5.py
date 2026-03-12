edad = int(input("Ingresa tu edad: "))
ingresos = float(input("Ingresa tus monto mensual en €: "))
if edad > 16 and ingresos >= 1000:
    print("Tienes que tributar.")
else:
    print("No tienes que tributar.")


