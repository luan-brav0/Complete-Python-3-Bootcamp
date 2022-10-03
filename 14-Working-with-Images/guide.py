from PIL import Image

mac = Image.open('example.jpg')

mac = mac.crop((850,850,1200,1200))
mac.show()