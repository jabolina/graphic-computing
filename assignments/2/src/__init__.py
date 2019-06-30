from math import sin, cos

import pywavefront
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pywavefront import visualization
import sys

from camera import CameraHelper
from constants import position_look, position_rotate, position_translate, light_by_key

OBJ_PATH = './resources/camera.obj'
WINDOW_NAME = 'Very beautiful camera'
obj = []
holder = CameraHelper()


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
        print(position_translate[ord(key)])

    elif ord(key) in light_by_key.keys():
        glLightfv(*light_by_key[ord(key)])
        redisplay = True

    if redisplay:
        glutPostRedisplay()


def rotate_y(context: CameraHelper):
    context.lx = sin(context.angle)
    context.lz = -cos(context.angle)

    glLoadIdentity()
    gluLookAt(*context.get_look_at())
    print(context.get_look_at())


def rotate_x(context: CameraHelper):
    context.ly = sin(context.angle)
    context.lz = -cos(context.angle)

    glLoadIdentity()
    gluLookAt(*context.get_look_at())


def mouse_movement(x, y):
    global holder
    holder.x = x
    holder.y = y

    if x >= (GLUT_WINDOW_WIDTH // 2):
        holder.angle = x / 10 * 0.5

    else:
        holder.angle = x / 10 * -0.5

    rotate_y(holder)

    if y >= (GLUT_WINDOW_HEIGHT // 2):
        holder.angle = y / 10 * 0.1
    else:
        holder.angle = y / 10 * -0.1

    rotate_x(holder)
    glutPostRedisplay()


def handle_scroll(button, _, __, ___):
    if button == 3:
        glTranslatef(*position_translate[113])

    if button == 4:
        glTranslatef(*position_translate[101])


def slide_on_mouse(x, y):
    global holder

    if holder.is_first:
        holder.is_first = False
        holder.x = x
        holder.y = y

    if holder.x - x > 0:
        glTranslatef(*position_translate[100])
    elif holder.x - x < 0:
        glTranslatef(*position_translate[97])

    if holder.y - y > 0:
        glTranslatef(*position_translate[119])
    elif holder.y - y < 0:
        glTranslatef(*position_translate[115])

    holder.x = x
    holder.y = y
    glutPostRedisplay()


def main():
    global obj
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1024, 768)
    glutCreateWindow(WINDOW_NAME)

    glutDisplayFunc(display)
    glutKeyboardFunc(handle_key_press)
    glutMouseFunc(handle_scroll)
    glutPassiveMotionFunc(slide_on_mouse)
    glClearColor(0.3, 0.3, 0.3, 0)

    light = [0.2, 0.2, 0.2, 0.0]

    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, light)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(30., 1., 0.1, 80.)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(*position_look[49])

    obj = pywavefront.Wavefront(OBJ_PATH)

    glutMainLoop()
    return


def display():
    global obj, holder

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    visualization.draw(obj)

    glutSwapBuffers()
    return


if __name__ == '__main__':
    main()
