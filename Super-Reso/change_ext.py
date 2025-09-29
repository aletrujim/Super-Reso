import os
from PIL import Image

def convertir_png_a_jpg(path):
    # Iterar sobre todos los archivos en el directorio
    for archivo in os.listdir(path):
        # Comprobar si el archivo tiene la extensión .png
        if archivo.endswith(".png"):
            # Abrir la imagen usando Pillow
            img = Image.open(os.path.join(path, archivo))
            # Convertir la imagen a modo RGB si no lo está
            img = img.convert("RGB")
            # Construir el nuevo nombre de archivo con la extensión .jpg
            nuevo_nombre = os.path.splitext(archivo)[0] + ".jpg"
            # Guardar la imagen como .jpg
            img.save(os.path.join(path, nuevo_nombre), "JPEG")
            print(f"Se ha convertido {archivo} a {nuevo_nombre}")

# Ruta del directorio donde se encuentran los archivos
#ruta = "/home/pfi/PFI/PFISAT/CODE/code/ESRGAN/Super-Resolution-Space/data/crops_lowres"
ruta = "/home/pfi/PFI/PFISAT/CODE/code/ESRGAN/Super-Resolution-Space/results/RGB_vertederos_crops_lowres"

# Llamar a la función para convertir los archivos PNG a JPG en el directorio especificado
convertir_png_a_jpg(ruta)

