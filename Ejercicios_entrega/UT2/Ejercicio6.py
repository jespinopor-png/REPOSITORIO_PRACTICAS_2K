nombre = input("Ingresa tu nombre: ")
sexo = input("Ingresa tu sexo (M/F): ").upper()
if (sexo == 'F' and nombre[0].upper() < 'M') or (sexo == 'M' and nombre[0].upper() > 'N'):
    print("Perteneces al grupo A.")
else:
    print("Perteneces al grupo B.")

    
