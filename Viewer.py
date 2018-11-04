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
        a = 250
        b = 500
        c = 60
        d = 120
        cube = [(a, a, d), (a, b, d), (b, b, d), (b, a, d),
                (a, a, c), (a, a, d), (b, a, d), (b, a, c),
                (a, a, c), (a, b, c), (a, b, d), (a, a, d),
                (a, a, c), (a, b, d), (b, b, d), (b, b, c),
                (b, a, d), (b, b, d), (b, b, c), (b, a, c),
                (a, a, d), (a, b, c), (b, b, d), (b, a, c)]
        cube_obj = Polygon(*cube)

        self.painter = qg.QPainter(self.canvas)
        self.painter.setPen(qg.QPen(qc.Qt.red, 5, qc.Qt.SolidLine))
        self.painter.setBrush(qg.QBrush(qc.Qt.red, qc.Qt.SolidPattern))

        for point in cube_obj.points:
            self.painter.drawPoint(point[0] + 0.5 * np.sqrt(2) * point[2], point[1] + 0.5 * np.sqrt(2) * point[2])

        self.display.setPixmap(self.canvas)


# Start app
if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    View = Viewer()
    sys.exit(app.exec_())
