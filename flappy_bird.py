
import pygame
import random
# inizializzo Pygame
pygame.init()
# carico le immagini
sfondo = pygame.image.load(
    'C:/Users/axelc/Desktop/GiochiPython/immagini/sfondo.png')
uccello = pygame.image.load(
    'C:/Users/axelc/Desktop/GiochiPython/immagini/chiccox2.jpg')
base = pygame.image.load(
    'C:/Users/axelc/Desktop/GiochiPython/immagini/base.png')
gameover = pygame.image.load(
    'C:/Users/axelc/Desktop/GiochiPython/immagini/gameover.png')
tubo_giu = pygame.image.load(
    'C:/Users/axelc/Desktop/GiochiPython/immagini/bottle.png')
tubo_su = pygame.transform.flip(tubo_giu, False, True)

# aggiungo la finestra di gioco

SCHERMO = pygame.display.set_mode((288, 512))
FPS = 50
VEL_AVANZ = 3 


class tubi_classe:
    def __init__(self):
        self.x = 300
        self.y = random.randint(-75+15, 150+30)

    def avanza_e_disegna(self):
        self.x -= VEL_AVANZ
        SCHERMO.blit(tubo_giu, (self.x, self.y+210))
        SCHERMO.blit(tubo_su, (self.x, self.y-210))

    def collissione(self, uccello, uccellox, uccelloy):
        tolleranza = 10
        uccello_lato_dx = uccellox+uccello.get_width() - tolleranza
        uccello_lato_sx = uccellox+tolleranza
        tubi_lato_dx = self.x+tubo_giu.get_width()
        tubi_lato_sx= self.x
        uccello_lato_su=uccelloy+tolleranza
        uccello_lato_giu=uccelloy+uccello.get_height()-tolleranza
        tubi_lato_su=self.y+110
        tubi_lato_giu=self.y+210
        
        if uccello_lato_dx> tubi_lato_sx and uccello_lato_sx<tubi_lato_dx :
            if uccello_lato_su<tubi_lato_su or uccello_lato_giu > tubi_lato_giu :
                hai_perso()


def disegna_oggetti():
    SCHERMO.blit(sfondo, (0, 0))
    for t in tubi:
        t.avanza_e_disegna()

    SCHERMO.blit(uccello, (uccellox, uccelloy))
    SCHERMO.blit(base, (basex, 400))


def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)


def inizializza():
    global uccellox, uccelloy, uccello_vely
    global basex
    global tubi
    uccellox, uccelloy = 60, 150
    uccello_vely = 0
    basex = 0
    tubi = []
    tubi.append(tubi_classe())


def hai_perso():
    SCHERMO.blit(gameover, (50, 180))
    aggiorna()
    ricominciamo = False
    while not ricominciamo:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                inizializza()
                ricominciamo = True
            if event.type == pygame.QUIT:
                pygame.quit()


inizializza()

while True:
    # avanzamento della base
    if basex < -45: basex = 0
    basex -= VEL_AVANZ

    # GRAVITA
    uccello_vely += 1
    uccelloy += uccello_vely
    # COMANDI
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN) and event.key == pygame.K_UP:
            uccello_vely = -10
        if event.type == pygame.QUIT:
            pygame.quit()
    #gestione tubi
    if tubi[-1].x<60: tubi.append(tubi_classe())
    for t in tubi:
        t.collissione(uccello,uccellox,uccelloy)
    #colisone con la base
    if (uccelloy > 380):
        hai_perso()
    # AGGIORNAMENTO SCHERMO
    disegna_oggetti()
    aggiorna()
