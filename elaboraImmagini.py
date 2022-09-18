# Image Editor
# pip install pillow
from PIL import Image
from PIL import ImageDraw
# Combine Image
img1 = Image.open('1.jpg')
img2 = Image.open('2.jpg')
combine = Image.blend(img1, img2, 0.5)
combine.show()