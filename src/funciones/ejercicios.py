# Funciones
def saludar():
    print("¡Hola, mundo!")

#calcular area rectagulo como practica
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

# Uso de la función
resultado = calcular_area_rectangulo(5, 3)
print(f"El área del rectángulo es: {resultado}")  # Imprime: El área del rectángulo es: 15

# Parámetros y argumentos
def saludar_persona(nombre):  # 'nombre' es un parámetro
    print(f"Hola, {nombre}!")

saludar_persona("Ana")  # "Ana" es un argumento

# Parámetros posicionales
def calcular_precio_final(precio_base, impuesto):
    return precio_base + (precio_base * impuesto)

total = calcular_precio_final(100, 0.21)  # 100 va a precio_base, 0.21 va a impuesto
print(f"Precio final: {total}")  # Imprime: Precio final: 121.0

# Parámetros con valores predeterminados
def saludar(nombre, mensaje="¡Bienvenido!"):
    print(f"Hola {nombre}. {mensaje}")

saludar("Carlos")  # Usa el mensaje predeterminado
# Imprime: Hola Carlos. ¡Bienvenido!

saludar("María", "¿Cómo estás hoy?")  # Usa el mensaje personalizado
# Imprime: Hola María. ¿Cómo estás hoy?
# Correcto
def crear_perfil(nombre, edad, ciudad="Madrid"):
    return f"Perfil: {nombre}, {edad} años, {ciudad}"# Incorrecto - causaría un error de sintaxis
# def crear_perfil(nombre, ciudad="Madrid", edad):
#     return f"Perfil: {nombre}, {edad} años, {ciudad}"

# Parámetros por nombre
def dividir(dividendo, divisor):
    return dividendo / divisor

# Usando argumentos posicionales
resultado1 = dividir(10, 2)  # resultado1 = 5.0

# Usando argumentos por nombre
resultado2 = dividir(divisor=2, dividendo=10)  # resultado2 = 5.0

def crear_usuario(nombre, apellido, edad, email, activo=True):
    return {
        "nombre_completo": f"{nombre} {apellido}",
        "edad": edad,
        "email": email,
        "activo": activo
    }

# Más fácil de leer con argumentos por nombre
usuario = crear_usuario(
    nombre="Juan",
    apellido="Pérez",
    edad=28,
    email="juan@ejemplo.com",
    activo=False
)

# Combinando tipos de parámetros
def calcular_pago(horas, tarifa=15, moneda="EUR"):
    total = horas * tarifa
    return f"{total} {moneda}"# Diferentes formas de llamar a la función
pago1 = calcular_pago(40)  # 40 horas, tarifa predeterminada, moneda predeterminada
pago2 = calcular_pago(35, 20)  # 35 horas, tarifa de 20, moneda predeterminada
pago3 = calcular_pago(30, moneda="USD")  # 30 horas, tarifa predeterminada, moneda USD
pago4 = calcular_pago(horas=25, tarifa=18, moneda="GBP")  # Todo especificado por nombre

print(pago1)  # Imprime: 600 EUR
print(pago2)  # Imprime: 700 EUR
print(pago3)  # Imprime: 450 USD
print(pago4)  # Imprime: 450 GBP

# Validación de argumentos
def calcular_descuento(precio, porcentaje):
    # Validación de argumentos
    if not isinstance(precio, (int, float)) or precio < 0:
        raise ValueError("El precio debe ser un número positivo")

    if not isinstance(porcentaje, (int, float)) or not (0 <= porcentaje <= 100):
        raise ValueError("El porcentaje debe ser un número entre 0 y 100")

    # Cálculo del descuento
    descuento = precio * (porcentaje / 100)
    return precio - descuento

try:
    precio_final = calcular_descuento(100, 15)
    print(f"Precio con descuento: {precio_final}")  # Imprime: Precio con descuento: 85.0

    # Esto lanzará un error
    precio_erroneo = calcular_descuento(-50, 10)
except ValueError as e:
    print(f"Error: {e}")  # Imprime: Error: El precio debe ser un número positivo

# Argumentos posicionales variables (*args)
def sumar(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

# Podemos pasar cualquier cantidad de argumentos
print(sumar(1, 2))  # Imprime: 3
print(sumar(1, 2, 3, 4, 5))  # Imprime: 15
print(sumar())  # Imprime: 0

# Argumentos por nombre variables (**kwargs)
def mostrar_informacion(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

# Podemos pasar cualquier cantidad de argumentos por nombre
mostrar_informacion(nombre="Python", creador="Guido van Rossum", año=1991)
# Imprime:
# nombre: Python
# creador: Guido van Rossum
# año: 1991

# Ejemplo práctico: Función para formatear texto
def formatear_texto(texto, mayusculas=False, prefijo="", sufijo="", separador=" "):
    # Aplicar mayúsculas si se solicita
    if mayusculas:
        texto = texto.upper()

    # Dividir el texto en palabras
    palabras = texto.split()

    # Aplicar prefijo y sufijo a cada palabra
    palabras_formateadas = [f"{prefijo}{palabra}{sufijo}" for palabra in palabras]

    # Unir las palabras con el separador especificado
    resultado = separador.join(palabras_formateadas)

    return resultado

# Ejemplos de uso
texto_original = "python es un lenguaje versátil"

# Uso básico sin modificaciones
print(formatear_texto(texto_original))
# Imprime: python es un lenguaje versátil

# Convertir a mayúsculas
print(formatear_texto(texto_original, mayusculas=True))
# Imprime: PYTHON ES UN LENGUAJE VERSÁTIL

# Añadir prefijo y sufijo
print(formatear_texto(texto_original, prefijo="«", sufijo="»"))
# Imprime: «python» «es» «un» «lenguaje» «versátil»

# Cambiar el separador
print(formatear_texto(texto_original, separador="-"))
# Imprime: python-es-un-lenguaje-versátil

# Combinación de opciones
print(formatear_texto(
    texto_original,
    mayusculas=True,
    prefijo="#",
    sufijo="!",
    separador="..."
))
# Imprime: #PYTHON!...#ES!...#UN!...#LENGUAJE!...#VERSÁTIL!

# Return 
def calcular_cuadrado(numero):
    resultado = numero * numero
    return resultado  # Devuelve el valor y termina la función

area = calcular_cuadrado(4)
print(area)  # Imprime: 16

# Funciones sin return
def saludar(nombre):
    print(f"Hola, {nombre}")
    # No hay return explícito

resultado = saludar("Laura")
print(f"La función devolvió: {resultado}")  # Imprime: La función devolvió: None

# Retornando múltiples valores
def estadisticas(numeros):
    total = sum(numeros)
    promedio = total / len(numeros)
    minimo = min(numeros)
    maximo = max(numeros)
    return total, promedio, minimo, maximo

datos = [4, 8, 15, 16, 23, 42]
suma, media, menor, mayor = estadisticas(datos)

print(f"Suma: {suma}")        # Imprime: Suma: 108
print(f"Promedio: {media}")   # Imprime: Promedio: 18.0
print(f"Mínimo: {menor}")     # Imprime: Mínimo: 4
print(f"Máximo: {mayor}")     # Imprime: Máximo: 42

# Return anticipado
def dividir_seguro(a, b):
    # Verificación de seguridad
    if b == 0:
        print("Error: División por cero")
        return None  # Salida anticipada

    # Este código solo se ejecuta si b no es cero
    resultado = a / b
    return resultado

print(dividir_seguro(10, 2))   # Imprime: 5.0
print(dividir_seguro(10, 0))   # Imprime: Error: División por cero y luego None

# Patrones comunes con return
# Función booleana (predicado)
def es_mayor_de_edad(edad):
    return edad >= 18

def es_correo_valido(email):
    return "@" in email and "." in email

# Uso en condicionales
usuario_edad = 16
if es_mayor_de_edad(usuario_edad):
    print("Acceso permitido")
else:
    print("Acceso denegado")  # Imprime: Acceso denegado

# Cálculos y procesamiento
def calcular_precio_con_iva(precio_base, tasa_iva=0.21):
    return precio_base * (1 + tasa_iva)

precio_final = calcular_precio_con_iva(100)
print(f"Precio con IVA: {precio_final} €")  # Imprime: Precio con IVA: 121.0 €

# Return con estructuras de datos
def crear_lista_pares(maximo):
    return [num for num in range(2, maximo + 1, 2)]

def crear_diccionario_cuadrados(numeros):
    return {num: num ** 2 for num in numeros}

pares = crear_lista_pares(10)
print(pares)  # Imprime: [2, 4, 6, 8, 10]

cuadrados = crear_diccionario_cuadrados([1, 2, 3, 4])
print(cuadrados)  # Imprime: {1: 1, 2: 4, 3: 9, 4: 16}

# Buenas prácticas con return
# Enfoque mejorado: siempre devuelve una lista (vacía en caso de error)
def filtrar_positivos(numeros):
    if not isinstance(numeros, list):
        return []  # Lista vacía en caso de error

    return [num for num in numeros if num > 0]

# Documentar el valor de retorno: Es importante que quede claro qué devuelve la función.
def calcular_descuento(precio, porcentaje):
    """
    Calcula el precio con descuento.

    Args:
        precio: El precio original
        porcentaje: El porcentaje de descuento (0-100)

    Returns:
        float: El precio después de aplicar el descuento
    """
    return precio - (precio * porcentaje / 100)

# Evitar efectos secundarios: Las funciones que devuelven valores no deberían, idealmente, modificar el estado global o realizar acciones como imprimir.
# Mejor: separar la obtención del resultado de su presentación
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

# Uso
notas = [7, 8, 6, 9]
promedio = calcular_promedio(notas)
print(f"El promedio es: {promedio}")  # La impresión se hace fuera de la función

# Usar return temprano para casos especiales: Esto mejora la legibilidad del código.
def obtener_calificacion(puntuacion):
    if puntuacion < 0 or puntuacion > 100:
        return "Puntuación inválida"

    if puntuacion >= 90:
        return "Sobresaliente"
    if puntuacion >= 70:
        return "Notable"
    if puntuacion >= 60:
        return "Bien"
    if puntuacion >= 50:
        return "Suficiente"

    return "Insuficiente"

# Ejemplo práctico: Función de conversión de temperatura
def convertir_temperatura(valor, origen, destino):
    """
    Convierte una temperatura entre diferentes unidades.

    Args:
        valor: El valor de la temperatura a convertir
        origen: Unidad de origen ('C', 'F' o 'K')
        destino: Unidad de destino ('C', 'F' o 'K')

    Returns:
        float: La temperatura convertida, o None si los parámetros son inválidos
    """
    # Validación de parámetros
    unidades_validas = {'C', 'F', 'K'}
    if origen not in unidades_validas or destino not in unidades_validas:
        return None

    # Si origen y destino son iguales, no hay conversión necesaria
    if origen == destino:
        return valor

    # Primero convertimos a Celsius como unidad intermedia
    if origen == 'F':
        celsius = (valor - 32) * 5/9
    elif origen == 'K':
        celsius = valor - 273.15
    else:  # origen es 'C'
        celsius = valor

    # Luego convertimos de Celsius a la unidad de destino
    if destino == 'F':
        return celsius * 9/5 + 32
    elif destino == 'K':
        return celsius + 273.15
    else:  # destino es 'C'
        return celsius

# Ejemplos de uso
print(convertir_temperatura(25, 'C', 'F'))    # Imprime: 77.0
print(convertir_temperatura(98.6, 'F', 'C'))  # Imprime: 37.0
print(convertir_temperatura(0, 'C', 'K'))     # Imprime: 273.15
print(convertir_temperatura(20, 'X', 'Y'))    # Imprime: None

# Docstrings
def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b

# Estructura básica de un docstring
def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.

    Suma todos los números de la lista y divide el resultado
    entre la cantidad de elementos.

    Args:
        numeros: Una lista de valores numéricos

    Returns:
        El promedio como valor flotante

    Ejemplo:
        >>> calcular_promedio([1, 2, 3, 4])
        2.5
    """
    return sum(numeros) / len(numeros)

    # Accediendo a los docstrings
    # Acceder al docstring directamente
print(calcular_promedio.__doc__)

# O usar la función help
help(calcular_promedio)

# Estilos de docstrings
# Estilo Google
def validar_email(email):
    """
    Verifica si una dirección de correo electrónico tiene formato válido.

    Args:
        email (str): La dirección de correo a validar

    Returns:
        bool: True si el formato es válido, False en caso contrario

    Raises:
        TypeError: Si email no es una cadena de texto
    """
    if not isinstance(email, str):
        raise TypeError("El email debe ser una cadena de texto")
    return "@" in email and "." in email.split("@")[-1]

    

