from PIL import Image, ImageFilter
import os

newfolder = 'filtered'
os.makedirs(newfolder, exist_ok=True)

for i in range(1, 6):
    photo = f'nofilter/{i}.jpg'
    image = Image.open(photo)
    newphoto = image.filter(ImageFilter.CONTOUR)
    newphoto.save(f'filtered/filter_{i}.jpg')