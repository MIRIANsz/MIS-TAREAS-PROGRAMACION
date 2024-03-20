

# Diccionario
informacion_personal = {
    'nombre': 'Mirian Sarango',
    'edad': 21,
    'ciudad': 'Lago agrio',
    'profesion': 'estudiante',
}
print(informacion_personal)

# Modificar el valor
informacion_personal['ciudad'] = 'Santo Domingo'
print(informacion_personal)

# Agregar nueva clave:valor
informacion_personal['profesion'] = 'estudiante'
print(informacion_personal)

# Verificar telefono y agregar
if 'telefono' in informacion_personal:
    print(informacion_personal['telefono'])
else:
    informacion_personal['telefono'] = '0999990190'
print(informacion_personal)

# Eliminar edad
del informacion_personal['edad']
print(informacion_personal)
