import math

# Función para resolver la ecuación cuadrática
def resolver_ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    
    # Caso 1: Discriminante positivo (dos soluciones reales distintas)
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return x1, x2
    
    # Caso 2: Discriminante igual a cero (una solución real doble)
    elif discriminante == 0:
        x = -b / (2*a)
        return x, x
    
    # Caso 3: Discriminante negativo (soluciones complejas)
    else:
        parte_real = -b / (2*a)
        parte_imaginaria = math.sqrt(-discriminante) / (2*a)
        x1 = complex(parte_real, parte_imaginaria)
        x2 = complex(parte_real, -parte_imaginaria)
        return x1, x2

# Ejemplo de uso:
if __name__ == "__main__":
    # Pedir al usuario que ingrese los coeficientes a, b y c
    a = float(input("Ingrese el coeficiente a: "))
    b = float(input("Ingrese el coeficiente b: "))
    c = float(input("Ingrese el coeficiente c: "))
    
    # Resolver la ecuación cuadrática
    soluciones = resolver_ecuacion_cuadratica(a, b, c)
    
    # Mostrar las soluciones
    print("Las soluciones de la ecuación cuadrática son:")
    if isinstance(soluciones[0], complex):
        print(f"x1 = {soluciones[0]}")
        print(f"x2 = {soluciones[1]}")
    else:
        print(f"x1 = {soluciones[0]}")
        print(f"x2 = {soluciones[1]}")
