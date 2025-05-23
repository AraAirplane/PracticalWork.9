from PIL import Image
image = Image.open("photo.jpg")
image.show()
print("Имя файла:", image.filename)
print("Формат:", image.format)
print("Размер:", image.height,"*",image.width)
print(f"Цветовая модель: {image.mode}")
