num1 = float(input("Introduce el numero a dividir: "))
num2 = float(input("Introduce la cantidad a dividir: "))
if num2 == 0:
    print("Error: No se puede dividir entre cero.")
else:
    resultado = num1 / num2
    print(f"El resultado es: {resultado}")

