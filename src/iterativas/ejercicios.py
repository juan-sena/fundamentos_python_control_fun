# Bucles for y sentencia range
# Bucle for básico
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

# La función range()
for i in range(5):
    print(i)

# Iterando sobre índices
nombres = ["Ana", "Carlos", "Elena"]
for i in range(len(nombres)):
    print(f"Posición {i}: {nombres[i]}")

# Iterando sobre cadenas
mensaje = "Python"
for letra in mensaje:
    print(letra)

# Iterando sobre diccionarios
usuario = {"nombre": "Laura", "edad": 28, "ciudad": "Madrid"}

# Iterando sobre claves
for clave in usuario:
    print(f"Clave: {clave}, Valor: {usuario[clave]}")

# Iterando sobre pares clave-valor
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")

# Iterando solo sobre valores
for valor in usuario.values():
    print(valor)

# Comprensiones de listas con for
# Crear una lista con los cuadrados de los números del 1 al 5
cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)  # [1, 4, 9, 16, 25]

# Filtrar elementos usando una condición
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]

# Bucles for anidados
# Crear una matriz de multiplicación 3x3
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i*j}", end="\t")
    print()  # Salto de línea después de cada fila

# Casos prácticos
# Ejemplo 1: Calcular la suma de los primeros n números
n = 10
suma = 0
for i in range(1, n+1):
    suma += i
print(f"La suma de los primeros {n} números es: {suma}")  # 55

# Ejemplo 2: Encontrar números primos en un rango
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

primos = []
for num in range(2, 20):
    if es_primo(num):
        primos.append(num)

print(f"Números primos entre 2 y 19: {primos}")  # [2, 3, 5, 7, 11, 13, 17, 19]

# Ejemplo 3: Procesamiento de datos
temperaturas = [22, 19, 24, 25, 21, 23, 20]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Encontrar el día más caluroso
max_temp = max(temperaturas)
indice_max = temperaturas.index(max_temp)
print(f"El día más caluroso fue {dias[indice_max]} con {max_temp}°C")

# Calcular la temperatura promedio
promedio = sum(temperaturas) / len(temperaturas)
print(f"Temperatura promedio: {promedio:.1f}°C")

# Días con temperatura superior al promedio
for i in range(len(dias)):
    if temperaturas[i] > promedio:
        print(f"{dias[i]}: {temperaturas[i]}°C (por encima del promedio)")

# Bucles while
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

#Cuándo usar while en lugar de for
entrada = ""
while not entrada.isdigit():
    entrada = input("Introduce un número: ")

print(f"Has introducido el número: {entrada}")

# Bucles controlados por eventos
import random

objetivo = random.randint(1, 10)
intentos = 0
adivinado = False

while not adivinado and intentos < 3:
    intentos += 1
    numero = int(input(f"Intento {intentos}/3: Adivina un número del 1 al 10: "))

    if numero == objetivo:
        print(f"¡Correcto! Has adivinado en {intentos} intentos.")
        adivinado = True
    else:
        pista = "mayor" if numero < objetivo else "menor"
        print(f"Incorrecto. El número es {pista} que {numero}.")

if not adivinado:
    print(f"Se acabaron los intentos. El número era {objetivo}.")

# Bucles con condición de salida variable
saldo = 1000
while saldo > 0:
    print(f"Saldo actual: {saldo}€")
    gasto = float(input("Introduce la cantidad a gastar (0 para salir): "))

    if gasto == 0:
        break  # Salimos del bucle inmediatamente

    if gasto > saldo:
        print("No tienes suficiente saldo.")
        continue  # Volvemos al inicio del bucle

    saldo -= gasto

print(f"Saldo final: {saldo}€")

# Bucles infinitos controlados
while True:
    respuesta = input("¿Quieres continuar? (s/n): ").lower()

    if respuesta == "n":
        print("Programa finalizado.")
        break

    if respuesta == "s":
        print("Continuando...")
    else:
        print("Respuesta no válida. Introduce 's' o 'n'.")
    
# Procesamiento de datos con while
def calcular_factorial(n):
    resultado = 1
    while n > 0:
        resultado *= n
        n -= 1
    return resultado

numero = 5
print(f"El factorial de {numero} es {calcular_factorial(numero)}")  # 120

# Simulaciones y aproximaciones
def calcular_raiz_cuadrada(numero, precision=0.0001):
    aproximacion = numero / 2  # Valor inicial
    while abs(aproximacion**2 - numero) > precision:
        aproximacion = (aproximacion + numero/aproximacion) / 2
    return aproximacion

print(f"Raíz cuadrada de 25: {calcular_raiz_cuadrada(25):.6f}")  # 5.000000
print(f"Raíz cuadrada de 7: {calcular_raiz_cuadrada(7):.6f}")    # 2.645751

# Validación de entrada con while
def obtener_numero_en_rango(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print(f"Error: El número debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print("Error: Debes introducir un número entero.")

edad = obtener_numero_en_rango("Introduce tu edad (0-120): ", 0, 120)
print(f"Edad registrada: {edad} años")

# Patrones con while
def imprimir_triangulo(altura):
    fila = 1
    while fila <= altura:
        print("*" * fila)
        fila += 1

imprimir_triangulo(5)

# Consideraciones de rendimiento
# ¡CUIDADO! Bucle infinito
contador = 1
while contador <= 5:
    print(contador)
    # Olvidamos incrementar contador

#version corregida 
contador = 1
while contador <= 5:
    print(contador)
    contador += 1  # Importante: actualizar la variable de control

# Comparación con bucles for
# Usando while
suma = 0
i = 1
while i <= 10:
    suma += i
    i += 1
print(f"Suma (while): {suma}")

# Equivalente con for
suma = 0
for i in range(1, 11):
    suma += i
print(f"Suma (for): {suma}")

# break, continue
for numero in range(1, 11):
    if numero == 5:
        print("¡Encontrado el 5! Saliendo del bucle...")
        break
    print(f"Número actual: {numero}")

print("Bucle terminado")

# Casos de uso prácticos para break
def buscar_elemento(lista, objetivo):
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice

    return -1  # Si llegamos aquí, el elemento no está en la lista

numeros = [4, 7, 2, 9, 1, 5]
posicion = buscar_elemento(numeros, 9)
print(f"El elemento se encuentra en la posición: {posicion}")

# Validación de entrada con salida: Permitir al usuario salir de un proceso de entrada.
while True:
    entrada = input("Escribe algo (o 'salir' para terminar): ")

    if entrada.lower() == 'salir':
        print("Programa terminado.")
        break

    print(f"Has escrito: {entrada}")

# Optimización de algoritmos: Evitar cálculos innecesarios.
def es_primo(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # No es primo, salimos inmediatamente

    return True  # Si llegamos aquí, es primo

# La sentencia continue
for numero in range(1, 11):
    if numero % 2 == 0:  # Si el número es par
        continue  # Saltamos a la siguiente iteración

    print(f"Número impar: {numero}")

# Casos de uso prácticos para continue
# Filtrado de datos: Procesar solo los elementos que cumplen cierta condición.
temperaturas = [22, -5, 28, 31, -15, 19, 26, -8]

print("Temperaturas positivas:")
for temp in temperaturas:
    if temp <= 0:
        continue

    print(f"{temp}°C")

# Manejo de casos especiales: Evitar procesar casos que requieren tratamiento diferente.
numeros = [1, 2, 0, 4, 0, 6, 7]

for num in numeros:
    if num == 0:
        print("Omitiendo división por cero")
        continue

    resultado = 10 / num
    print(f"10 / {num} = {resultado}")

# Validación de datos: Saltar entradas inválidas en un proceso de análisis.
datos = ["25", "error", "42", "texto", "17"]

suma = 0
for valor in datos:
    if not valor.isdigit():
        print(f"Valor no numérico ignorado: '{valor}'")
        continue

    suma += int(valor)

print(f"La suma de los valores válidos es: {suma}")

# Combinando break y continue
numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
limite = 50
suma = 0

for num in numeros:
    # Ignoramos múltiplos de 3
    if num % 3 == 0:
        print(f"Omitiendo {num} (múltiplo de 3)")
        continue

    # Sumamos el número
    suma += num
    print(f"Añadiendo {num}: suma = {suma}")

    # Si la suma supera el límite, terminamos
    if suma > limite:
        print(f"Límite de {limite} superado")
        break

# Uso en bucles anidados
for i in range(1, 4):
    print(f"Grupo {i}:")

    for j in range(1, 6):
        if j == 3:
            print("  Saltando el elemento 3")
            continue  # Solo afecta al bucle interno

        print(f"  Elemento {j}")

    print("Fin del grupo\n")
# Si necesitas salir de múltiples bucles anidados, puedes usar una bandera o variable de control:
encontrado = False

for i in range(5):
    for j in range(5):
        if i * j > 10:
            print(f"Valor encontrado: {i} * {j} = {i*j}")
            encontrado = True
            break  # Sale del bucle interno

    if encontrado:
        break  # Sale del bucle externo

# Consideraciones de rendimiento y legibilidad
# En lugar de:
for item in lista:
    if condicion1(item):
        continue
    if condicion2(item):
        break
    # Más código...

# Considera:
def procesar_item(item):
    if condicion1(item):
        return False
    if condicion2(item):
        return None
    # Procesar y devolver resultado
    return resultado

for item in lista:
    resultado = procesar_item(item)
    if resultado is None:
        break
    if resultado is False:
        continue
    # Usar resultado...

# pass y else en bucles
# Bucle que no hace nada para los números pares
for numero in range(1, 10):
    if numero % 2 == 0:
        pass  # No hacemos nada con los números pares
    else:
        print(f"Procesando número impar: {numero}")

# La cláusula else en bucles


