import pyautogui
from time import sleep
from PIL import Image
from math import sqrt

palette = {
    (0, 0, 0): (40, 975), (1, 1, 1): (1870, 975), (128, 128, 128): (95, 975),
    (169, 169, 169): (150, 975), (211, 211, 211): (205, 975), (255, 255, 255): (270, 975),
    (139, 0, 0): (330, 975), (255, 0, 0): (400, 975), (255, 165, 0): (450, 975),
    (255, 215, 0): (510, 975), (255, 255, 0): (575, 975), (255, 255, 224): (630, 975),
    (0, 100, 0): (690, 975), (0, 128, 0): (750, 975), (144, 238, 144): (810, 975),
    (0, 80, 80): (870, 975), (0, 128, 128): (930, 975), (173, 216, 230): (980, 975),
    (0, 0, 139): (1050, 975), (0, 0, 255): (1100, 975), (0, 255, 255): (1160, 975),
    (75, 0, 130): (1230, 975), (138, 43, 226): (1280, 975), (100, 0, 100): (1350, 975),
    (128, 0, 128): (1400, 975), (221, 160, 221): (1460, 975), (255, 20, 147): (1530, 975),
    (255, 192, 203): (1580, 975), (255, 182, 193): (1640, 975), (101, 67, 33): (1700, 975),
    (165, 42, 42): (1760, 975), (245, 245, 220): (1820, 975),
}

def set_matriz(img_rgba):
    width, height = img_rgba.size
    pixels = img_rgba.load()
    matriz = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(pixels[x, y])
        matriz.append(row)
    return matriz

def createPalette(matriz):
    cores = []
    for row in matriz:
        for i in row:
            if i not in cores:
                cores.append(i)

    print(cores)

def pixeis(matriz):
    pix = 0
    for row in matriz:
        for i in row:
            if i in palette:
                pix += 1
    print(pix)
pallete_rgb_opacas = [rgb for rgb in palette.keys() if rgb != (1, 1, 1)]
def find_closest_color_rgb(rgb_tuple):
    min_distance = float('inf')
    closest_rgb = None
    for palette_color in pallete_rgb_opacas:
        distance = sqrt(((rgb_tuple[0] - palette_color[0]) ** 2) + ((rgb_tuple[1] - palette_color[1]) ** 2) + ((rgb_tuple[2] - palette_color[2]) ** 2))
        if distance < min_distance:
            min_distance = distance
            closest_rgb = palette_color
    return closest_rgb

def set_matriz_colorida(img_rgba):
    width, height = img_rgba.size
    pixels = img_rgba.load()
    matriz = []
    pos_transparente = palette[(1, 1, 1)]
    for y in range(height):
        row = []
        for x in range(width):
            r, g, b, a = pixels[x, y]
            if a < 128:
                pos_cor = pos_transparente
            else:
                closest_rgb = find_closest_color_rgb((r, g, b))
                pos_cor = palette[closest_rgb]
            row.append(pos_cor)
        matriz.append(row)
    return matriz

if __name__ == '__main__':
    img = Image.open('carapoke.png').convert('RGBA').resize((64,64))
    matriz = set_matriz_colorida(img)
    createPalette(matriz)

