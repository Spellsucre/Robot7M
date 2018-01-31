
#import

from tkinter import *
from Arene import *
from Cube import *
from Mur import *
import random

#code

fenetre = Tk()
fenetre.title("_______Robot 2i013_______")
fenetre.resizable(width=False, height=False)
a1 = Creation_Arene()

#affichage d'un texte dans la fenetre principale
label = Label(fenetre, text = "Premier Test affichage de l'arene + blocs", bg="lightgrey")
label.pack()

#creation frame1 -> conteneur
frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
frame1.pack(side=TOP, padx=5, pady=5)

#label_frame1
Label(frame1, text="Carré gris = Arene 500 x 500px").pack()

#creation d'un canvas (toile ou tableau) dans la fenetre
canvas1 = Canvas(frame1, width=a1.lx, height=a1.ly, background="grey")
canvas1.pack()



##  TEST DE CREATION PLUS AFFICHAGE DE L'ARENE ET DES BLOCS

def update_canvas():
    aleatoire = random.randint(0,1)
    if aleatoire == 1:
        print("JE SUIS DANS CUBE")
        c1 = Creation_Cube()
        if a1.ajouter_cube(c1):
            #a1.afficher()
            dessiner_bloc(c1, a1)
        else:
            print("Error : object outside arena ")
    else:
        print("JE SUIS DANS MUR")
        m1 = Creation_Mur()
        if a1.ajouter_cube(m1):
            #a1.afficher()
            dessiner_bloc(m1, a1)
        else:
            print("Error : object outside arena")


#creation d'un bouton d'affichage des objets
bouton = Button(fenetre, text= "UPDATE GRAPH", command=update_canvas).pack(side=LEFT)

#creation d'un bouton de nettoyage du canvas
bouton = Button(fenetre, text= "QUIT", command=fenetre.destroy).pack(side=RIGHT)


def dessiner_bloc(cube,arene):
    if isinstance(cube,Cube) and cube.x + cube.larg < arene.lx and cube.y + cube.long < arene.ly:
        canvas1.create_rectangle(cube.x, cube.y, cube.x + cube.larg, cube.y + cube.long, fill="darkgrey")
        canvas1.create_text(cube.x + cube.larg/2, cube.y + cube.long/2, text="C", activefill="red")

    if isinstance(cube,Mur) and cube.x + cube.larg < arene.lx and cube.y + cube.long < arene.ly:
        canvas1.create_rectangle(cube.x, cube.y, cube.x + cube.larg, cube.y + cube.long, fill="black")
        canvas1.create_text(cube.x + cube.larg/2, cube.y + cube.long/2, text="M", fill="white", activefill="yellow")
             
            
fenetre.mainloop()


##________________________________
##        RESTE A JETTER ?      ##
##________________________________




"""
def dessiner_blocs(self):
    for i in self.liste_cube:
        tpx, tpy, tpz, tplarg, tplong, tphaut = i.x, i.y, i.y, i.larg, i.long, i.haut
        
        if isinstance(i,Cube) and tpx+tplarg < self.lx and tpy+tplong < self.ly:
            canvas1.create_rectangle(tpx, tpy, tpx+tplarg, tpy+tplong, fill="darkgrey")
            canvas1.create_text(tpx+tplarg/2, tpy+tplong/2, text="C")
        if isinstance(i, Mur) and tpx+tplarg < self.lx and tpy+tplong < self.ly:
            canvas1.create_rectangle(tpx, tpy, tpx+tplarg, tpy+tplong, fill="black")
        else:
            print("Objet inconnu!")
"""  


"""
###########################INTERFACE#########################
fenetre_principale = Tk()
fenetre_principale.resizable(width=False, height=False)
canvas1 = Canvas(fenetre_principale, width=350, height=350, background="lightgrey").pack()

def affiche():
    print("C'est bon ça marche !")

def ajout_arene():
    liste_c1 = []
    
    arene1 = Arene(50,50,0,liste_c1)
    canvas1.create_rectangle(0, 0, arene1.lx, arene1.ly,)

cree une fenetre et l'initialise avec une frame, un titre et un menu deroulant

fenetre_principale.title("representation graphique de l'Arene")

#ajout d'un menu a la fenetre
menubar = Menu(fenetre_principale)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Ajouter Arene Custom", command=ajout_arene)
menu1.add_command(label="Ajouter Arene 500 x 500", command=ajout_arene)
menu1.add_command(label="Ajouter Arene 200 x 200", command=ajout_arene)
    
menu1.add_command(label="Ajouter Blocs", command=affiche)
menu1.add_separator()
menu1.add_command(label="Réinitialiser Interface", command=affiche)
menu1.add_command(label="Quitter", command=fenetre_principale.destroy)
menubar.add_cascade(label="Option", menu=menu1)

fenetre_principale.config(menu=menubar)

fenetre_principale.mainloop()
"""
