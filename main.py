"""
Programme du tron
Besnard, Mathéo, 1G8
"""
import pygame
from random import *

#constantes de la fenÃªtre d'affichage
LARGEUR=512       #hauteur de la fenÃªtre
HAUTEUR=512      #largeur de la fenÃªtre
ROUGE=(255,0,0)     # dÃ©finition de 4 couleurs
VERT=(0,255,0)
BLEU=(0,0,255)
JAUNE=(255,255,0)

#Utilisation de la bibliothÃ¨que pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Tron")             #titre de la fenÃªtre
font = pygame.font.Font('freesansbold.ttf', 20)     #choix de la police de caractÃ¨res
frequence = pygame.time.Clock()                     #mode animation dans pygame


p1motoX=LARGEUR//2
p1motoY=HAUTEUR//2
p1direction = 'haut'


p2motoX=LARGEUR//2
p2motoY=HAUTEUR//2
p2direction = 'bas'


tempsPartie=0

p1point=0
p2point=0

round=0

def dessineDecor():
    """
    dessine un decor
    """
    pygame.draw.rect(fenetre, ROUGE, [1, 1, LARGEUR-1, HAUTEUR-70],1)

    nbCircle = randint(5,15)
    for a in range(nbCircle):
        pygame.draw.circle(fenetre, ROUGE, (randint(0,230),randint(0,400)), randint(10,35))
        pygame.draw.circle(fenetre, ROUGE, (randint(270, 512), randint(0, 400)), randint(10, 35))
    nbRect = randint(5,15)
    for b in range(nbRect):
        pygame.draw.rect(fenetre, BLEU, [randint(0,230), randint(0,230), randint(10,50), randint(10,50)],0)
        pygame.draw.rect(fenetre, BLEU, [randint(270, 350), randint(270, 350), randint(10, 50), randint(10, 50)], 0)

def afficheTexte(x,y,txt):
    """
    affiche un texte aux coordonnÃ©es x,y
    """
    texteAfficher = font.render(str(txt), True, JAUNE)
    fenetre.blit(texteAfficher,(x,y))


def p1collisionMur(p1x,p1y):
    """
    verifie si on touche un mur ou autre chose
    aucun obstacle correspond Ã  une couleur noire
    """
    global p2point, round
    p1color=fenetre.get_at((p1x, p1y))[:3]
    p1somme=p1color[0]+p1color[1]+p1color[2]
    if p1somme==0:
        p1collision=False
    else:
        p1collision=True
        p2point+=1

    return p1collision

def p2collisionMur(p2x,p2y):
    """
    verifie si on touche un mur ou autre chose
    aucun obstacle correspond Ã  une couleur noire
    """
    global p1point, round
    p2color=fenetre.get_at((p2x, p2y))[:3]
    p2somme=p2color[0]+p2color[1]+p2color[2]
    if p2somme==0:
        p2collision=False
    else:
        p2collision=True
        p1point+=1

    return p2collision


def deplacementmotop1():
    """
    deplace la moto si c'est possible
    """
    global p1motoX,p1motoY
    p1touche=False
    if p1direction=='haut':
        p1x=p1motoX
        p1y=p1motoY-1
        p1touche=p1collisionMur(p1x,p1y)
    elif p1direction=='bas':
        p1x=p1motoX     #a completer
        p1y=p1motoY+1
        p1touche = p1collisionMur(p1x, p1y)
    elif p1direction=='droite':
        p1x=p1motoX+1     #a completer
        p1y=p1motoY
        p1touche = p1collisionMur(p1x, p1y)
    elif p1direction=='gauche':
        p1x=p1motoX-1
        p1y=p1motoY
        p1touche=p1collisionMur(p1x,p1y)


    if p1touche==False:       #si pas d'obstacle alors on trace le point de la moto
        p1motoX=p1x
        p1motoY=p1y
    fenetre.set_at((p1x, p1y), VERT)
    return p1touche           #retourne la variable booleenne touche pour savoir si la partie est terminÃ©e

def deplacementmotop2():
    """
    deplace la moto si c'est possible
    """
    global p2motoX,p2motoY
    p2touche=False

    if p2direction=='haut':
        p2x=p2motoX
        p2y=p2motoY-1
        p2touche=p2collisionMur(p2x,p2y)
    elif p2direction=='bas':
        p2x=p2motoX     #a completer
        p2y=p2motoY+1
        p2touche = p2collisionMur(p2x, p2y)
    elif p2direction=='droite':
        p2x=p2motoX+1     #a completer
        p2y=p2motoY
        p2touche = p2collisionMur(p2x, p2y)
    elif p2direction=='gauche':
        p2x=p2motoX-1
        p2y=p2motoY
        p2touche=p2collisionMur(p2x,p2y)

    if p2touche==False:
        p2motoX=p2x
        p2motoY=p2y

    fenetre.set_at((p2x, p2y), JAUNE)
    return p2touche

loop=True
dessineDecor()
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenÃªtre (croix rouge)
        if event.type == pygame.KEYDOWN:  #une touche a Ã©tÃ© pressÃ©e...laquelle ?
            if event.key == pygame.K_ESCAPE:
                loop = False
            #fenetre.set_at((200, 200), color)

    keys = pygame.key.get_pressed()         #recupÃ©ration des touches appuyÃ©es en continu
    if keys[pygame.K_UP]:    #est-ce la touche UP
        p1direction = 'haut'
    elif keys[pygame.K_DOWN]:  #est-ce la touche DOWN
        p1direction = 'bas'
    elif keys[pygame.K_RIGHT]:  #est-ce la touche RIGHT
        p1direction = 'droite'
    elif keys[pygame.K_LEFT]:  #est-ce la touche LEFT
        p1direction = 'gauche'


    if keys[pygame.K_z]:    #est-ce la touche UP
        p2direction = 'haut'
    elif keys[pygame.K_s]:  #est-ce la touche DOWN
        p2direction = 'bas'
    elif keys[pygame.K_d]:  #est-ce la touche RIGHT
        p2direction = 'droite'
    elif keys[pygame.K_q]:  #est-ce la touche LEFT
        p2direction = 'gauche'


    #fenetre.fill((0,0,0))   #efface la fenÃªtre, non utilisÃ© ici

    if deplacementmotop1()==True:
        fenetre.fill((0, 0, 0))
        p1x = 0
        p1y = 0
        p2x = 0
        p2y = 0
        round+=1
        dessineDecor()
        print("Round :",round)
        #p1direction = 'haut'
        #p2direction = 'bas'
        if round==3:
            loop=False
            print("Fin de la partie !")

    if deplacementmotop2()==True:
        fenetre.fill((0, 0, 0))
        p1x = 0
        p1y = 0
        p2x = 0
        p2y = 0
        round+=1
        dessineDecor()
        print("Round :",round)
        #p1direction = 'haut'
        #p2direction = 'bas'
        if round==3:
            loop=False
            print("Fin de la partie !")

    frequence.tick(60)
    pygame.display.update() #mets Ã  jour la fenÃªtre graphique
    tempsPartie+=1
    afficheTexte(50,450,"Joueur 1 :")
    afficheTexte(90, 470,p1point)
    afficheTexte(350,450,"Joueur 2 :")
    afficheTexte(390, 470,p2point)

    pygame.display.flip()
pygame.quit()
print("Joueur 1 :",p1point)
print("Joueur 2 :",p2point)
print('Temps des trois rounds',tempsPartie)
if p1point > p2point:
    print("Le gagnant est donc le Joueur 1 avec : {}/3 manches gagnées".format(p1point))
else:
    print("Le gagnant est donc le Joueur 2 avec : {}/3 manches gagnées".format(p2point))