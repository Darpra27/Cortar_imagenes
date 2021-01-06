# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 15:26:42 2020

@author: David
"""
try:
    import Image
except ImportError:
    from PIL import Image

image_file = "G:/Mi unidad/Instabot/Programa Bot/Main/pics/1-Thitobb.jpeg"

image = Image.open(image_file)

print(image.size)
xcenter = image.width/2
ycenter = image.height/2
cropped = image.crop((0, ycenter-xcenter, image.width, image.width))
cropped.save(image_file)
cropped.show()
