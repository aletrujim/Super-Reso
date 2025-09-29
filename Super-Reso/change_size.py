import os
from PIL import Image

def resize_to_square(input_dir, output_dir, size):
    # Comprobar si el directorio de salida existe, si no, crearlo
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Recorrer todos los archivos en el directorio de entrada
    for filename in os.listdir(input_dir):
        if filename.endswith('.jpg'):
            # Abrir la imagen
            image_path = os.path.join(input_dir, filename)
            img = Image.open(image_path)

            # Obtener dimensiones originales de la imagen
            original_width, original_height = img.size

            # Calcular el tamaño de recorte para hacerlo cuadrado
            crop_size = min(original_width, original_height)

            # Recortar la imagen al tamaño cuadrado
            left = (original_width - crop_size) / 2
            top = (original_height - crop_size) / 2
            right = (original_width + crop_size) / 2
            bottom = (original_height + crop_size) / 2
            img_cropped = img.crop((left, top, right, bottom))

            # Redimensionar la imagen al tamaño deseado
            img_resized = img_cropped.resize((size, size))

            # Guardar la imagen en el directorio de salida
            output_path = os.path.join(output_dir, filename)
            img_resized.save(output_path)

            print(f"Imagen {filename} redimensionada y guardada como {output_path}")

# Directorio de entrada y salida
input_directory = "/home/pfi/PFI/PFISAT/CODE/code/ESRGAN/Super-Resolution-Space/data/crops"
output_directory = "/home/pfi/PFI/PFISAT/CODE/code/ESRGAN/Super-Resolution-Space/data/crops_train"

# Tamaño deseado (512x512 píxeles)
size = 512

# Llamar a la función para redimensionar imágenes
resize_to_square(input_directory, output_directory, size)

