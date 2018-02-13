import pyglet
from pyglet.gl import *
from pyglet.window import key
WINDOW = 800
INCREMENT = 5


class Window(pyglet.window.Window):
    # Cube 3D start rotation
    xRotation = yRotation = 30

    def __init__(self, width, height, cube, x, y, t, title=''):
        super(Window, self).__init__(width, height, title)
        glClearColor(0, 0, 0, 1) # couleur de la fenetre
        self.t = t
        self.x = x
        self.y = y
        self.cube = cube 
        glEnable(GL_DEPTH_TEST)
        self.label = pyglet.text.Label('x : %d y : '%cube.xx, 
                          font_name='Times New Roman', 
                          font_size=20,
                          x=-200, y=200)
        
        
        

    def on_draw(self):
        # Clear the current GL Window
        self.clear()

        # Push Matrix onto stack
        glPushMatrix()

        glRotatef(self.xRotation, 1, 0, 0) # gere les rotations
        glRotatef(self.yRotation, 0, 1, 0)

        # Draw the six sides of the cube [f1, ...., f6]
        
        glBegin(GL_QUADS) # marque le debut de la construction


        #f1 violet
        glColor3f(0.9, 0.01, 1) 
        glVertex3f(self.t, -self.t, -self.t)#coin inferieur droit

        glColor3f(0.9, 0.01, 1) 
        glVertex3f(self.t, -self.t, self.t)#coin inferieur gauche

        glColor3f(0.9, 0.01, 1) 
        glVertex3f(self.t, self.t, self.t)# coin superieur gauche

        glColor3f(0.9, 0.01, 1) 
        glVertex3f(self.t, self.t, -self.t)# coin superieur droit

        #f2 orange
        glColor3f(1, 0.5, 0)
        glVertex3f(self.t, -self.t, -self.t)

        glColor3f(1, 0.5, 0)
        glVertex3f(-self.t, -self.t, -self.t)

        glColor3f(1, 0.5, 0)
        glVertex3f(-self.t, -self.t, self.t)

        glColor3f(1, 0.5, 0)
        glVertex3f(self.t, -self.t, self.t)

        #f3 jaune
        glColor3f(0.8, 0.7, 0)
        glVertex3f(-self.t, -self.t, -self.t)

        glColor3f(0.8, 0.7, 0)
        glVertex3f(-self.t, -self.t, self.t)

        glColor3f(0.8, 0.7, 0)
        glVertex3f(-self.t, self.t, self.t)

        glColor3f(0.8, 0.7, 0)
        glVertex3f(-self.t, self.t, -self.t)

        #f4 rouge
        glColor3f(1, 0, 0)
        glVertex3f(-self.t, self.t, self.t)

        glColor3f(1, 0, 0)
        glVertex3f(self.t, self.t, self.t)

        glColor3f(1, 0, 0)
        glVertex3f(self.t, self.t, -self.t)

        glColor3f(1, 0, 0)
        glVertex3f(-self.t, self.t, -self.t)


        #f5 vert
        glColor3f(0, 1, 0)
        glVertex3f(-self.t, -self.t, self.t)

        glColor3f(0, 1, 0)
        glVertex3f(-self.t, self.t, self.t)

        glColor3f(0, 1, 0)
        glVertex3f(self.t, self.t, self.t)

        glColor3f(0, 1, 0)
        glVertex3f(self.t, -self.t, self.t)


        #f6 bleu
        glColor3f(0, 0, 1)
        glVertex3f(-self.t, -self.t, -self.t)

        glColor3f(0, 0, 1)
        glVertex3f(-self.t, self.t, -self.t)

        glColor3f(0, 0, 1)
        glVertex3f(self.t, self.t, -self.t)

        glColor3f(0, 0, 1)
        glVertex3f(self.t, -self.t, -self.t)
        

        glEnd() # marque la fin de la construction
        a=5
        
        
        self.label.draw()

        # Pop Matrix off stack
        glPopMatrix()

    

    def on_resize(self, width, height):
        # set the Viewport
        glViewport(0, 0, width, height) # width gere "l'applatissement" horizontale du cube, height le vertical

        # using Projection mode
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        aspectRatio = width / height
        gluPerspective(35, aspectRatio, 1, 1000) #premier argument gere le rapprochement du cube de la camera

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(self.cube.xx, self.cube.yy, -800) # (x,y,z) x gere la position horizontale de la camera, y gere sa position verticale, et z gere le zoom
        # plus x augmente plus le cube monte et plus y monte plus le cube monte (0,0,-800)

    ## touche du clavier pour deplacer le cube ##

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.xRotation -= INCREMENT
        elif symbol == key.DOWN:
            self.xRotation += INCREMENT
        elif symbol == key.LEFT:
            self.yRotation -= INCREMENT
        elif symbol == key.RIGHT:
            self.yRotation += INCREMENT
        elif symbol == key.Q: # cube va vers la gauche
            self.clear()
            glTranslatef(-10, 0, 0)
            self.cube.xx = self.cube.xx -10
        elif symbol == key.D: # cube va vers la droite
            self.clear()
            glTranslatef(10, 0, 0)
            self.cube.xx = self.cube.xx +10
        elif symbol == key.Z: # cube va vers le haut
            self.clear()
            glTranslatef(0,10,0)
            self.cube.yy = self.cube.yy +10
        elif symbol == key.S: # cube va vers le bas
            self.clear()
            glTranslatef(0,-10,0)
            self.cube.yy = self.cube.yy -10
        elif symbol == key.P:
            self.clear()
            glTranslatef(0,0,10)
            self.cube.zz = self.cube.zz +10
        elif symbol == key.M:
            self.clear()
            glTranslatef(0,0,-10)
            self.cube.zz = self.cube.zz -10

class Cube3D():
    def __init__(self,xx,yy,zz,taille):
        self.xx = xx
        self.yy = yy
        self.zz = zz
        self.taille = taille

    def dessiner(self):
        w = Window(WINDOW, WINDOW, self, self.xx, self.yy,self.taille, 'CUBE')
        pyglet.app.run()
        

    def tmp():
         return Cube3D(0,0,1,70)
