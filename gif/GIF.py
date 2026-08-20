



import imageio.v3 as iio
from PIL import Image


filenames = ['image1.jpg', 'image2.jpg', 'image3.jpg']
images = []

for filename in filenames:
    image = Image.open(filename)
    image = image.resize((500, 500))
    images.append(image)

    
iio.imwrite('my_gif.gif', images, duration=500, loop=0)

