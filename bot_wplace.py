import pyautogui
from time import sleep
from PIL import Image
from math import sqrt

# --- FUNÇÕES E PALETAS DO MODO COLORIDO (ANTIGO) ---
pallete_posicoes = {
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
pallete_rgb_opacas = [rgb for rgb in pallete_posicoes.keys() if rgb != (1, 1, 1)]

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
    pos_transparente = pallete_posicoes[(1, 1, 1)]
    for y in range(height):
        row = []
        for x in range(width):
            r, g, b, a = pixels[x, y]
            if a < 128:
                pos_cor = pos_transparente
            else:
                closest_rgb = find_closest_color_rgb((r, g, b))
                pos_cor = pallete_posicoes[closest_rgb]
            row.append(pos_cor)
        matriz.append(row)
    return matriz

def draw_colorido(canvas_x, canvas_y, pixel_size, matriz):
    count = 0
    last_color_pos = None
    pos_transparente = pallete_posicoes[(1, 1, 1)]
    print("Iniciando desenho colorido. Começa em 5 segundos...")
    sleep(5)
    for y, row in enumerate(matriz):
        for x, cor_pos in enumerate(row):
            if cor_pos == pos_transparente: continue
            if cor_pos != last_color_pos:
                pyautogui.moveTo(cor_pos); pyautogui.click(); sleep(0.1)
                last_color_pos = cor_pos
            if count != 0 and count % 3 == 0: pyautogui.moveTo(1000, 1030); sleep(0.1); pyautogui.click(); sleep(1); pyautogui.click(); sleep(1)
            px = int(canvas_x + x * pixel_size); py = int(canvas_y + y * pixel_size)
            pyautogui.moveTo(px, py); pyautogui.click(); count += 1; sleep(0.001)
    print("Desenho colorido concluído! ✅")

# --- NOVAS FUNÇÕES DO MODO BINÁRIO ---
def set_matriz_binaria(imagem, limiar=128):
    img_cinza = imagem.convert('L')
    width, height = img_cinza.size
    pixels = img_cinza.load()
    matriz = []
    print(f"Gerando matriz binária com limiar de brilho < {limiar}...")
    for y in range(height):
        row = []
        for x in range(width):
            brilho = pixels[x, y]
            if brilho < limiar: row.append(1)
            else: row.append(0)
        matriz.append(row)
    return matriz

def draw_binario(canvas_x, canvas_y, pixel_size, matriz_binaria):
    count = 0
    pixels_a_desenhar = sum(row.count(1) for row in matriz_binaria)
    print(f"Iniciando desenho binário. Total de pixels a pintar: {pixels_a_desenhar}")
    print("Posicione o mouse em local seguro! O desenho começa em 3 segundos...")
    sleep(3)
    for y, row in enumerate(matriz_binaria):
        for x, valor in enumerate(row):
            if valor == 0: continue
            px = int(canvas_x + x * pixel_size); py = int(canvas_y + y * pixel_size)
            pyautogui.moveTo(px, py); pyautogui.click(); count += 1; sleep(0.01)
            if count != 0 and count % 300 == 0: print(f"Cooldown..."); sleep(30)
    print("Desenho binário concluído! ✅")

# --- BLOCO PRINCIPAL COM MENU DE ESCOLHA ---
if __name__ == '__main__':
    print(r"""
 _              __  __       _                  __      _      _ 
| |__  _   _   |  \/  | __ _| |_ ___ _   _ ___ / _|_ __| |_ __| |
| '_ \| | | |  | |\/| |/ _` | __/ _ \ | | / __| |_| '__| __/ _` |
| |_) | |_| |  | |  | | (_| | ||  __/ |_| \__ \  _| |  | || (_| |
|_.__/ \__, |  |_|  |_|\__,_|\__\___|\__,_|___/_| |_|   \__\__,_|
       |___/                                                    
""")
    
    # --- MENU DE ESCOLHA ---
    modo = ''
    while modo not in ['1', '2']:
        print("\nEscolha o modo de desenho:")
        print("  1 - Modo Colorido")
        print("  2 - Modo Binário")
        modo = input("Digite 1 ou 2 e pressione Enter: ")

    # --- CONFIGURAÇÕES GERAIS ---
    IMAGEM_ARQUIVO = "./images/coracao.png"
    LARGURA_DESENHO = 27  # Pixels
    ALTURA_DESENHO = 50   # Pixels
    
    canvas_x, canvas_y = 525, 35
    pixel_size = 9
    pyautogui.FAILSAFE = True

    # --- LÓGICA DE EXECUÇÃO BASEADA NA ESCOLHA ---
    if modo == '1':
        print("\n--- MODO COLORIDO SELECIONADO ---")
        img_original_rgba = Image.open(IMAGEM_ARQUIVO).convert("RGBA")
        img_resized = img_original_rgba.resize((LARGURA_DESENHO, ALTURA_DESENHO), Image.Resampling.NEAREST)
        matriz_final = set_matriz_colorida(img_original_rgba)
        draw_colorido(canvas_x, canvas_y, pixel_size, matriz_final)

    elif modo == '2':
        print("\n--- MODO BINÁRIO SELECIONADO ---")
        img_original = Image.open(IMAGEM_ARQUIVO)
        img_resized = img_original.resize((LARGURA_DESENHO, ALTURA_DESENHO), Image.Resampling.NEAREST)
        matriz_final = set_matriz_binaria(img_resized, limiar=180) # Ajuste o limiar se necessário
        draw_binario(canvas_x, canvas_y, pixel_size, matriz_final)
