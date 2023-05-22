from fltk import *
from menu import *
import math


def close_node(dico,coo):
    """
    Renvoie une liste de toutes les coordonées des points
    qui sont sur le meme x et y que la position donnée en argument
    et renvoie une liste vide si la position donnée en argument n'a pas de jeton dessus
    """
    possible = []
    if dico[coo] != None:
        for node in dico:
            x,y = node
            if x == coo[0]: possible.append(node)
            if y == coo[1]: possible.append(node)

    return possible # liste de toutes les positions sur le meme x et y que les coo du jeton


def point_proches(coo,pos,esp,var):
    """
    Utilise la fonction close_node pour avoir la liste  de toutes les position sur le meme x et y

    Calcule la distance minimal sur x et sur y en entre coo et les points de possible

    Regarde quelle points dans la liste possible sont a cette distance minimal
    Ajoute a lst toute les postions qui sont a la distance minimal sur x ou sur y

    Ajoute a new_lst les valeurs de lst qui n'ont pas deja de jeton dessus

    Renvoie une liste de positions jouable
    """
    possible =  close_node(pos,coo)
    min_x = 500
    min_y = 500
    lst = []

    for e in possible:
        if e != coo:
            x1,y1 = coo
            x2,y2 = e
            dist_x = math.sqrt((x2 - x1)**2)
            dist_y = math.sqrt((y2 - y1)**2)
            if x2 != x1:
                if dist_x<=min_x:
                    min_x=dist_x
            if y2 != y1:
                if dist_y<=min_y:
                    min_y=dist_y

    for e in possible:
        if e != coo:
            x1,y1 = coo
            x2,y2 = e
            dist_x = math.sqrt((x2 - x1)**2)
            dist_y = math.sqrt((y2 - y1)**2)
            if x2 != x1:
                if dist_x<=min_x:
                    lst.append(e)
            if y2 != y1:
                if dist_y<=min_y:
                    lst.append(e)

    if var == 12:

        lst.append((coo[0]+ esp,coo[1]+esp))
        lst.append((coo[0]-esp,coo[1]-esp))
        lst.append((coo[0]-esp,coo[1]+esp))
        lst.append((coo[0]+esp,coo[1]-esp))

    if var == 3:
        if coo != (mid,mid):
            lst.append((mid,mid))
        else :
            lst.append((coo[0]+esp,coo[1]+esp))
            lst.append((coo[0]-esp,coo[1]-esp))
            lst.append((coo[0]-esp,coo[1]+esp))
            lst.append((coo[0]+esp,coo[1]-esp))


    new_lst = []
    for p in lst:
        if p in pos:
            if pos[p] == None:
                new_lst.append(p)
    
    return new_lst # liste de toutes les positions où on peut deplacer le jeton


def pos_jouable(x_souris,y_souris,pos,esp,var):  
    """
    Utilise la fonction point_proches() pour avoir la liste des positions jouables
    Dessine un cercle vert sur le plateau pour chaque valeur de la liste
    """ 
    jouable = point_proches((x_souris,y_souris),pos,esp,var)    
    i = 0
    for e in jouable:
        cercle(e[0],e[1],10,couleur='white',remplissage='green',tag='id_vert'+str(i))
        i += 1


def efface_pos_jouable():
    """
    Efface les cercles verts si on clique ailleurs
    """
    for p in range(50): efface('id_vert'+str(p))


def end_game_pos_jouable(pos):
    """
    Affiche des cercles verts sur toutes les positions jouables
    """
    i = 0
    for e in pos:
        if pos[e] == None:
            cercle(e[0],e[1],10,couleur='white',remplissage='green',tag='id_vert'+str(i))
            i += 1


def fin_jeu(tour,j1,j2,pos,esp,var,colJ1,colJ2):
    """
    Verifie si il ne reste plus que 2 pions a un joueur
    Ou si il ne peut plus effectuer aucun deplacement
    """
    if len(j1) <= 2:
        info(False,2,colJ1,colJ2) # J2 a gagné
        return True
        
    if len(j2) <= 2:
        info(False,1,colJ1,colJ2) # J1 a gagné
        return True

    if tour % 2 == 0:
        joueur = j1
        win = 2
    else:
        joueur = j2
        win = 1

    tout = len(joueur)
    tt = 0

    for j in joueur:
        if point_proches(j[:-1],pos,esp,var) == []:
            tt += 1
        
    if tt == tout:
        info(False,win,colJ1,colJ2) # le joueur "win" a gagné
        return True