from fltk import *
from menu import *


class Jeton:
    """
    Class qui permet de representer de representer les jetons
    Elle prend comme arguments :

    joueur : str(une couleur)
    var : la varable du plateau
    pos : le dictionnaire des positions du plateau
    esp : espacement entre deux position digonales (uniquement pour var = 12 ou 3)
    """

    def __init__(self,joueur,var,pos,esp):
        """
        self.id est un nombre qui identifie l'objet pour fltk

        self.tout_les_jetons est une liste de tuples de toute les positions
        ainsi que les identifiant des jetons du joueur
        ex : [(150,150,1),(150,320,2),(380,420,5)]

        self.moulin est une liste de liste
        Chaque liste contient 3 tuples de coordonne forment un moulin
        """
        self.joueur = joueur
        self.tout_les_jetons = []
        self.id = 0
        self.moulin = []
        self.var = var
        self.pos = pos
        self.esp = esp


    def jeton(self,x,y):
        """
        Dessine un cercle de coordonee x,y
        Ajoute ces coordonee à la liste self.tout_les_jetons
        """
        cercle(x,y,30,couleur ='white',epaisseur=2,remplissage=self.joueur,tag = self.joueur + str(self.id))
        self.tout_les_jetons.append((x,y,self.id))
        self.id += 1


    def aligner(self,x,y): 
        """
        Chaque liste correspond a un axe possible sur le plateau 
        pour construire un moulin

        La fonction parcours la liste self.tout_les_jetons
        si une valeur de la liste est sur le meme axe que les argument x,y
        elle est ajoute a sa liste correspondante

        les listes avec mid servent a ce que il n'y ai pas un moulin
        si le jetons est sur un des axe du milieu
        En effet dans la variant 9 par exemple, 2 moulins peuvent etre
        effectue sur la ligne centrale
        Pour eviter cela on partage le plateau en 4 avec les deux moitie sur x
        et deux moitie sur y
        On verifie alors avec quel moite du plateau le jeton fait un moulin

        diago est utilisé pour la variant de 12 et 3 jetons
        esp est utilisé pour claculer une position diagonale
        si un jeton du meme joueur se trouve en diagnoale la fonction cherche
        si il existe un autre jeton du meme joueur en poursuivant la diagonal
        d'une case


        Si la taille d'une liste est egale a 3, c'est a dire que 3 element 
        forment un moulin alors la fonction renvoie True  
        """
        nb_x = []
        nb_y = []
        mid_y_left = []
        mid_y_right = []
        mid_x_top = []
        mid_x_bottom = []
        diago_gauche = []
        diago_droite = []

        if self.var == 3 or self.var == 12:
 
            diago_droite.append((x,y))
            diago_gauche.append((x,y))

            for i in self.tout_les_jetons:
                
                if i[0] == x+self.esp and i[1] == y+self.esp:
                    diago_gauche.append(i[:-1])
                    
                    for id in range(self.var):
                        if (x+self.esp*2,y+self.esp*2,id) in self.tout_les_jetons :
                            diago_gauche.append((x+self.esp*2,y+self.esp*2))
                            

                if i[0] == x-self.esp and i[1] == y-self.esp:
                    diago_gauche.append(i[:-1])
                    
                    for id in range(self.var):
                        if (x-self.esp*2,y-self.esp*2,id) in self.tout_les_jetons :
                            diago_gauche.append((x-self.esp*2,y-self.esp*2))
                            
                
                if i[0] == x+self.esp and i[1] == y-self.esp:
                    diago_droite.append(i[:-1])
                    
                    for id in range(self.var):
                        if (x+self.esp*2,y-self.esp*2,id) in self.tout_les_jetons :
                            diago_droite.append((x+self.esp*2,y-self.esp*2))
                            

                if i[0] == x-self.esp and i[1] == y+self.esp:
                    diago_droite.append(i[:-1])
                    
                    for id in range(self.var):
                        if (x-self.esp*2,y+self.esp*2,id) in self.tout_les_jetons :
                            diago_droite.append((x-self.esp*2,y+self.esp*2))
                            
        if self.var != 3:      
            for i in self.tout_les_jetons:
                
                if i[0]==x and x!= mid:   
                    nb_x.append(i[:-1])

                if x==mid and y<mid:
                        if i[1] < mid and i[0]==mid:
                            mid_x_top.append(i[:-1])
                if x==mid and y>mid:           
                        if i[1] > mid and i[0]==mid:
                            mid_x_bottom.append(i[:-1])

                if i[1]==y and i[1]!=mid:
                    nb_y.append(i[:-1])

                if y==mid and x<mid:
                    if i[0] < mid and i[1]==mid:
                        mid_y_left.append(i[:-1])
                if y==mid and x>mid:  
                    if i[0] > mid and i[1]==mid:
                        mid_y_right.append(i[:-1])

        if self.var == 3: 
            for i in self.tout_les_jetons:
                if i[0]==x:   
                    nb_x.append(i[:-1])
                if i[1]==y:
                    nb_y.append(i[:-1])

        if len(nb_x) == 3:
            self.moulin.append(nb_x)
            self.show_moulin(nb_x)
            return True
        if  len(nb_y) == 3:
            self.moulin.append(nb_y)
            self.show_moulin(nb_y)
            return True
        if len(mid_x_top) == 3:
            self.moulin.append(mid_x_top)
            self.show_moulin(mid_x_top)
            return True
        if len(mid_x_bottom) == 3:
            self.moulin.append(mid_x_bottom)
            self.show_moulin(mid_x_bottom)
            return True
        if len(mid_y_left) == 3:
            self.moulin.append(mid_y_left)
            self.show_moulin(mid_y_left)
            return True
        if len(mid_y_right) == 3:
            self.moulin.append(mid_y_right)
            self.show_moulin(mid_y_right)
            return True
        if len(diago_droite) == 3:
            self.moulin.append(diago_droite)
            self.show_moulin(diago_droite)
            return True    
        if len(diago_gauche) == 3:
            self.moulin.append(diago_gauche)
            self.show_moulin(diago_gauche)
            return True


        return False
    

    def enlever (self,x,y,joueur):
        """
        Parcours la liste de tout les jetons
        et efface le jeton de la fentre
        le retire le la liste des jetons
        et met la position du jeton dans le dictionnaire pos a "None"
        """
        for i in range(self.var):
            if (x,y,i) in self.tout_les_jetons:
                efface(joueur + str(i))
                self.tout_les_jetons.remove((x,y,i))
                self.pos[(x,y)] = None


    def deplacer (self,x,y,pos_avant,joueur):
        """
        pos_avant est l'avant dernière position cliqué par le joueur,
        elle correspond au jeton a deplacer

        x,y sont la dernière position cliqué, elle correspond a la position 
        où le jeton va etre deplacé

        Si le jeton deplacé se trouvait dans un moulin 
        on supprime les cercle jaunes par des cercles blanc
        pour toute les valeurs du moulin

        Si le jeton appartenait a plusieurs moulin 
        on appelle la fonction show_moulin pour ne pas effacer 
        les jetons en commun du moulin
        """
        x_avant , y_avant = pos_avant
        
        for i in range(self.var):
            if (x_avant,y_avant,i) in self.tout_les_jetons:
                
                efface(self.joueur + str(i))
                cercle(x,y,30,couleur='white',epaisseur=2,remplissage=self.joueur,tag = self.joueur + str(i))
                self.tout_les_jetons.remove((x_avant,y_avant,i))
                self.tout_les_jetons.append((x,y,i))
                self.pos[(pos_avant)]=None
                self.pos[(x,y)]=joueur

                for moulin in self.moulin:
                    if (pos_avant) in moulin:
                        for jeton in moulin:
                            x,y = jeton
                            for i in range(self.var):
                                if (x,y,i) in self.tout_les_jetons:
                                    efface(self.joueur + str(i))
                                    cercle(x,y,30,couleur='white',epaisseur=2,remplissage=self.joueur,tag = self.joueur + str(i))
                        self.moulin.remove(moulin)
                        for moulin in self.moulin:
                            self.show_moulin(moulin) 
                return True 


    def show_moulin (self,ligne):
        """
        ligne est une liste de 3 tuples (x,y)
        elle correspond au jeton d'un moulin

        Pour chaque coordonne la fonction efface les cercles blanc
        et les remplace par des cercles jaunes pour montrer le moulin
        le tag du cercle reste le meme
        """
        for jeton in ligne:
            x,y = jeton
            for i in range(self.var):
                if (x,y,i) in self.tout_les_jetons:
                    efface(self.joueur + str(i))
                    cercle(x,y,30,couleur='yellow',epaisseur=2,remplissage=self.joueur,tag = self.joueur + str(i))