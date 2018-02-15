from pynput import keyboard
from Structures.Arene import *
from Structures.Robot import *

arene = Creation_Arene()
robot = Creation_Robot(arene)

def on_press(key):
	try:
		#print('{0} released'.format(key))
		if(key == keyboard.Key.esc):
			return False
		elif(key == keyboard.Key.left):
			print(robot.toString())
			robot.rotation_tete(30)
			robot.move()
			print(robot.toString())
		elif(key == keyboard.Key.right):
			print(robot.toString())
			robot.rotation_tete(30)
			robot.move()
			print(robot.toString())
		elif(key.char == "z"):
			print(robot.toString())
			robot.setVitesse(robot.getVitesse()+3)
			robot.move()
			print(robot.toString())
		elif(key.char == "s"):
			print(robot.toString())
			robot.setVitesse(robot.getVitesse()-3)
			robot.move()
			print(robot.toString())
		elif(key.char == "q"):
			print(robot.toString())
			robot.setVitesse(0)
			robot.rotation(90)
			robot.move()
			print(robot.toString())
		elif(key.char == "d"):
			print(robot.toString())
			robot.setVitesse(0)
			robot.rotation(-90)
			robot.move()
			print(robot.toString())
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
			