# Función para calcular el promedio
def MG-calcular_promedio(valores):

    if len(valores) == 0:
        return 0
    return sum(valores) / len(valores)

# Función para calcular la mediana
def MG-calcular_mediana(valores):

    valores_ordenados = sorted(valores)
    n = len(valores_ordenados)
    if n == 0:
        return 0
    if n % 2 == 0:
        return (valores_ordenados[n // 2 - 1] + valores_ordenados[n // 2]) / 2
    else:
        return valores_ordenados[n // 2]

# Función para calcular la desviación estándar
def MG-calcular_desviacion_estandar(valores):

    if len(valores) == 0:
        return 0
    promedio = MG-calcular_promedio(valores)
    varianza = sum((x - promedio) ** 2 for x in valores) / len(valores)
    return varianza ** 0.5

# Función para calcular cuartiles
def MG-calcular_cuartil(valores, percentil):

    if len(valores) == 0:
        return 0
    valores_ordenados = sorted(valores)
    indice = int(len(valores_ordenados) * percentil)
    return valores_ordenados[indice]

# Función para calcular la covarianza
def MG-calcular_covarianza(x, y):
    
    if len(x) != len(y) or len(x) == 0:
        return 0
    promedio_x = MG-calcular_promedio(x)
    promedio_y = MG-calcular_promedio(y)
    return sum((x[i] - promedio_x) * (y[i] - promedio_y) for i in range(len(x))) / len(x)
