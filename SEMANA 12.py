import np

# Definir las ciudades, días de la semana y semanas

ciudades = \
    {'Ciudad A', 'Ciudad B', 'Ciudad C'}
dias_semana =\
    ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = \
    ['Semana 1', 'Semana 2', 'Semana 3']

# Crear una matriz 3D para almacenar las temperaturas

matriz_temperaturas = np.random.randint(20, 30, size=(len(ciudades), len(dias_semana), len(semanas)))

# Calcular el promedio de temperaturas por ciudad y semana

promedios = np.mean(matriz_temperaturas, axis=1)

# Mostrar el promedio de temperaturas para cada ciudad y semana

for i, ciudad in enumerate(ciudades):
    print(f"\nPromedio de temperaturas para {ciudad}:")
    for j, semana in enumerate(semanas):
        promedio_semana = promedios[i, j]
        print(f"{semana}: {promedio_semana:.2f}°C")
