import pyautogui
from time import sleep
from PIL import Image
from math import sqrt

def cor_mais_proxima(cor, paleta):
    r1, g1, b1 = cor
    menor_dist = float('inf')
    cor_proxima = None

    for cor_paleta, posicao in paleta.items():
        r2, g2, b2 = cor_paleta[:3]  # ignora canal alpha se existir
        dist = sqrt((r1 - r2)**2 + (g1 - g2)**2 + (b1 - b2)**2)
        if dist < menor_dist:
            menor_dist = dist
            cor_proxima = posicao

    return cor_proxima  # tupla (x, y)

img = Image.open('coracao.png').resize((15, 15))
matriz = []
quantizada = img.quantize(colors=32).convert("RGB")
pixels = quantizada.load()
width, height = quantizada.size

pallete = {
    (0, 0, 0): (40, 975),         # Black
    (64, 64, 64): (95, 975),      # Dark gray
    (128, 128, 128): (150, 975),  # Gray
    (192, 192, 192): (205, 975),  # Light Gray
    (255, 255, 255): (270, 975),  # White
    (128, 0, 0): (330, 975),      # Deep Red
    (255, 0, 0): (400, 975),      # Red
    (255, 128, 0): (450, 975),    # Orange
    (255, 204, 0): (510, 975),    # Gold
    (255, 255, 0): (575, 975),    # Yellow
    (255, 255, 153): (630, 975),  # Light yellow
    (0, 100, 0): (690, 975),      # Dark green
    (0, 255, 0): (750, 975),      # Green
    (153, 255, 153): (810, 975),  # Light green
    (0, 128, 128): (870, 975),    # Dark teal
    (0, 255, 255): (930, 975),    # Teal
    (153, 255, 255): (980, 975),  # Light teal
    (0, 0, 139): (1050, 975),     # Dark blue
    (0, 0, 255): (1100, 975),     # Blue
    (0, 255, 255): (1160, 975),   # Cyan
    (75, 0, 130): (1230, 975),    # Indigo
    (147, 112, 219): (1280, 975), # Light indigo
    (75, 0, 130): (1350, 975),    # Dark purple
    (128, 0, 128): (1400, 975),   # Purple
    (216, 191, 216): (1460, 975), # Light purple
    (139, 0, 139): (1530, 975),   # Dark pink
    (255, 105, 180): (1580, 975), # Pink
    (255, 182, 193): (1640, 975), # Light pink
    (101, 67, 33): (1700, 975),   # Dark brown
    (150, 75, 0): (1760, 975),    # Brown
    (245, 245, 220): (1820, 975), # Beige
    (0, 0, 0, 0): (1870, 975),    # Transparent (opcional)
}

# Abrir imagem
img = Image.open("coracao.png").convert("RGB")

# Redimensionar se quiser acelerar
img = img.resize((50, 50))

pixels = img.load()
width, height = img.size

matriz = []

for y in range(height):
    linha = []
    for x in range(width):
        cor = pixels[x, y]
        pos_cor = cor_mais_proxima(cor, pallete)  # retorna (x, y) do seletor
        linha.append(pos_cor)
    matriz.append(linha)
for i in matriz:
    print(i)