import itertools

distancias = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]


def calcular_distancia_total(ruta):
    distancia_total = 0
    for i in range(len(ruta)):
        distancia_total += distancias[ruta[i]][ruta[(i + 1) % len(ruta)]]
    return distancia_total

def tsp():
    ciudades = list(range(len(distancias)))
    mejores_ruta = None
    mejor_distancia = float('inf')

    for ruta in itertools.permutations(ciudades):
        distancia = calcular_distancia_total(ruta)
        if distancia < mejor_distancia:
            mejor_distancia = distancia
            mejores_ruta = ruta

    return mejores_ruta, mejor_distancia

mejores_ruta, mejor_distancia = tsp()
print("Mejor ruta:", mejores_ruta)
print("Mejor distancia:", mejor_distancia)
