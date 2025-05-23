from PIL import Image

image = Image.open("photo.jpg")
watermark = Image.open("watermark.png")

image.paste(watermark, (200, 200), watermark)
image.save("photo_watermark.jpg")
