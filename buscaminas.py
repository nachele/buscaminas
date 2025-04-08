import pygame
import random
pygame.init()
pantalla = pygame.display.set_mode((400,400))
campo =[]
filas = 8
columnas = 8
x = random.randint(0,7)
y = random.randint(0,7)
running = True
bombasColocadas = 0
anchoCelda = 50
altoCelda = 50
imagen = pygame.image.load("imgBusca/1.png")
imagenTrans = pygame.transform.scale(imagen,(50,50))
mousePos = pygame.mouse.get_pos()
teclaMouse = pygame.mouse.get_pressed()
bombita = 0
fuente = pygame.font.SysFont("Arial", 20)
color_texto = (0,0,225)
texto = fuente.render(str(3),True, color_texto)

class Casilla:
    def __init__(self,x,y,imagen):
        self.x =( x * anchoCelda)
        self.y = (y * altoCelda)
        self.bomba = False
        self.exploto = False
        self.imagen =pygame.transform.scale(pygame.image.load(imagen),(anchoCelda,altoCelda)) 
        self.descubierto = False
        self.bombasAlrededor = 0
    def pintar(self):
        pantalla.blit(self.imagen, (self.x, self.y))

def crearCampo():
    global campo
    global Casilla
    campo = [[Casilla(i,x,"imgBusca/0.png") for i in range(columnas)] for x in range(filas)]
def crearBombas():
    global campo, columnas, filas, bombasColocadas
    while bombasColocadas < 8:
        x = random.randint(0,7)
        y = random.randint(0,7)
        if campo[y][x].bomba == False:
            campo[y][x].bomba = True
            bombasColocadas += 1



def casillaBomba():
    global campo, anchoCelda, altoCelda, mousePos, teclaMouse
    mousePos = pygame.mouse.get_pos()
    teclaMouse = pygame.mouse.get_pressed()
    x = int((mousePos[0])/ anchoCelda)
    y = int((mousePos[1]) / altoCelda)

   # print(int(mousePos[0]/ anchoCelda))
    if teclaMouse[0] and x >= 0 and x <= 7 and y >= 0 and y <= 7:
        if campo[y][x].bomba:
            campo[y][x].imagen = pygame.transform.scale(pygame.image.load("imgBusca/1.png"),(anchoCelda,altoCelda))


#VOY POR AQUI
array0Bombas = []
arrayBombas = []
#array0Bombas = [[None for i in range(filas)] for x in range(columnas)]
def casillaSinBomba():
    global campo, anchoCelda, altoCelda, mousePos,teclaMouse,array0Bombas,bombita,texto, fuente, color_texto
    x = int((mousePos[0]/ anchoCelda))
    y = int((mousePos[1] / altoCelda))
    if teclaMouse[0] and x >= 0 and x <= 7 and y >= 0 and y <= 7:
        if not campo[y][x].bomba:
            bombita = 0
            while bombita < 1:
                for i in range(3):
                   for X in range(3):
                        if((y - 1) + i) >= 0 and ((y - 1) + i) <= 7 and ((x - 1) + X) >= 0 and ((x - 1) + X) <= 7:
                            if not campo[(y - 1) + i][(x - 1) + X].bomba and campo[((y - 1) + i)][(x - 1) + X] not in array0Bombas:
                                array0Bombas.append(campo[((y - 1) + i)][(x - 1) + X])
                            elif campo[(y - 1) + i][(x - 1) + X].bomba:
                                bombita += 1
                for bomba0 in array0Bombas:
                    for i in range(3):
                        for X in range(3):
                            if((int(bomba0.y / altoCelda) - 1) + i) >= 0 and ((int(bomba0.y / altoCelda) - 1) + i) <= 7 and ((int(bomba0.x / altoCelda) - 1) + X) >= 0 and ((int(bomba0.x / altoCelda) - 1) + X) <= 7: 
                                if campo[((int(bomba0.y / altoCelda) - 1) + i)][((int(bomba0.x / altoCelda) - 1) + X)].bomba == False:
                                    campo[((int(bomba0.y / altoCelda) - 1) + i)][((int(bomba0.x / altoCelda) - 1) + X)].descubierto = True
                                    campo[((int(bomba0.y / altoCelda) - 1) + i)][((int(bomba0.x / altoCelda) - 1) + X)].imagen = pygame.transform.scale(pygame.image.load("imgBusca/3.png"),(anchoCelda,altoCelda))
                                else:
                                    bombita += 1
            
                
                            
    

def casillasAlaoBombas():
    for i in range(8):
        for x in range(8):
            print(campo[i][x].bombasAlrededor)
            if campo[i][x].bomba ==  False:
                for z in range(3):
                    for y in range(3):
                        if((i - 1)+z) >= 0 and ((i - 1) + z)  <= 7 and ((x - 1) + y) >= 0 and ((x - 1) + y) <= 7:
                            if campo[(i - 1) + z][(x - 1) + y].bomba == True:
                                campo[i][x].bombasAlrededor += 1






        

crearCampo()
crearBombas()
casillasAlaoBombas()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    casillaBomba()
   
    #print(len(array0Bombas))
    pantalla.fill("white") 
    casillaSinBomba()
    for i in range(8):
        for x in range(8):
            campo[i][x].pintar()
            if campo[i][x].bombasAlrededor > 0 and campo[i][x].descubierto == True:
                pantalla.blit(fuente.render(str(campo[i][x].bombasAlrededor), True, color_texto),(x * 50 + 15, i * 50 + 15))
    pygame.display.flip()
    pygame.display.update()
pygame.quit()