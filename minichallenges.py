

# Día 1 – Inversión de una Cadena


texto = input("Ingresa una cadena: ")
print("Invertida:", texto[::-1])

# Día 2 – Tabla de Multiplicar
n = int(input("\nNúmero para la tabla: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")




# Día 3 – Contar Vocales

vocales = "aeiouAEIOU"
cadena = input("\nIngresa otra cadena: ")
conteo = sum(1 for c in cadena if c in vocales)
print("Vocales encontradas:", conteo)

# Día 4 – Ordenar Lista
nums = input("\nNúmeros separados por espacios: ")
lista = [int(x) for x in nums.split()]
lista.sort()
print("Orden ascendente:", lista)




# Día 5 – Crear un Diccionario

claves = input("\nClaves separadas por comas: ").split(",")
valores = input("Valores separados por comas: ").split(",")
dicc = dict(zip(claves, valores))
print("Diccionario resultante:", dicc)

# Día 6 – Conversión de Temperatura
celsius = float(input("\nTemperatura en °C: "))
fahrenheit = celsius * 9/5 + 32
print(f"{celsius} °C = {fahrenheit} °F")




# Día 7 – Juego Piedra, Papel o Tijeras

import random
opciones = ["piedra", "papel", "tijeras"]
usuario = input("\nElige piedra, papel o tijeras: ").lower()
compu = random.choice(opciones)
print("Computadora:", compu)
if usuario == compu:
    print("¡Empate!")
elif (usuario, compu) in [("piedra", "tijeras"),
                          ("papel", "piedra"),
                          ("tijeras", "papel")]:
    print("¡Ganaste!")
else:
    print("Perdiste :(")





# Día 8 – Generador de Contraseñas Seguras

import string, random
long = int(input("\nLongitud de la contraseña (8‑16): "))
long = max(8, min(long, 16))  # forzar rango
caracteres = string.ascii_letters + string.digits + string.punctuation
contraseña = "".join(random.choice(caracteres) for _ in range(long))
print("Contraseña generada:", contraseña)
