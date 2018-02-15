from pynput import keyboard
from Structures.Arene import *
from Structures.Robot import *

arene = Creation_Arene()
robot = Creation_Robot(arene)

def on_press(key):
	try:
		print('{0} released'.format(key))
		if(key == keyboard.Key.esc):
			return False
		elif (key.char == "a"):
			print("1")
		else:
			print("0")
	except AttributeError:
		print('special key {0} pressed'.format(key))

def on_release(key):
	try:
		print('{0} released'.format(key))
		if(key == "a"):
			print("true")
		else:
			print("false")
	except AttributeError:
		print('special key {0} pressed'.format(key))

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
	try:
		listener.join()
	except MyException as e:
		print('{0} was pressed'.format(e.args[0]))
			