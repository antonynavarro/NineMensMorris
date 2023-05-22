from fltk import *
from menu import *
from jeton import *
from game import *
from confettis import *
import math



while back:
    ev = donne_ev()
    tev = type_ev(ev)
    
    if init: # le menu a été lancé plus d'une fois
        pos,var,esp,colJ1,colJ2,tour_maxi = retour(colJ1,colJ2,tour_maxi)
    else: # le menu a été lancé une fois
        init = True

    ### Commencement de la partie
    j1 = Jeton(colJ1,var,pos,esp)
    j2 = Jeton(colJ2,var,pos,esp)

    tour_poser = 0
    peut_enlever = False
    moins_j1 = False
    moins_j2 = False

    #tour_maxi = 30
    pos_avant = (150,650) # a modifier ajouter une valeur speciale au dico 
    tour=0
    old_tour = 0
    num_conf = 1

    info('placer',1,colJ1,colJ2) # Au tour du joueur 1

    if tev == 'Quitte':  # on sort de la boucle
        back = False
        break



    while var: # Si la fenêtre est fermée au menu, on n'exécute pas
        ev = donne_ev()
        tev = type_ev(ev)
        x = abscisse_souris()
        y = ordonnee_souris()

        # Bouton retour
        if (tev == 'Touche' and touche(ev) == 'Escape')\
                or (tev == "ClicGauche" and 25 <= x <= 195 and 20 <= y <= 80):
            back = True
            break

        
        # Affichage des infos
        '''
        Si la partie n'est pas terminée (sinon affiché avec fin_jeu)
        et si les infos n'ont pas encore été affichées
        '''
        if tour != tour_maxi and tour != old_tour:
            old_tour = tour

            if peut_enlever:
                if moins_j2: info('enlever',1,colJ1,colJ2) # J1 enlève j2
                elif moins_j1: info('enlever',2,colJ1,colJ2) # J2 enlève J1
                old_tour -= 1 # affichage du prochain tour
            else:
                if tour<var*2: action = 'placer' # phase 1
                else: action = 'déplacer' # phase 2
                
                if tour%2 == 0: info(action,1,colJ1,colJ2) # au tour de J1
                else: info(action,2,colJ1,colJ2) # au tour de J2


        # Retire un jeton de l'adversaire
        if peut_enlever == True:
            if tev == "ClicGauche":
                for e in pos:
                    xx,yy = e
                    distance = math.sqrt((x - xx)**2 + (y - yy )**2) # distance entre souris et centre du cecle
                    if distance <= 30:
                        if pos[(xx,yy)] !=None:
                            if moins_j2 == True:
                                if pos[(xx,yy)] == 'j2':
                                    if (xx,yy) not in (item for sublist in j2.moulin for item in sublist)\
                                            or len(j2.moulin)*3 == len(j2.tout_les_jetons): 
                                        j2.enlever(xx,yy,colJ2)
                                        peut_enlever = moins_j2 = False # on passe au tour du joueur 2
                            elif moins_j1 == True:
                                if pos[(xx,yy)] == 'j1':
                                    if (xx,yy) not in (item for sublist in j1.moulin for item in sublist)\
                                            or len(j1.moulin)*3 == len(j1.tout_les_jetons):
                                        j1.enlever(xx,yy,colJ1)
                                        peut_enlever = moins_j1 = False # on passe au tour du joueur 1


        # Phase 1 du jeu, tout les joueurs posent leurs jetons
        elif tour<var*2:
            if tev == "ClicGauche":
                print(tour,tour_maxi)
                for e in pos:
                    xx,yy = e
                    distance = math.sqrt((x - xx)**2 + (y - yy )**2) 
                    if distance <= 30:
                        if (tour%2) == 0:
                            if pos[(xx,yy)] ==None:
                                j1.jeton(xx,yy)
                                pos[(xx,yy)]="j1"
                                tour+=1
                            if j1.aligner(xx,yy): peut_enlever = moins_j2 = True # j1 peut enlever j2

                        else:
                            if pos[(xx,yy)]==None:
                                j2.jeton(xx,yy)
                                pos[(xx,yy)]="j2"
                                tour+=1
                            if j2.aligner(xx,yy): peut_enlever = moins_j1 = True # j2 peut enlever j1


        # Phase 2 du jeu, les jours deplacent leurs jetons
        elif tour < tour_maxi and not fin_jeu(tour,j1.tout_les_jetons,j2.tout_les_jetons,pos,esp,var,colJ1,colJ2):

            if tev == "ClicGauche":
                efface_pos_jouable()
                print(tour,tour_maxi)
                for e in pos:
                    xx,yy = e
                    distance = math.sqrt((x - xx)**2 + (y - yy )**2)
                    if distance <= 30:

                        if (tour%2) == 0: # TOUR J1
                            for i in range (var):
                                if (xx,yy,i) in j1.tout_les_jetons:
                                    if len(j1.tout_les_jetons)>3 or var == 3: pos_jouable(xx,yy,pos,esp,var)
                                    elif len(j1.tout_les_jetons)<=3 and var!=3: end_game_pos_jouable(pos)

                            if (xx,yy) in point_proches(pos_avant,pos,esp,var):
                                if j1.deplacer(xx,yy,pos_avant,"j1"):
                                    if j1.aligner(xx,yy): peut_enlever = moins_j2 = True # j1 peut enlever j2
                                    tour+=1

                            elif (pos[(xx,yy)] == None and len(j1.tout_les_jetons) == 3) and var!= 3:
                                j1.deplacer(xx,yy,pos_avant,"j1")
                                if j1.aligner(xx,yy): peut_enlever = moins_j2 = True # j1 peut enlever j2
                                tour+=1

                        else: # TOUR J2
                            for i in range (var):
                                if (xx,yy,i) in j2.tout_les_jetons:
                                    if len(j2.tout_les_jetons)>3 or var == 3: pos_jouable(xx,yy,pos,esp,var)
                                    elif len(j2.tout_les_jetons)<=3 and var!=3: end_game_pos_jouable(pos)
                            
                            if (xx,yy) in point_proches(pos_avant,pos,esp,var):
                                if j2.deplacer(xx,yy,pos_avant,"j2"):
                                    if j2.aligner(xx,yy): peut_enlever = moins_j1 = True # j2 peut enlever j1
                                    tour+=1
                            
                            elif (pos[(xx,yy)] == None and len(j2.tout_les_jetons) == 3) and var!= 3:
                                j2.deplacer(xx,yy,pos_avant,"j2")
                                if j2.aligner(xx,yy): peut_enlever = moins_j1 = True # j2 peut enlever j1
                                tour+=1

                        pos_avant = (xx,yy)

        elif tour == tour_maxi:
            action = "egalite"
            info(action,2,colJ1,colJ2)
            
        else: # partie terminée -> arrêt de l'affichage des infos et affichage des confettis 
            #tour = tour_maxi
            num_conf = display_confettis(num_conf,100,10)


        if tev == 'Quitte': # on sort de la boucle
            back = False
            break

        mise_a_jour()

ferme_fenetre()