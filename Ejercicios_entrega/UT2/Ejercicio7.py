renta = float(input("Introduce tu renta anual en €: "))
if renta < 10000:
    tipo = 5
elif 10000 <= renta < 20000:
    tipo = 15
elif 20000 <= renta < 35000:
    tipo = 20
elif 35000 <= renta < 60000:
    tipo = 30
else:
    tipo = 45
print(f"El tipo impositivo que te corresponde es: {tipo}%")



