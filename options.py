from fltk import *


def options(var,colJ1,colJ2,max):
    etage = 1 # 1: couleurs / 0: tour_maxi
    
    # Choix des couleurs
    joueur = '1'
    change_player = True # affichage des select_col une première fois
    change_clic = False
    change_etage = False
    select_colJ1 = 'white' # les deux couleurs sont donc inversées
    select_colJ2 = 'yellow'

    efface_tout()    
    # Interface
    image(0,0,'images/background.png',ancrage='nw')
    # Joueurs (flèches)
    polygone([(390,80),(415,60),(415,100)],remplissage='white',couleur='white')
    polygone([(650,80),(625,60),(625,100)],remplissage='white',couleur='white')
    texte(520,80,'Joueur '+joueur,couleur='white',ancrage='center',tag='joueur')
    # Couleurs
    texte(220,80,'Couleurs:',couleur='yellow',ancrage='center',tag='couleurs')
    # Choix tours max (flèches)
    polygone([(300,520),(325,500),(325,540)],remplissage='white',couleur='white')
    polygone([(500,520),(475,500),(475,540)],remplissage='white',couleur='white')
    texte(410,450,'Nombre de tours maximum:',ancrage='center',couleur='white',tag='etage')
    texte(400,520,str(max),ancrage='center',couleur='white',taille='40',tag='max')
    # Bouton valider
    image(400,680,'images/button_big.png',ancrage='center')
    texte(400,681,'Valider',police='impact',taille='30',couleur='white',ancrage='center')

    # Affichage des couleurs (listes en (y,x) car + simple pour la structuration)
    colors = [['black','red','purple','blue','green'],
        ['gray','orange','violet','cyan','yellowgreen']]
    for L in range(2):
        for C in range(5):
            cercle(200+100*C,170+75*L,20,remplissage=colors[L][C],epaisseur=0)

    # Coordonnées des couleurs
    for L in range(2):
        for C in range(5):
            colors[L][C] = [colors[L][C]]
            colors[L][C].append((170+75*L,200+100*C))

    # Tour maximum
    choix = [30,40,50,70,80,90,100,110,120,130,140,150,200,300,400,500,1000]
    move = choix.index(max) # Position dans choix de la variante
    

    while True:
        ev = donne_ev()
        tev = type_ev(ev)
        x = abscisse_souris()
        y = ordonnee_souris()

        ### EVENEMENTS
        # Flèche du haut et du bas
        if etage == 1 and tev == 'Touche' and touche(ev) == 'Down':
            etage -= 1
            change_etage = True
        elif etage == 0 and tev == 'Touche' and touche(ev) == 'Up':
            etage += 1
            change_etage = True

        # Flèche Gauche tours max
        if (etage == 0 and tev == 'Touche' and touche(ev) == 'Left')\
                or (tev == 'ClicGauche' and (300 <= x <= 325 and 500 <= y <= 540)):
            if move > 0:
                max = False
                move -= 1

        # Flèche Droite tour max
        if (etage == 0 and tev == 'Touche' and touche(ev) == 'Right')\
                or (tev == 'ClicGauche' and (475 <= x <= 500 and 500 <= y <= 540)):
            if move < len(choix)-1:
                max = False
                move += 1

        # Séléction du joueur
        if (tev == 'ClicGauche' and (390 <= x <= 415 or 625 <= x <= 650) and 60 <= y <= 100)\
                or (etage == 1 and tev == 'Touche' and (touche(ev) == 'Left' or touche(ev) == 'Right')):
            change_player = True
            if joueur == '1': joueur = '2'
            elif joueur == '2': joueur = '1'
            efface('joueur')
            texte(520,80,'Joueur '+joueur,couleur='white',ancrage='center',tag='joueur')

        # Couleurs
        if tev == 'ClicGauche':

            # Séléction de couleur
            for L in range(2):
                for C in range(5):
                    # Si le clic est sur une couleur qui n'appartient à personne
                    if -20 <= x-colors[L][C][1][1] <= 20 and -20 <= y-colors[L][C][1][0] <= 20\
                            and colors[L][C][0] != colJ1 and  colors[L][C][0] != colJ2:

                        if joueur == '1':
                            colJ1 = colors[L][C][0]
                            efface('select_colJ1')
                            cercle(200+100*C,170+75*L,20,select_colJ1,epaisseur=3,tag='select_colJ1')
                        elif joueur == '2':
                            colJ2 = colors[L][C][0]
                            efface('select_colJ2')
                            cercle(200+100*C,170+75*L,20,select_colJ2,epaisseur=3,tag='select_colJ2')

        # Bouton valider
        if (tev == 'Touche' and touche(ev) == 'Return')\
                or (tev == 'ClicGauche' and (290 <= x <= 510 and 640 <= y <= 720)):
            return var,colJ1,colJ2,max

        if tev == 'Quitte': # on sort de la boucle
            exit()


        ### AFFICHAGES
        # Affichage de la séléction de l'étage
        if change_etage:
            if etage == 1: cols_etage = ['yellow','white']
            elif etage == 0: cols_etage = ['white','yellow']

            efface('etage')
            texte(220,80,'Couleurs:',couleur=cols_etage[0],ancrage='center',tag='etage')
            texte(410,450,'Nombre de tours maximum:',couleur=cols_etage[1],ancrage='center',tag='etage')

        # Affichage des cercles des joueurs
        if change_player or change_clic:
            efface('select_colJ1')
            efface('select_colJ2')

            if change_player: # on inverse les couleurs de séléction
                stock_colJ1 = select_colJ1
                select_colJ1 = select_colJ2
                select_colJ2 = stock_colJ1

            for L in range(2):
                for C in range(5):
                    if colJ1 == colors[L][C][0]:
                        cercle(200+100*C,170+75*L,20,select_colJ1,epaisseur=3,tag='select_colJ1')
                    if colJ2 == colors[L][C][0]:
                        cercle(200+100*C,170+75*L,20,select_colJ2,epaisseur=3,tag='select_colJ2')
            change_player = change_clic = None

        # Tour maximum
        if not max:
            max = choix[move]
            efface('max')
            texte(400,520,max,ancrage='center',couleur='white',taille='40',tag='max')

        mise_a_jour()