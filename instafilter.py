from PIL import Image

#load images to objecta
base_img = Image.open("pic4.jpg")
img_filter = Image.open("pic2.jpg")
# set output image size
size = (360,260)
# resize all images
base_img = base_img.resize(size)
img_filter = img_filter.resize(size)

r,g,b = base_img.split()
R,G,B = img_filter.split()
#merge rgb
im = Image.merge("RGB", (R,g,b))
# im.show()
im.save("image1.jpg","JPG")