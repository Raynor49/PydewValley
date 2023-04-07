import os
import pygame

def import_folder(path):
    surface_list = []

    try:
        for _, __, img_files in os.walk(path):
            for image in img_files:
                full_path = os.path.join(path, image)
                image_surf = pygame.image.load(full_path).convert_alpha()
                surface_list.append(image_surf)
    except Exception as e:
        print("an exception has occurred : " + str(e))

    return surface_list