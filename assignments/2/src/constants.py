from OpenGL.raw.GL.VERSION.GL_1_1 import GL_LIGHT0, GL_POSITION

position_look = {
    49: (0, 0, 10, 0, 0, 0, 0, 1, 0),
    50: (0, 0, 20, 0, 0, 0, 0, 1, 0),
}

position_rotate = {
    51: (-15.0, 1.0, 0.0, 0.0),
    52: (-15.0, 0.0, 1.0, 0.0),
    53: (-15.0, 0.0, 0.0, 1.0),
}

position_translate = {
    97: (0.1, 0.0, 0.0),
    100: (-0.1, 0.0, 0.0),
    119: (0.0, 0.1, 0.0),
    115: (0.0, -0.1, 0.0),
    113: (0.0, 0.0, 0.1),
    101: (0.0, 0.0, -0.1),
}

light_by_key = {
    112: (GL_LIGHT0, GL_POSITION, [20., 2., -2., 1.]),
    111: (GL_LIGHT0, GL_POSITION, [-20., 2., -2., 1.]),
    108: (GL_LIGHT0, GL_POSITION, [20., 20., -2., 1.])
}
