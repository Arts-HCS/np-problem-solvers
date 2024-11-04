import time
import itertools
import random

# Función del problema del viajante
def generar_matriz_distancias(n):
    # Genera una matriz de distancias aleatorias para n ciudades
    return [[0 if i == j else random.randint(10, 50) for j in range(n)] for i in range(n)]

def calcular_distancia_total(ruta, distancias):
    distancia_total = 0
    for i in range(len(ruta)):
        distancia_total += distancias[ruta[i]][ruta[(i + 1) % len(ruta)]]
    return distancia_total

def tsp(distancias):
    ciudades = list(range(len(distancias)))
    mejor_distancia = float('inf')

    for ruta in itertools.permutations(ciudades):
        distancia = calcular_distancia_total(ruta, distancias)
        if distancia < mejor_distancia:
            mejor_distancia = distancia

    return mejor_distancia

# Función del problema de la mochila
def mochila(weights, values, capacity):
    n = len(weights)
    dp = [[0 for i in range(capacity + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Prueba de tiempo con aumento de variables
def medir_tiempo(func, *args):
    inicio = time.time()
    resultado = func(*args)
    fin = time.time()
    duracion = fin - inicio
    return duracion, resultado

# Variables iniciales y capacidad
ciudades = 4
articulos = 3
capacity = 50
tiempo_limite = 10 

# Bucle de prueba
while True:
    # Prueba del viajante con incremento de ciudades
    distancias = generar_matriz_distancias(ciudades)
    tiempo_tsp, _ = medir_tiempo(tsp, distancias)
    
    if tiempo_tsp > tiempo_limite:
        print(f"El problema del viajante con {ciudades} ciudades excede el límite de {tiempo_limite} segundos.")
        break
    else:
        print(f"El problema del viajante con {ciudades} ciudades se resolvió en {tiempo_tsp:.2f} segundos.")
    ciudades += 1  # Incremento de ciudades

    # Prueba de la mochila con incremento de artículos
    weights = random.sample(range(1, 100000000), articulos) 
    values = random.sample(range(10, 100000000), articulos)
    tiempo_mochila, _ = medir_tiempo(mochila, weights, values, capacity)
    
    if tiempo_mochila > tiempo_limite:
        print(f"El problema de la mochila con {articulos} artículos excede el límite de {tiempo_limite} segundos.")
        break
    else:
        print(f"El problema de la mochila con {articulos} artículos se resolvió en {tiempo_mochila:.2f} segundos.")
    
    articulos += 500  
