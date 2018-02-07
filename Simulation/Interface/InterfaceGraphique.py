
#import

from tkinter import *
from Arene import *
from Cube import *
from Mur import *
from Sol import *
import random

#code

#_________________________CREATION DU ARENE DE BASE ~> PAS TRES PROPRE__________________________

a1 = Creation_Arene()

def gen_aleatoire():
    
    #cube_horizontal = Cube(X,Y,0,longueur,largeur,30)
    #cube_vertical = Cube(X,Y,0,largeur,longueur,30)
    
    ###   Initialise le contour de l'arene avec des murs ###
    
    taille = 500 # taille de l'arene
    larg_mur = 30 # largeur des murs de contour
    
    dessiner_mur(Mur(0,0,0,taille-1,larg_mur,larg_mur),a1) #mur du haut
    dessiner_mur(Mur(0,0,0,larg_mur,taille-1,30),a1) #mur gauche
    dessiner_mur(Mur(0,taille-larg_mur-1,0,taille-1,larg_mur,larg_mur),a1) #mur du bas
    dessiner_mur(Mur(taille-larg_mur-1,0,0,larg_mur,taille-1,larg_mur),a1) #mur droit

    ###   Création d'une liste d'obstacles (murs) que l'on va tirer aléatoirement   ###

    # les coordonnées x et y doivent être comprises entre larg_mur et taille-larg_mur-1 soit ici entre 30 et 469

    nb_obstacles = 5
    i = 0
    long_max = 90
    larg_max = 90
    while i<nb_obstacles:
        x = random.randint(larg_mur,taille-larg_mur-1)
        y = random.randint(larg_mur,taille-larg_mur-1)
        long = random.randint(0,long_max)
        larg = random.randint(0,larg_max)
        
        if a1.isCube(x,y,0):
            print("ajout obstacle impossible : cube déja présent à cette position")

        else:
            dessiner_mur(Mur(x,y,0,long,larg,0),a1)
        i = i + 1

            

        
            
                  
            

#___________________________________GESTION DES CLICS (G & D)___________________________________

#fonction detection du clic gauche (ajout d'un obstacle de type cube)
def clicgauche(event):
    X = event.x
    Y = event.y
    c1 = Creation_Cube_xy(X, Y)
    if a1.ajouter_cube(c1):
        dessiner_cube(c1, a1)
    else:
        print("Error : object 'Cube' outside arena ")


#fonction detection du clic droit (ajout d'un mur)
def clicdroit(event):
    X = event.x
    Y = event.y
    m1 = Creation_Mur_xy(X, Y)
    if a1.ajouter_cube(m1):
        dessiner_mur(m1, a1)
    else:
        print("Error : object 'Mur' outside arena ")

#___________________________________AJOUT D'UN SOL VIA LE BOUTON___________________________________
        
def ajout_sol():
    s1 = Creation_Sol(a1)
    #if a1.ajouter_cube(s1):
    dessiner_sol(s1)

#___________________________________AJOUT D'UN ROBOT VIA LE BOUTON___________________________________

def ajout_robot():
    robot=Creation_Robot(a1)
    if a1.ajouter_robot(robot): #il faudra modifier la methode ajouter_robot pour qu'on ne puisse ajouter qu'un seul robot
        dessiner_robot(robot)
    else:
        if not a1.possede_sol:
            print("Ajouter un sol avant de placer un robot !")

        else:
            print("Impossible d'ajouter un robot, il en existe déjà un")
            
fenetre = Tk()
fenetre.title("_______Robot 2i013_______")
fenetre.resizable(width=False, height=False)


#affichage d'un texte dans la fenetre principale
label = Label(fenetre, text = "Clic gauche ~> ajout d'un cube\nClic droit  ~> ajout d'un mur")
label.pack()

#creation frame1 -> conteneur
frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
frame1.pack(side=TOP, padx=5, pady=5)

#label_frame1
Label(frame1, text="Carré gris = Arene 500 x 500px").pack()

#creation d'un canvas (toile ou tableau) dans la fenetre
canvas1 = Canvas(frame1, width=a1.lx, height=a1.ly, background="lightgrey")
canvas1.bind('<Button-1>', clicgauche)
#canvas1.bind('<Button-2>', clicmolette)
canvas1.bind('<Button-3>', clicdroit)
canvas1.pack()


#Fonction pour effacer le canvas
def effacer():
    """efface tout le canvas"""
    canvas1.delete(ALL)

def effacerdernier():
    """ Efface le dernier objet"""
    for i in range(2):
        if len(canvas1.find_all()) >= 1:
            item = canvas1.find_all()[-1]
            # on efface le cercle
            canvas1.delete(item)

##  TEST DE CREATION PLUS AFFICHAGE DE L'ARENE ET DES BLOCS

def update_canvas():
    aleatoire = random.randint(0,1)
    if aleatoire == 1:
        print("JE SUIS DANS CUBE")
        c1 = Creation_Cube(a1)
        if a1.ajouter_cube(c1):
            dessiner_cube(c1, a1)
        else:
            print("Error : object outside arena ")
    else:
        print("JE SUIS DANS MUR")
        m1 = Creation_Mur(a1)
        if a1.ajouter_cube(m1):
            dessiner_mur(m1, a1)
        else:
            print("Error : object outside arena")

#___________________________________LES BOUTONS___________________________________

#creation d'un bouton d'affichage des objets
bouton = Button(fenetre, text= "Ajout aleatoire de blocs", command=update_canvas).pack(side=LEFT)

#creation d'un bouton de fermeture de la fenetre
bouton = Button(fenetre, text= "Quitter", command=fenetre.destroy).pack(side=RIGHT)

#creation d'un bouton de nettoyage du canvas
bouton = Button(fenetre, text= "Effacer tout", command=effacer).pack(side=LEFT)

#creation d'un bouton qui efface le dernier ajouté au canvas
bouton = Button(fenetre, text= "Effacer Dernier objet", command=effacerdernier).pack(side=LEFT)

#creation d'un bouton qui ajoute un sol à l'arene
bouton = Button(fenetre, text= "Nouveau Sol", command=ajout_sol).pack(side=LEFT)

#creation bouton qui genere des murs tout autour de l'arene ainsi que des obstacles
bouton = Button(fenetre, text= "Generation Aleatoire", command=gen_aleatoire).pack(side=LEFT)

#creation d'un bouton qui ajoute un robot à l'arene
bouton = Button(fenetre, text= "Ajout Robot", command=ajout_robot).pack(side=RIGHT)



def dessiner_cube(cube,arene):
    if isinstance(cube,Cube) and cube.x + cube.larg < arene.lx and cube.y + cube.long < arene.ly:
        canvas1.create_rectangle(cube.x, cube.y, cube.x + cube.larg, cube.y + cube.long, fill="darkgrey")
        canvas1.create_text(cube.x + cube.larg/2, cube.y + cube.long/2, text="Cube", fill="darkgrey", activefill="black")

def dessiner_mur(mur,arene):
    if isinstance(mur,Mur) and mur.x + mur.larg < arene.lx and mur.y + mur.long < arene.ly:
        canvas1.create_rectangle(mur.x, mur.y, mur.x + mur.larg, mur.y + mur.long, fill="yellow")
        canvas1.create_text(mur.x + mur.larg/2, mur.y + mur.long/2, text="Mur", fill="yellow", activefill="Black")
             
def dessiner_sol(s1):
    canvas1.create_rectangle(s1.x,s1.y, s1.x + s1.larg,s1.y + s1.long, fill="grey")

def dessiner_robot(robot):
    
    x, y, z= robot.position
    long, larg, haut= robot.dimension
    dirx, diry, dirz =robot.direction
    canvas1.create_rectangle(x, y, x+larg, y+long, fill="blue")
    canvas1.create_text(x + larg / 2, y+long / 2, text="Robot", fill="blue", activefill="black")
    canvas1.create_line(x + larg/2, y, x + dirx, y - diry , fill="black",arrow='last') # creation d'une fleche indiquant la direction du robot
    canvas1.create_oval(x+ 2*larg/3, y- long/4, x+ larg/3, y+ long/4, outline="black") # creation d'un cercle representant la tete du robot    
    



fenetre.mainloop()
