# Nombre del archivo
nombre_archivo = "ejemplo6.txt"

# Contenido que quieres escribir
contenido = "Hola, este es un archivo de texto creado con Python version 6."

# Crear y escribir en el archivo
with open(nombre_archivo, "w", encoding="utf-8") as archivo:
    archivo.write(contenido)

print(f"Archivo '{nombre_archivo}' creado con éxito cambio 6.")
