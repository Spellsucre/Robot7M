##TEST PYGLET ~> HS

import pyglet
from pyglet.gl import *
from pyglet.window import key
from OpenGL.GLUT import *

WINDOW = 800
INCREMENT = 5


class Window(pyglet.window.Window):
    # Cube 3D start rotation
    xRotation = yRotation = 30

    def __init__(self, width, height, title=''):
        super(Window, self).__init__(width, height, title)
        glClearColor(0, 0, 0, 1)
        glEnable(GL_DEPTH_TEST)


    def on_draw(self):
        # Clear the current GL Window
        self.clear()

        # Push Matrix onto stack
        glPushMatrix()

        glRotatef(self.xRotation, 1, 0, 0)
        glRotatef(self.yRotation, 0, 1, 0)

        # Draw the six sides of the cube [f1, ...., f6]
        glBegin(GL_QUADS)


        #f1 violet
        glColor3f(0.9, 0.01, 1)
        glVertex3f(50, -50, -50)

        glColor3f(0.9, 0.01, 1)
        glVertex3f(50, -50, 50)

        glColor3f(0.9, 0.01, 1)
        glVertex3f(50, 50, 50)

        glColor3f(0.9, 0.01, 1)
        glVertex3f(50, 50, -50)

        #f2 orange
        glColor3f(1, 0.5, 0)
        glVertex3f(50, -50, -50)

        glColor3f(1, 0.5, 0)
        glVertex3f(-50, -50, -50)

        glColor3f(1, 0.5, 0)
        glVertex3f(-50, -50, 50)

        glColor3f(1, 0.5, 0)
        glVertex3f(50, -50, 50)

        #f3 jaune
        glColor3f(0.8, 0.7, 0)
        glVertex3f(-50, -50, -50)

        glColor3f(0.8, 0.7, 0)
        glVertex3f(-50, -50, 50)

        glColor3f(0.8, 0.7, 0)
        glVertex3f(-50, 50, 50)

        glColor3f(0.8, 0.7, 0)
        glVertex3f(-50, 50, -50)

        #f4 rouge
        glColor3f(1, 0, 0)
        glVertex3f(-50, 50, 50)

        glColor3f(1, 0, 0)
        glVertex3f(50, 50, 50)

        glColor3f(1, 0, 0)
        glVertex3f(50, 50, -50)

        glColor3f(1, 0, 0)
        glVertex3f(-50, 50, -50)


        #f5 vert
        glColor3f(0, 1, 0)
        glVertex3f(-50, -50, 50)

        glColor3f(0, 1, 0)
        glVertex3f(-50, 50, 50)

        glColor3f(0, 1, 0)
        glVertex3f(50, 50, 50)

        glColor3f(0, 1, 0)
        glVertex3f(50, -50, 50)


        #f6 bleu
        glColor3f(0, 0, 1)
        glVertex3f(-50, -50, -50)

        glColor3f(0, 0, 1)
        glVertex3f(-50, 50, -50)

        glColor3f(0, 0, 1)
        glVertex3f(50, 50, -50)

        glColor3f(0, 0, 1)
        glVertex3f(50, -50, -50)
        

        glEnd()

        # Pop Matrix off stack
        glPopMatrix()


    def on_resize(self, width, height):
        # set the Viewport
        glViewport(0, 0, width, height)

        # using Projection mode
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        aspectRatio = width / height
        gluPerspective(35, aspectRatio, 1, 1000)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0, 0, -400)


    def on_text_motion(self, motion):
        if motion == key.UP:
            self.xRotation -= INCREMENT
        elif motion == key.DOWN:
            self.xRotation += INCREMENT
        elif motion == key.LEFT:
            self.yRotation -= INCREMENT
        elif motion == key.RIGHT:
            self.yRotation += INCREMENT

#def INIT():
Window(WINDOW, WINDOW, 'Pyglet Colored Cube')
pyglet.app.run()


"""
if __name__ == '__main__':
    Window(WINDOW, WINDOW, 'Pyglet Colored Cube')
    pyglet.app.run()
"""
