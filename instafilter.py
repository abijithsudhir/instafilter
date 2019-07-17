from PIL import Image

base_img = Image.open("pic4.jpg")
img_filter = Image.open("pic2.jpg")

size = (360,260)

base_img = base_img.resize(size)
img_filter = img_filter.resize(size)

r,g,b = base_img.split()
R,G,B = img_filter.split()

im = Image.merge("RGB", (R,g,b))
im.show()
