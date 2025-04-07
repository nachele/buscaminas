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

class Casilla:
    def __init__(self,x,y,imagen):
        self.x =( x * anchoCelda)
        self.y = (y * altoCelda)
        self.bomba = False
        self.exploto = False
        self.imagen =pygame.transform.scale(pygame.image.load(imagen),(anchoCelda,altoCelda)) 
        
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
#array0Bombas = [[None for i in range(filas)] for x in range(columnas)]
def casillaSinBomba():
    global campo, anchoCelda, altoCelda, mousePos,teclaMouse,array0Bombas,bombita
    x = int((mousePos[0]/ anchoCelda))
    y = int((mousePos[1] / altoCelda))
    if teclaMouse[0] and x >= 0 and x <= 7 and y >= 0 and y <= 7:
        if not campo[y][x].bomba:
            for i in range(3):
                for X in range(3):
                    if not campo[(y - 1) + i][(x - 1) + X].bomba and campo[((y - 1) + i)][(x - 1) + X] not in array0Bombas:
                        array0Bombas.append(campo[((y - 1) + i)][(x - 1) + X])
                    elif campo[(y - 1) + i][(x - 1) + X].bomba:
                        bombita += 1
            for bomba0 in array0Bombas:
                for i in range(3):
                    for X in range(3):
                        if((int(bomba0.y / altoCelda) - 1) + i) >= 0 and ((int(bomba0.y / altoCelda) - 1) + i) <= 7 and ((int(bomba0.x / altoCelda) - 1) + i) >= 0 and ((int(bomba0.x / altoCelda) - 1) + i) <= 7: 
                           
                            array0Bombas.append(   bomba0[int(bomba0.y / altoCelda) + i][int(bomba0.x / altoCelda) + X]              )



                    


def imgBomba():
    global anchoCelda, altoCelda
    for y in range(8):
        for x in range(8):
            if campo[y][x].bomba == True:
                campo[y][x].imagen = pygame.transform.scale(pygame.image.load("imgBusca/1.png"),(anchoCelda,altoCelda))

            
    





        

crearCampo()
crearBombas()
#imgBomba()

for i in range (8):
    for x in range(8):
        
        print(str(campo[i][x].bomba) + " campo[" + str(i) + "]" + "[" + str(x) + "]")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    casillaBomba()
    casillaSinBomba()
    print(len(array0Bombas))
    pantalla.fill("white") 
    for i in range(8):
        for x in range(8):
            campo[i][x].pintar()

    pygame.display.flip()
    pygame.display.update()
pygame.quit()