# Imports
from exif import Image
import PIL.Image

# Image Info
img_path = 'images/Image1.jpg'
with open(img_path, 'rb') as src:
    img = Image(src)
    print(src.name, img)

image = PIL.Image.open(img_path)
print(img)

if img.has_exif:
    info = f"✅ -> has the EXIF {img.exif_version}"
else:
    info = "{❌} -> Does not contain any EXIF info"
print(f"Image {src.name}: {info}")

# Read
with open(img_path, "rb") as src:
    img = Image(src)

img.list_all()
