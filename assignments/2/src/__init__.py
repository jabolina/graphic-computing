import pywavefront
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pywavefront import visualization
import sys

from constants import position_look, position_rotate, position_translate, light_by_key

OBJ_PATH = './resources/camera.obj'
WINDOW_NAME = 'Very beautiful camera'
obj = []


def handle_key_press(key, _, __):
    redisplay = False

    if ord(key) in position_look.keys():
        glLoadIdentity()
        gluLookAt(*position_look[ord(key)])
        redisplay = True

    elif ord(key) in position_rotate.keys():
        glRotatef(*position_rotate[ord(key)])
        redisplay = True

    elif ord(key) in position_translate.keys():
        glTranslatef(*position_translate[ord(key)])
        redisplay = True

    elif ord(key) in light_by_key.keys():
        glLightfv(*light_by_key[ord(key)])
        redisplay = True

    if redisplay:
        glutPostRedisplay()


def main():
    global obj
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1024, 768)
    glutCreateWindow(WINDOW_NAME)

    glutDisplayFunc(display)
    glutKeyboardFunc(handle_key_press)
    glClearColor(0.3, 0.3, 0.3, 0)

    light = [0.2, 0.2, 0.2, 0.0]

    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, light)

    glutDisplayFunc(display)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(30., 1., 0.1, 80.)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(*position_look[49])

    obj = pywavefront.Wavefront(OBJ_PATH)

    glutMainLoop()
    return


def display():
    global obj

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    visualization.draw(obj)

    glutSwapBuffers()
    return


if __name__ == '__main__':
    main()
