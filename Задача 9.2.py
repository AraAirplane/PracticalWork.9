from PIL import Image

image = Image.open('photo.jpg')

reduced = image.reduce(3)
reduced.save('reduced_photo.jpg')

flip_h = image.transpose(Image.FLIP_LEFT_RIGHT)
flip_h.save('horizontal_photo.jpg')

flip_v = image.transpose(Image.FLIP_TOP_BOTTOM)
flip_v.save('vertical_photo.jpg')
