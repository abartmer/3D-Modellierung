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
        a = 200
        b = 500
        c = 60
        d = 120
        cube1 = Polygon((a, a, d), (a, b, d), (b, b, d), (b, a, d))
        cube2 = Polygon((a, a, c), (a, a, d), (b, a, d), (b, a, c))
        cube3 = Polygon((a, a, c), (a, b, c), (a, b, d), (a, a, d))
        cube4 = Polygon((a, a, c), (a, b, d), (b, b, d), (b, b, c))
        cube5 = Polygon((b, a, d), (b, b, d), (b, b, c), (b, a, c))
        cube6 = Polygon((a, a, d), (a, b, c), (b, b, d), (b, a, c))

        cub_obj = []
        cub_obj.append([cube1])
        cub_obj.append([cube2])
        cub_obj.append([cube3])
        cub_obj.append([cube4])
        cub_obj.append([cube5])
        cub_obj.append([cube6])

        self.painter = qg.QPainter(self.canvas)
        self.painter.setPen(qg.QPen(qc.Qt.red, 5, qc.Qt.SolidLine))
        self.painter.setBrush(qg.QBrush(qc.Qt.red, qc.Qt.SolidPattern))

        for poly in cub_obj:
            x = poly[0] + 0.5 * np.sqrt(2) * poly[2]
            y = poly[1] + 0.5 * np.sqrt(2) * poly[2]
            self.painter.drawPoint(x, y)

        index = 0
        for point in range(len(cube_obj.points) - 1):
            x = cube_obj.points[point][0] + 0.5 * np.sqrt(2) * cube_obj.points[point][2]
            y = cube_obj.points[point][1] + 0.5 * np.sqrt(2) * cube_obj.points[point][2]
            x2 = cube_obj.points[point + 1][0] + 0.5 * np.sqrt(2) * cube_obj.points[point + 1][2]
            y2 = cube_obj.points[point + 1][1] + 0.5 * np.sqrt(2) * cube_obj.points[point + 1][2]
            self.painter.drawLine(x, y, x2, y2)
            index += 1

        self.display.setPixmap(self.canvas)

# Start app
if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    View = Viewer()
    sys.exit(app.exec_())
