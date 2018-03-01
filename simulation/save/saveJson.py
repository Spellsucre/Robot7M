import json
from structures.arene import Arene
from structures.robot import Robot
from structures.teteRobot import TeteRobot
from basiques.cube import Cube
from basiques.sol import Sol
from basiques.mur import Mur


def saveFic(obj, nomfichier="defaultsave.txt"):
    with open("save/"+nomfichier,'w') as f:
        f.write(serialiser(obj))
        
def loadFic(nomfichier="defaultsave.txt"):
    with open("save/"+nomfichier,'r') as f:
        content=f.read()
    return deserialiser(content)
        
def serialiser(obj):
    return json.dumps(obj, default=serialiser_aux)

def serialiser_aux(obj):
    dic = obj.__dict__
    dic.update({"__class":obj.__class__.__name__})
    return dic
    
def my_hook(dic):
    if "__class" in dic:
        cls = dic.pop("__class")
        return eval(cls)(**dic)
    return dic

def deserialiser(s):
     return json.loads(s,object_hook=my_hook)
     
