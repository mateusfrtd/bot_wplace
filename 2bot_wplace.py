import pyautogui
from time import sleep
from PIL import Image
from math import sqrt

palette = {
(17, 21, 22, 255): (40, 930), 
(36, 43, 46, 255): (100, 930), 
(69, 81, 87, 255): (1765, 980), 
(52, 62, 66, 255): (1700, 980), 
(96, 116, 125, 255): (155, 930), 
(12, 15, 15, 255): (40, 930), 
(0, 0, 0, 255): (40, 930)
}

    

def set_matriz_colorida(img_rgba):
    width, height = img_rgba.size
    pixels = img_rgba.load()
    matriz = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(pixels[x, y])
        matriz.append(row)
    return matriz

def draw(canvas_x, canvas_y, pixel_size, matriz):
    last_color_pos = None
    print("Iniciando desenho colorido. Começa em 5 segundos...")
    sleep(5)
    count = 0
    for y, row in enumerate(matriz):
        for x, cor in enumerate(row):
            if cor == (0, 0, 0, 0):
                continue

            if count >= 353:
                for i in range(177):
                    print(f'Volta em {i} minutos!')
                    sleep(60)

                _ = input('Press ENTER')
                count = 0

            cor_pos = palette[cor]
            if cor_pos != last_color_pos:
                pyautogui.moveTo(cor_pos); pyautogui.click()
                last_color_pos = cor_pos
                sleep(0.1)

            px = int(canvas_x + x * pixel_size)
            py = int(canvas_y + y * pixel_size)
            pyautogui.moveTo(px, py)
            pyautogui.click()
            sleep(0.001)
            count += 1

    print("Desenho colorido concluído! ✅")

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


if __name__ == '__main__':
    canvas_x, canvas_y = 51, 0
    #pixel_size = float(input('pixel size: '))
    #width = int(input("Width: "))
    #height = int(input('height: '))
    pyautogui.FAILSAFE = True
    img = Image.open('carapoke.png').convert('RGBA')
    #img_resized = img.resize((width, height), Image.Resampling.NEAREST)
    matriz = set_matriz_colorida(img)
    #draw(canvas_x, canvas_y, pixel_size, matriz)
    print(img.size)
    pixeis(matriz)

    

    

    
            
    