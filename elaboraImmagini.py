# Image Editor
# pip install pillow
from PIL import Image
from PIL import ImageDraw
# Combine Image
img1 = Image.open('1.jpg')
img2 = Image.open('2.jpg')

w = img1.size[0] + img2.size[0]
h = max(img1.size[1], img2.size[1])
im = Image.new("RGBA", (w, h))

im.paste(img1)
im.paste(img2, (img1.size[0], 0))
im.show()
