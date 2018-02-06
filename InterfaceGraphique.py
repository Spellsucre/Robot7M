
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


#___________________________________GESTION DES CLICS (G & D)___________________________________

#fonction detection du clic gauche (ajout d'un obstacle de type cube)
def clicgauche(event):
    if a1.possede_sol():
        X = event.x
        Y = event.y
        c1 = Creation_Cube_xy(X, Y, a1)
        if a1.ajouter_cube(c1):
            dessiner_cube(c1, a1)
        else:
            print("Error : object 'Cube' outside arena ")
    else:
        print("Ajoutez un sol avant de poser des blocs !")


#fonction detection du clic droit (ajout d'un mur)
def clicdroit(event):
    if a1.possede_sol():
        X = event.x
        Y = event.y
        m1 = Creation_Mur_xy(X, Y, a1)
        if a1.ajouter_cube(m1):
            dessiner_mur(m1, a1)
        else:
            print("Error : object 'Mur' outside arena ")
    else:
        print("Ajoutez un sol avant de poser des blocs !")


#___________________________________AJOUT D'UN SOL VIA LE BOUTON___________________________________

def ajout_sol():
    if not a1.possede_sol():
        s1 = Creation_Sol(a1)
        if a1.ajouter_cube(s1):
            dessiner_sol(s1)
    else:
        print("Il y a déjà un sol !")


#___________________________________FENETRE PRINCIPALE___________________________________

fenetre = Tk()
fenetre.title("_______Robot 2i013_______")
fenetre.resizable(width=True, height=False)
#affichage d'un texte dans la fenetre principale
label = Label(fenetre, text = "Clic gauche ~> ajout d'un cube\nClic droit  ~> ajout d'un mur").pack()


#___________________________________FRAME & CANEVAS___________________________________

#creation frame1 -> conteneur
frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
frame1.pack(side=TOP, padx=5, pady=5)
#label_frame1
Label(frame1, text="Carré gris = Arene 500 x 500px").pack()

#creation d'un canvas (toile ou tableau) dans la fenetre
canvas1 = Canvas(frame1, width=a1.lx, height=a1.ly)
canvas1.bind('<Button-1>', clicgauche)
canvas1.bind('<Button-3>', clicdroit)
canvas1.pack()

#___________________________________NETTOYAGE DU CANEVAS___________________________________

def effacer():
    """efface tout le canvas"""
    canvas1.delete(ALL)
    while len(a1.liste_cube) > 0:
        a1.liste_cube.pop(-1)


def effacerdernier():
    """ Efface le dernier objet"""
    for i in range(2):
        if len(canvas1.find_all()) >= 1:
            item = canvas1.find_all()[-1]
            canvas1.delete(item)
    if len(a1.liste_cube) > 0:
        a1.liste_cube.pop(-1)


#___________________________________GENERATION ALEATOIRE DE BLOC___________________________________

def pose_bloc_alea():
    if a1.possede_sol():
        aleatoire = random.randint(0,1)
        if aleatoire == 1:
            #print("JE SUIS DANS CUBE")
            c2 = Creation_Cube(a1)
            if a1.ajouter_cube(c2):
                dessiner_cube(c2, a1)
            else:
                print("Error : object outside arena ")
        else:
            #print("JE SUIS DANS MUR")
            m2 = Creation_Mur(a1)
            if a1.ajouter_cube(m2):
                dessiner_mur(m2, a1)
            else:
                print("Error : object outside arena")
    else:
        print("Ajoutez un sol avant de poser des blocs !")


#___________________________________LES BOUTONS___________________________________


#       WIP     ~>      FCT BROKEN      :)
#creation d'un bouton d'affichage des objets
#bouton0 = Button(fenetre, text= "Ajout aleatoire de blocs", command=pose_bloc_alea).pack(side=LEFT)

#creation d'un bouton de fermeture de la fenetre
bouton1 = Button(fenetre, text= "Quitter", command=fenetre.destroy).pack(side=RIGHT)

#creation d'un bouton de nettoyage du canvas
bouton2 = Button(fenetre, text= "Effacer tout", command=effacer).pack(side=LEFT)

#creation d'un bouton qui efface le dernier ajouté au canvas
bouton3 = Button(fenetre, text= "Effacer Dernier objet", command=effacerdernier).pack(side=LEFT)

#creation d'un bouton qui ajoute un sol à l'arene
bouton4 = Button(fenetre, text= "Nouveau Sol", command=ajout_sol).pack(side=LEFT)

#creation d'un bouton qui affiche l'état de l'arene
bouton5 = Button(fenetre, text= "Etat Arene", command=a1.afficher).pack(side=RIGHT)


#___________________________________FONCTIONS DRAW___________________________________

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
    canvas1.create_text(s1.x + s1.larg / 2, s1.y + s1.long / 2, text="Sol", fill="grey", activefill="Black")


#___________________________________MAINLOOP___________________________________

fenetre.mainloop()
