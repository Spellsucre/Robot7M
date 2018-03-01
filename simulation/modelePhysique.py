from pynput import keyboard
from structures.arene import *
from structures.robot import *

arene = Creation_Arene()
arene.ajouter_robot(Creation_Robot(arene))
arene.afficher()

def on_press(key):
	try:
		#print('{0} released'.format(key))
		if(key == keyboard.Key.esc):
			return False
		elif(key == keyboard.Key.left):
			#print(arene.liste_robot[0].toString())
			arene.liste_robot[0].rotation_tete(30)
			arene.liste_robot[0].move()
			print(arene.liste_robot[0].toString())
		elif(key == keyboard.Key.right):
			#print(arene.liste_robot[0]szszszdq.toString())
			arene.liste_robot[0].rotation_tete(-30)
			arene.liste_robot[0].move()
			print(arene.liste_robot[0].toString())
		elif(key.char == "z"):
			#print(arene.liste_robot[0].toString())
			arene.liste_robot[0].setVitesse(+3)
			arene.liste_robot[0].move()
			print(arene.liste_robot[0].toString())
			arene.liste_robot[0].setVitesse(0)
		elif(key.char == "s"):
			#print(arene.liste_robot[0].toString())
			arene.liste_robot[0].setVitesse(-3)
			arene.liste_robot[0].move()
			print(arene.liste_robot[0].toString())
			arene.liste_robot[0].setVitesse(0)
		elif(key.char == "q"):
			#print(arene.liste_robot[0].toString())
			arene.liste_robot[0].rotation(90)
			arene.liste_robot[0].move()
			print(arene.liste_robot[0].toString())
		elif(key.char == "d"):
			#print(arene.liste_robot[0].toString())
			arene.liste_robot[0].rotation(-90)
			arene.liste_robot[0].move()
			print(arene.liste_robot[0].toString())
		elif(key.char == "e"):
			arene.afficher()
		else:
			print("0")
	except AttributeError:
		print('special key {0} pressed'.format(key))

"""
def on_release(key):
	try:
		print('{0} released'.format(key))
		if(key == "a"):
			print("true")
		else:
			print("false")
	except AttributeError:
		print('special key {0} pressed'.format(key))
"""

with keyboard.Listener(on_press=on_press) as listener:
	try:
		listener.join()
	except MyException as e:
		print('{0} was pressed'.format(e.args[0]))
			
