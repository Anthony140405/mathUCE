Algoritmo ResolverEcuacionCuadratica
    // Este algoritmo resuelve la ecuación cuadrática ax^2 + bx + c = 0
    
    Definir a, b, c, discriminante, x1, x2 Como Real
    
    Escribir "Ingrese el coeficiente a: "
    Leer a
    
    Escribir "Ingrese el coeficiente b: "
    Leer b
    
    Escribir "Ingrese el coeficiente c: "
    Leer c
    
    // Calcular el discriminante
    discriminante <- b^2 - 4*a*c
    
    // Determinar las soluciones basadas en el discriminante
    Si discriminante > 0 Entonces
        // Dos soluciones reales distintas
        x1 <- (-b + RaizCuadrada(discriminante)) / (2*a)
        x2 <- (-b - RaizCuadrada(discriminante)) / (2*a)
        Escribir "Las soluciones son:"
        Escribir "x1 = ", x1
        Escribir "x2 = ", x2
    FinSi
    
    Si discriminante = 0 Entonces
        // Una solución real doble
        x1 <- -b / (2*a)
        Escribir "La solución doble es:"
        Escribir "x = ", x1
    FinSi
    
    Si discriminante < 0 Entonces
        // Soluciones complejas
        parte_real <- -b / (2*a)
        parte_imaginaria <- RaizCuadrada(Abs(discriminante)) / (2*a)
        Escribir "Las soluciones son complejas:"
        Escribir "x1 = ", parte_real, " + ", parte_imaginaria, "i"
        Escribir "x2 = ", parte_real, " - ", parte_imaginaria, "i"
    FinSi
    
FinAlgoritmo
