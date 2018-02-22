
###############################
#CECI EST LA DERNIERE VERSION #
###############################


# import

from tkinter import *
from Arene import *
from Cube import *
from Mur import *
from Sol import *
import random

# code


# _________________________CREATION DU ARENE DE BASE ~> PAS TRES PROPRE__________________________

a1 = Creation_Arene()


# ___________________________________GENERATEUR DE MUR___________________________________


"""
    MANQUE:
       OK - l'ajout des 4 murs de l'arene à la liste de cube de l'arene (pour dans le futur faire un move du robot detectant les obstacles)
        
       OK - l'ajout des blocs random à la liste de cube de l'arene 
        
        - soit separer la fonction en deux fonctions distinctes (ajouter un autre bouton),
          une pour la generation des murs de l'arene et une pour les blocs
          sinon à chaque clic de bouton les murs sont recréés ~> saturation  de la liste de cube
          
        - soit bloquer cette fonction existante (gen_aleatoire()) à une seule generation comme pour le sol
          car ~> plusieurs sols = impossible. 
    
    FMANSON 7/2/18 20:06
"""
def gen_aleatoire():
    # cube_horizontal = Cube(X,Y,0,longueur,largeur,30)
    # cube_vertical = Cube(X,Y,0,largeur,longueur,30)

    ###   Initialise le contour de l'arene avec des murs ###

    ajout_sol()

    taille = 500  # taille de l'arene
    larg_mur = 30  # largeur des murs de contour

    m1 = Mur(0, 0, 0, taille - 1, larg_mur, larg_mur)
    m2 = Mur(0, 0, 0, larg_mur, taille - 1, 30)
    m3 = Mur(0, taille - larg_mur - 1, 0, taille - 1, larg_mur, larg_mur)
    m4 = Mur(taille - larg_mur - 1, 0, 0, larg_mur, taille - 1, larg_mur)

    a1.ajouter_cube(m1)
    a1.ajouter_cube(m2)
    a1.ajouter_cube(m3)
    a1.ajouter_cube(m4)
    
    dessiner_mur(m1, a1)  # mur du haut
    dessiner_mur(m2, a1)  # mur gauche
    dessiner_mur(m3, a1)  # mur du bas
    dessiner_mur(m4, a1)  # mur droit

    ###   Création d'obstacles (murs) que l'on va tirer aléatoirement   ###

    # les coordonnées x et y doivent être comprises entre larg_mur et taille-larg_mur-1 soit ici entre 30 et 469

    nb_obstacles = 5
    i = 0
    long_max = 90
    larg_max = 90
    while i < nb_obstacles:
        x = random.randint(larg_mur, taille - larg_mur - 1)
        y = random.randint(larg_mur, taille - larg_mur - 1)
        long = random.randint(0, long_max)
        larg = random.randint(0, larg_max)

        if a1.isCube(x, y, 0):  #MARCHE PAS ~> doit tester tous le pxl presents dans les coords de l'objet ~> à mon avis c'est trop compliqué et sert pas à grand chose... FManson
            canvas_console.delete(ALL)
            canvas_console.create_text(250, 15, text="ajout impossible : cube présent à cette position", fill="black", width=500,justify='center')
            print("ajout obstacle impossible : cube déja présent à cette position")

        else:
            m = Mur(x, y, 0, long, larg, 0)
            a1.ajouter_cube(m)
            dessiner_mur(m, a1)
        i = i + 1

# ___________________________________GESTION DES CLICS (G & D)___________________________________

# fonction detection du clic gauche (ajout d'un obstacle de type cube)
def clicgauche(event):
    if a1.possede_sol():
        X = event.x
        Y = event.y
        c1 = Creation_Cube_xy(X, Y, a1)
        if a1.ajouter_cube(c1):
            dessiner_cube(c1, a1)
        else:
            canvas_console.delete(ALL)
            canvas_console.create_text(250, 15, text="Error : object 'Cube' outside arena ", fill="black", width=500,justify='center')
            print("Error : object 'Cube' outside arena ")
    else:
        canvas_console.delete(ALL)
        canvas_console.create_text(250, 15, text="Ajoutez un sol avant de poser des blocs !", fill="black", width=500,justify='center')
        print("Ajoutez un sol avant de poser des blocs !")


# fonction detection du clic droit (ajout d'un mur)
def clicdroit(event):
    if a1.possede_sol():
        X = event.x
        Y = event.y
        m1 = Creation_Mur_xy(X, Y, a1)
        if a1.ajouter_cube(m1):
            dessiner_mur(m1, a1)
        else:
            canvas_console.delete(ALL)
            canvas_console.create_text(250, 15, text="Error : object 'Mur' outside arena ", fill="black", width=500, justify='center')
            print("Error : object 'Mur' outside arena ")
    else:
        canvas_console.delete(ALL)
        canvas_console.create_text(250, 15, text="Ajoutez un sol avant de poser des blocs !", fill="black", width=500,justify='center')
        print("Ajoutez un sol avant de poser des blocs !")


# ___________________________________AJOUT D'UN SOL VIA LE BOUTON___________________________________

def ajout_sol():
    if not a1.possede_sol():
        s1 = Creation_Sol(a1)
        if a1.ajouter_cube(s1):
            dessiner_sol(s1)
    else:
        canvas_console.delete(ALL)
        canvas_console.create_text(250,15, text="Il y a déjà un sol !", fill="black", width=500, justify='center')
        print("Il y a déjà un sol !")


#___________________________________AJOUT D'UN ROBOT VIA LE BOUTON___________________________________

def ajout_robot():

    if len(a1.liste_robot) == 0 and a1.possede_sol():
        robot=Creation_Robot(a1)
        a1.ajouter_robot(robot)
        dessiner_robot(robot)

    else:
        canvas_console.delete(ALL)
        canvas_console.create_text(250, 15, text="Il y a déjà un robot OU pas de sol !", fill="black", width=500, justify='center')


# ___________________________________FENETRE PRINCIPALE___________________________________

fenetre = Tk()
fenetre.geometry("600x660")
fenetre.title("Robot 2i013 Alpha 3.1")
fenetre.resizable(width=False, height=False)
# affichage d'un texte dans la fenetre principale
label = Label(fenetre, text="Clic gauche ~> ajout d'un cube\nClic droit  ~> ajout d'un mur").pack()


# ___________________________________FRAME & CANEVAS___________________________________

# creation frame1 -> conteneur
frame1 = LabelFrame(fenetre, text="Carré gris = Arene 500 x 500px", borderwidth=2, relief=GROOVE)
frame1.pack(side=TOP, padx=5, pady=5)

#creation frame2 ~> conteneur message erreur
frame2 = LabelFrame(fenetre, text="Informations", borderwidth=2, relief=GROOVE)
frame2.pack(side=TOP, padx=5, pady=5)

# creation d'un canvas principal (toile ou tableau) dans la fenetre
canvas1 = Canvas(frame1, width=a1.lx, height=a1.ly)
canvas1.bind('<Button-1>', clicgauche)
canvas1.bind('<Button-3>', clicdroit)
canvas1.pack()

#creation canvas secondaire pour affichage messages erreur
canvas_console = Canvas(frame2, width=500, height=30)
canvas_console.pack()


# ___________________________________NETTOYAGE DU CANEVAS___________________________________

def effacer():
    """efface tout le canvas"""
    canvas1.delete(ALL)
    canvas_console.delete(ALL)
    while len(a1.liste_cube) > 0:
        a1.liste_cube.pop(-1)
    while len(a1.liste_robot) > 0:
        a1.liste_robot.pop(-1)

def effacerdernier():
    """ Efface le dernier objet"""
    for i in range(2):
        if len(canvas1.find_all()) >= 1:
            item = canvas1.find_all()[-1]
            canvas1.delete(item)
    if len(a1.liste_cube) > 0:
        a1.liste_cube.pop(-1)

    if len(a1.liste_cube) == 0:
        canvas_console.delete(ALL)


# ___________________________________LES BOUTONS___________________________________

# creation d'un bouton de fermeture de la fenetre
bouton1 = Button(fenetre, text="Quitter", command=fenetre.destroy).pack(side=RIGHT)

# creation d'un bouton de nettoyage du canvas
bouton2 = Button(fenetre, text="Effacer tout", command=effacer).pack(side=LEFT)

# creation d'un bouton qui efface le dernier ajouté au canvas
bouton3 = Button(fenetre, text="Effacer Dernier objet", command=effacerdernier).pack(side=LEFT)

# creation d'un bouton qui ajoute un sol à l'arene
bouton4 = Button(fenetre, text="Nouveau Sol", command=ajout_sol).pack(side=LEFT)

# creation d'un bouton qui affiche l'état de l'arene
bouton5 = Button(fenetre, text="Etat Arene", command=a1.afficher).pack(side=LEFT)

# creation bouton qui genere des murs tout autour de l'arene ainsi que des obstacles
bouton = Button(fenetre, text="Generation Salle(WIP)", command=gen_aleatoire).pack(side=LEFT)

#creation d'un bouton qui ajoute un robot à l'arene
bouton = Button(fenetre, text= "Ajout Robot", command=ajout_robot).pack(side=LEFT)


# ___________________________________FONCTIONS DRAW___________________________________

def dessiner_cube(cube, arene):
    if isinstance(cube, Cube) and cube.x + cube.larg < arene.lx and cube.y + cube.long < arene.ly:
        canvas1.create_rectangle(cube.x, cube.y, cube.x + cube.larg, cube.y + cube.long, fill="darkgrey")
        canvas1.create_text(cube.x + cube.larg / 2, cube.y + cube.long / 2, text="Cube", fill="darkgrey",
                            activefill="black")


def dessiner_mur(mur, arene):
    if isinstance(mur, Mur) and mur.x + mur.larg < arene.lx and mur.y + mur.long < arene.ly:
        canvas1.create_rectangle(mur.x, mur.y, mur.x + mur.larg, mur.y + mur.long, fill="yellow")
        canvas1.create_text(mur.x + mur.larg / 2, mur.y + mur.long / 2, text="Mur", fill="yellow", activefill="Black")


def dessiner_sol(s1):
    canvas1.create_rectangle(s1.x, s1.y, s1.x + s1.larg, s1.y + s1.long, fill="grey")
    canvas1.create_text(s1.x + s1.larg / 2, s1.y + s1.long / 2, text="Sol", fill="grey", activefill="Black")


def dessiner_robot(robot):
    x, y, z = robot.position
    long, larg, haut = robot.dimension
    dirx, diry, dirz = robot.direction
    
    canvas1.create_rectangle(x, y, x + larg, y + long, fill="blue")
    canvas1.create_text(x + larg / 2, y + long / 2, text="Robot", fill="blue", activefill="black")   
    canvas1.create_oval(x + 2 * larg / 3, y - long / 4, x + larg / 3, y + long / 4,
                        outline="black")  # creation d'un cercle representant la tete du robot
    
    vecdirec_x=(x+larg/2)-dirx
    vecdirec_y=(y-long / 4)-diry #calcul du vecteur direction
    canvas1.create_line(x + larg / 2, y - long / 4, vecdirec_x , vecdirec_y, fill="black",
                       arrow='last')  # creation d'une fleche indiquant la direction du robot 


# ___________________________________MAINLOOP___________________________________

fenetre.mainloop()
