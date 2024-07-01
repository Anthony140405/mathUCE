
# Definir variables para el ejemplo
numero = 15
es_par = (numero % 2 == 0)
es_positivo = (numero > 0)

# Ejemplo de operador 'and'
resultado_and = es_par and es_positivo
print(f"¿Es {numero} un número par y positivo?: {resultado_and}")

# Ejemplo de operador 'or'
resultado_or = es_par or es_positivo
print(f"¿Es {numero} un número par o positivo (o ambas)?: {resultado_or}")

# Ejemplo de operador 'not'
resultado_not = not es_par
print(f"¿{numero} no es un número par?: {resultado_not}")

# Ejemplo combinado de operadores lógicos
resultado_combinado = (numero > 10 and numero <= 20) or (numero < 0)
print(f"¿{numero} está en el rango de 11 a 20 o es negativo?: {resultado_combinado}")

# Otra manera de usar operadores lógicos en una sola expresión
resultado_otra = 10 < numero <= 20 or numero < 0
print(f"¿{numero} está en el rango de 11 a 20 o es negativo?: {resultado_otra}")

# Ejemplo de negación con operadores lógicos
resultado_negacion = not (numero % 2 == 0)
print(f"¿{numero} es impar?: {resultado_negacion}")


