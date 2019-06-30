class CameraHelper:
    def __init__(self):
        self.angle = 0.0
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.lx = 0.0
        self.ly = -1.0
        self.lz = 0.0
        self.is_first = True

    def get_look_at(self):
        return self.x, self.y, self.z, \
               self.x + self.lx, self.y + self.ly, self.z + self.lz, \
               0.0, 1.0, 0.0
