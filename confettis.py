from fltk import *
import random


def create_confetti(num_conf, nb):
    """
    Créée un confetti "nb" fois dont le tag fltk est "num_conf",
    à un endroit aléatoire dans la fenêtre
    """
    size = 3

    for i in range(nb):
        colors = ['white','red','indian red','orange','yellow','yellow green',
            'light green','green','light blue','blue','purple','violet','pink']
        col = colors[random.randint(0,len(colors)-1)]

        x = random.randint(0,800-size)
        y = random.randint(0,800-size)

        rectangle(x,y,x+size,y+size,couleur=col,remplissage=col,tag='conf'+str(num_conf))
        num_conf += 1
        
    return num_conf


def display_confettis(num_conf, density, speed):
    """
    Affichage des confettis (appel de la fonction dans le while principal de jeu_du_moulin)

    densitée + grande -> impression de vitesse + petite
    0 <= speed <= density
    """
    num_conf = create_confetti(num_conf, speed) # 10 confetti d'un coup

    if num_conf > density + speed:
        for i in range(speed):
            efface('conf'+str(num_conf - density - i))

    return num_conf