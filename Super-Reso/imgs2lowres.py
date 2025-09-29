#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:58:44 2024

@author: pfi

input: aereal images
output: crops & low resolution crops

"""

import cv2
import os


def create_folder_if_not_exists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def save_image(path, image):
    resized = cv2.resize(image, (512,512), cv2.INTER_AREA)
    cv2.imwrite(path, resized)

def process_crop(image, start_x, start_y, crop_size):
    crop = image[start_y:start_y + crop_size, start_x:start_x + crop_size]
    return crop

def reduce_resolution(image, factor):
    height, width = image.shape[:2]
    new_height = height // factor
    new_width = width // factor    
    return cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)

def process_images(input_folder, output_folder, output_folder_lowres, crop_size=1000, reduction_factor=6):
    create_folder_if_not_exists(output_folder)
    create_folder_if_not_exists(output_folder_lowres)

    file_list = os.listdir(input_folder)

    for filename in file_list:
        if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.tif')):
            image_path = os.path.join(input_folder, filename)
            img = cv2.imread(image_path)
            height, width, _ = img.shape

            for y in range(0, height, crop_size):
                for x in range(0, width, crop_size):
                    # crop image
                    crop = process_crop(img, x, y, crop_size)

                    # Apply reduction function
                    grayscale_crop = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
                    #reduced_crop = reduce_resolution(grayscale_crop, reduction_factor)
                    reduced_crop = grayscale_crop

                    # Save the reduced crop
                    output_name = f"{os.path.splitext(filename)[0]}_{x//crop_size + 1}_{y//crop_size + 1}.png"
                    output_path_lowres = os.path.join(output_folder_lowres, output_name)
                    save_image(output_path_lowres, reduced_crop)
                    print(f"save: {output_path_lowres}")

                    # Save original crop
                    output_path = os.path.join(output_folder, output_name)
                    save_image(output_path, crop)
                    print(f"save: {output_path}")
                    
# Path to the directory containing images
#input_folder = "/home/pfi/PFI/PFISAT/IMAGES/leida"
input_folder = "/home/pfi/PFI/PFISAT/IMAGES/RGB_vertederos_recortes"
# Output directory for processed images
#output_folder = "/home/pfi/PFI/PFISAT/CROPS/leida/crops"
output_folder = "/home/pfi/PFI/PFISAT/CROPS/RGB_vertederos_crops"
#output_folder_lowres = "/home/pfi/PFI/PFISAT/CROPS/leida/crops_lowres"
output_folder_lowres = "/home/pfi/PFI/PFISAT/CROPS/RGB_vertederos_crops_lowres"

process_images(input_folder, output_folder, output_folder_lowres)

print("End")
