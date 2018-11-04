import sys
from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui as qg
from PyQt5 import QtCore as qc
from Polygons import Polygon
import numpy as np


class Viewer(qw.QMainWindow):
    def __init__(self):
        super(qw.QMainWindow, self).__init__()

        self.init_window()
        self.init_canvas()

        self.draw_polygon_cav()

        self.show()

    def init_window(self):
        self.height = 800
        self.width = 800
        self.setWindowTitle("3D Viewer")
        self.setFixedSize(self.width, self.height)

    def init_canvas(self):
        self.display = qw.QLabel()
        self.setCentralWidget(self.display)

        self.canvas = qg.QPixmap(self.width, self.height)
        self.painter = qg.QPainter(self.canvas)
        self.painter.fillRect(0, 0, self.width, self.height, qc.Qt.white)
        self.painter.end()

        self.display.setPixmap(self.canvas)

    def draw_polygon_cav(self):

        self.painter = qg.QPainter(self.canvas)
        self.painter.setPen(qg.QPen(qc.Qt.red, 5, qc.Qt.SolidLine))
        self.painter.setBrush(qg.QBrush(qc.Qt.red, qc.Qt.SolidPattern))

        for poly in cube_obj.polygons:
            x = poly[0][0] + 0.5 * np.sqrt(2) * poly[0][2]
            y = poly[0][1] + 0.5 * np.sqrt(2) * poly[0][2]
            self.painter.drawPoint(x, y)

        self.display.setPixmap(self.canvas)


""" attempting to draw a line from starting point to the following point (start = end)
        for i in cube_obj.polygons:
            for poly in range(len(cube_obj.polygons) - 1):
                x1 = cube_obj.polygons[i][poly][0]
                x2 = cube_obj.polygons[i][poly + 1][0]
                y1 = cube_obj.polygons[i][poly][1]
                y2 = cube_obj.polygons[i][poly + 1][1]
                self.painter.drawLine(x1, y1, x2, y2)"""


"""     for poly in range(len(cube_obj.polygons) - 1):
            x1 = (cube_obj.polygons[poly][0][0] + 0.5 * np.sqrt(2) * cube_obj.polygons[poly][0][2])
            y1 = (cube_obj.polygons[poly][0][1] + 0.5 * np.sqrt(2) * cube_obj.polygons[poly][0][2])
            x2 = (cube_obj.polygons[poly][1][0] + 0.5 * np.sqrt(2) * cube_obj.polygons[poly][1][2])
            y2 = (cube_obj.polygons[poly][1][1] + 0.5 * np.sqrt(2) * cube_obj.polygons[poly][1][2])
            self.painter.drawLine(x1, y1, x2, y2)"""


# -------------------------------------------------- Testing --------------------------------------------------------- #

a = 200
b = 500
c = 60
d = 120
cube = [(a, a, d), (a, b, d), (b, b, d), (b, a, d),
        (a, a, c), (a, a, d), (b, a, d), (b, a, c),
        (a, a, c), (a, b, c), (a, b, d), (a, a, d),
        (a, a, c), (a, b, d), (b, b, d), (b, b, c),
        (b, a, d), (b, b, d), (b, b, c), (b, a, c),
        (a, a, d), (a, b, c), (b, b, d), (b, a, c)]
cube_obj = Polygon(4, *cube)

# Start app
if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    View = Viewer()
    sys.exit(app.exec_())
