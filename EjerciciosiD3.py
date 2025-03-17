texto = input("Ingrese el texto a eleccion: ")

print("\n")

letras = []

texto = texto.lower()

letras.append(input("Ingrese la letra a eleccion: ").lower())
letras.append(input("Ingrese la letra a eleccion: ").lower())
letras.append(input("Ingrese la letra a eleccion: ").lower())

print("\n")

cantidad_letras0 = texto.count(letras[0])
cantidad_letras1 = texto.count(letras[1])
cantidad_letras2 = texto.count(letras[2])

print(f"La letra {letras[0]} se encontro {cantidad_letras0} veces ")
print(f"La letra {letras[1]} se encontro {cantidad_letras1} veces ")
print(f"La letra {letras[2]} se encontro {cantidad_letras2} veces ")

cantidad_palabras = texto.split()

print("\n")

print(f"El texto contiene {len(cantidad_palabras)} palabras")

primera_letra = texto[0]
ultima_letra = texto[-1]

print("\n")

print(f"La primer letra del texto es {primera_letra} y la ultima es {ultima_letra}")

cantidad_palabras.reverse()
texto_invertido = ' '.join(cantidad_palabras)

print("\n")

print(f"El texto inverso es: '{texto_invertido}'")

buscar_python = "python" in texto
dic = {True: "si", False: "no"}
print("\n")

print(f"La palabra Python {dic[buscar_python]} se encuentra en el texto")














