from PIL import Image

img = Image.open('qrcodeteste.jpeg').convert('L').resize((50,50))
pixels = img.load()
width, height = img.size
matriz = []

for y in range(height):
    row = []
    for x in range(width):
        valor = pixels[x, y]
        if valor < 128:
            row.append(1)
        else:
            row.append(0)
    matriz.append(row)
