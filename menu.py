from fltk import *
from options import *


def menu(var,colJ1,colJ2,max):

    choix = [3,5,6,7,9,10,12]
    move = choix.index(var) # Position dans choix de la variante

    efface_tout()
    # Interface
    image(0,0,'images/background.png',ancrage='nw',tag='bg')
    image(0,0,'images/logo.png',ancrage='nw',tag='menu')
    # Bouton options
    image(400,310,'images/button_small.png',ancrage='center',tag='menu')
    texte(400,310,'Options',police='impact',taille='25',ancrage='center',couleur='white',tag='menu')
    # Choix variante (flèches)
    polygone([(300,520),(325,500),(325,540)],remplissage='white',couleur='white',tag='menu')
    polygone([(500,520),(475,500),(475,540)],remplissage='white',couleur='white',tag='menu')
    texte(410,450,'Nombre de jetons:',ancrage='center',couleur='white',tag='menu')
    texte(400,520,str(var),ancrage='center',couleur='white',taille='40',tag='var')
    # Bouton jouer
    image(400,640,'images/button_big.png',ancrage='center',tag='menu')
    texte(400,641,'JOUER',police='impact',taille='40',ancrage='center',couleur='white',tag='menu')


    while True:
        ev = donne_ev()
        tev = type_ev(ev)
        x = abscisse_souris()
        y = ordonnee_souris()
        # Action dépendante du type d'événement reçu:

        # Flèche Gauche
        if (tev == 'Touche' and touche(ev) == 'Left')\
                or (tev == 'ClicGauche' and (300 <= x <= 325 and 500 <= y <= 540)):
            if move > 0:
                var = False
                move -= 1

        # Flèche Droite
        if (tev == 'Touche' and touche(ev) == 'Right')\
                or (tev == 'ClicGauche' and (475 <= x <= 500 and 500 <= y <= 540)):
            if move < 6:
                var = False
                move += 1
        
        # Bouton jouer
        if (tev == 'Touche' and touche(ev) == 'Return')\
                or (tev == 'ClicGauche' and (290 <= x <= 510 and 600 <= y <= 680)):
            efface('var')
            efface('menu')
            return var,None,colJ1,colJ2,max

        # Bouton options
        if (tev == 'Touche' and touche(ev) == 'Tab')\
                or (tev == 'ClicGauche' and (315 <= x <= 485 and 280 <= y <= 340)):
            var,colJ1,colJ2,max = options(var,colJ1,colJ2,max)
            return var,'options',colJ1,colJ2,max

        if tev == 'Quitte': # on sort de la boucle
            exit()

        
        if not var:
            var = choix[move]
            efface('var')
            texte(400,520,var,ancrage='center',couleur='white',taille='40',tag='var')

        mise_a_jour()


def plateau(var,x,y,xb,yb): # n est le nombre de carre
    r=10
    lst=[]

    if not var:
        return None
    elif var == 3:
        n = 1
        esp = (xb-x)/2
        ligne(x,y,xb,yb,epaisseur=2,couleur='white') # diagonale 1
        ligne(x,yb,xb,y,epaisseur=2,couleur='white') # diagonale 2
        ligne(x+(xb-x)/2,y,x+(xb-x)/2,yb,epaisseur=2,couleur='white') # ligne verticale
        ligne(x,y+(yb-y)/2,xb,y+(yb-y)/2,epaisseur=2,couleur='white') # ligne horizontale

    elif 5 <= var <= 7:
        n = 2
        esp = 130
        ligne(x+(xb-x)/2,y,x+(xb-x)/2,y+esp,epaisseur=2,couleur='white') # ligne verticale haute
        ligne(x+(xb-x)/2,yb,x+(xb-x)/2,yb-esp,epaisseur=2,couleur='white') # ligne verticale basse
        ligne(x,y+(yb-y)/2,x+esp,y+(yb-y)/2,epaisseur=2,couleur='white') # ligne horizontale gauche
        ligne(xb,y+(yb-y)/2,xb-esp,y+(yb-y)/2,epaisseur=2,couleur='white') # ligne horizontale droite

    elif 9 <= var <= 12:
        n = 3
        esp = 85
        ligne(x+(xb-x)/2,y,x+(xb-x)/2,y+esp*2,epaisseur=2,couleur='white') # ligne verticale haute
        ligne(x+(xb-x)/2,yb,x+(xb-x)/2,yb-esp*2,epaisseur=2,couleur='white') # ligne verticale basse
        ligne(x,y+(yb-y)/2,x+esp*2,y+(yb-y)/2,epaisseur=2,couleur='white') # ligne horizontale gauche
        ligne(xb,y+(yb-y)/2,xb-esp*2,y+(yb-y)/2,epaisseur=2,couleur='white') # ligne horizontale droite
        if var == 12:
            ligne(x,y,x+esp*2,y+esp*2,epaisseur=2,couleur='white') # diagonale haute gauche
            ligne(xb,y,xb-esp*2,y+esp*2,epaisseur=2,couleur='white') # diagonale haute droite
            ligne(x,yb,x+esp*2,yb-esp*2,epaisseur=2,couleur='white') # diagonale basse gauche
            ligne(xb,yb,xb-esp*2,yb-esp*2,epaisseur=2,couleur='white') # diagonale basse gauche


    for i in range (n):
        rectangle(x,y,xb,yb,couleur='white',epaisseur=2)

        cercle(x,y,r,couleur='white',remplissage='white',epaisseur=2) # haut droite
        lst.append((x,y))
        cercle(xb,y,r,couleur='white',remplissage='white',epaisseur=2) # haut gauche
        lst.append((xb,y))
        cercle(xb,yb,r,couleur='white',remplissage='white',epaisseur=2) # bas gauche
        lst.append((xb,yb))
        cercle(x,yb,r,couleur='white',remplissage='white',epaisseur=2) # bas droite
        lst.append((x,yb))
        cercle(x,y+(yb-y)/2,r,couleur='white',remplissage='white',epaisseur=2)# droite milieu
        lst.append((x,y+(yb-y)/2))
        cercle(x+(xb-x)/2,y,r,couleur='white',remplissage='white',epaisseur=2) # haut milieu
        lst.append((x+(xb-x)/2,y))
        cercle((x+(xb-x)/2),yb,r,couleur='white',remplissage='white',epaisseur=2) # bas mileu
        lst.append((x+(xb-x)/2,yb))
        cercle(xb,y-((y-yb)/2),r,couleur='white',remplissage='white',epaisseur=2) # gauche milieu
        lst.append((xb,y-(y-yb)/2))

        if var == 3:
            cercle(x+(xb-x)/2,y+(yb-y)/2,r,couleur='white',remplissage='white',epaisseur=2)
            lst.append((x+(xb-x)/2,y+(yb-y)/2))
            break

        x += esp
        y += esp
        xb -= esp
        yb -= esp
    
    # Bouton de retour au menu
    image(110,50,'images/button_small.png',ancrage='center')
    texte(50,28,'Retour',police='impact',taille='30',couleur='white')

    #liste des coordonnees des points triées de en haut à gauche à en bas à droite (sert à rien mais + simple pour debug)
    lst.sort(key = lambda x: (x[1], x[0]))

    d={}
    for i in lst:
        d[i] = None
        
    return (d,esp) # dictionnaire de forme  --> (tuple de coordonées) : None ou "j1" ou "j2"


def info(action,J,colJ1,colJ2):
    efface('info')

    # création des variables de Joueur et Adversaire
    if J == 1:
        colJ = colJ1
        colAdv = colJ2
        adv = '2'
    elif J == 2:
        colJ = colJ2
        colAdv = colJ1
        adv = '1'

    if action != "egalite" and action != False: # la partie n'est pas terminée, c'est au tour de "J"
        
        if action == 'enlever': # le joueur J peut enlever un pion de l'adversaire
            texte(495,50,'Le Joueur '+str(J)+' '*10+'enlève un pion du Joueur '+str(adv),
                couleur='white',police='impact',taille='20',ancrage='center',tag='info')
            cercle(407,50,12,couleur='white',remplissage=colJ,tag='info')
            cercle(750,50,12,couleur='white',remplissage=colAdv,tag='info')

        else: # le joueur J peut soit placer ou déplacer
            texte(495,50,'Le Joueur '+str(J)+' '*10+'peut '+action+' un pion',couleur='white',
                police='impact',taille='20',ancrage='center',tag='info')
            if action == 'placer': cercle(448,50,12,couleur='white',remplissage=colJ,tag='info')
            elif action == 'déplacer': cercle(436,50,12,couleur='white',remplissage=colJ,tag='info')

    elif action == "egalite":
        texte(495,50,'Egalité ! Vous avez atteint le nombre de tours maximum',couleur='white',police='impact',
            taille='18',ancrage='center',tag='info')

    else: # la partie est terminée, "J" est le gagnant
        texte(495,50,'Le Joueur '+str(J)+' '*10+' a gagné!',couleur='white',police='impact',
            taille='20',ancrage='center',tag='info')
        cercle(505,50,12,couleur='white',remplissage=colJ,tag='info')


def retour(colJ1,colJ2,max):

    var,opt,colJ1,colJ2,max = menu(9,colJ1,colJ2,100) # 9 = variante par défaut
    while opt: # si options ouvertes, on relance le menu et la variante choisie est gardée
        var,opt,colJ1,colJ2,max = menu(var,colJ1,colJ2,max)

    pos,esp = plateau(var,150,150,larg-150,haut-150)

    return (pos,var,esp,colJ1,colJ2,max)
    


larg = 800
haut = 800
mid = larg/2
cree_fenetre(larg,haut)

back = True # Bouton de retour au menu
init = False # Pour vérifier le 1er lancement du menu
pos,var,esp,colJ1,colJ2,tour_maxi = retour('black','red',100)