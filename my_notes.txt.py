# Escritura de archivo de texto
with open("my_notes.txt", "w") as file:
    # Escribir al menos tres líneas de notas personales
    file.write("Nota 1: Recordar comprar leche en el supermercado.\n")
    file.write("Nota 2: Llamar al médico para programar una cita.\n")
    file.write("Nota 3: Presentar la tarea de Fundamentos de Programación.\n")

# Lectura de archivo de texto
with open("my_notes.txt", "r") as file:
    # Leer el contenido del archivo línea por línea
    lines = file.readlines()
    # Mostrar en la consola cada línea leída
    for line in lines:
        print(line.strip())  # Eliminar los saltos de línea adicionales

# Cierre de archivo

# No es necesario cerrar explícitamente el archivo al usar el contexto "with",
# ya que se cierra automáticamente al salir del bloque "with".
