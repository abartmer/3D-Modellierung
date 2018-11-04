# -------------------------------------------------------------------------------------------------------------------- #
#                               Praktikum "mathematische Modellierung am Recher 2"                                     #
#                                       Abschnitt 2: 3D-Visualisierung                                                 #
#                                                                                                                      #
#                           Sean Genkel, André Wetzel, Marko Rubinić, Aron Bartmer-Freund                              #
#                                                                                                                      #
# -------------------------------------------------------------------------------------------------------------------- #

""" Wir benötigen Punkte im dreidimensionalen Raum P = (x,y,z), Linien dazwischen L = (P1, P2) sowie Polygone, die sich
aus Letzteren zusammensetzen Poly = (P1,P2,P3) """


class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


class Line:
    def __init__(self, point1=None, point2=None):
        self.point1 = point1 or Point()  # (0,0,0) by default
        self.point2 = point2 or Point()  # (0,0,0) by default


class Vector:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self._a = Point(x1, y1, z1)
        self._b = Point(x2, y2, z2)

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    # Route from Point a to Point b

    @property
    def i(self):
        return self.b.x - self.a.x

    @property
    def j(self):
        return self.b.y - self.a.y

    @property
    def k(self):
        return self.b.z - self.a.z

    def length(self):
        return (self.i ** 2 + self.j ** 2 + self.k ** 2) ** (1 / 2)


class Polygon:
    # n = size of each individual polygon
    # *argv = list of arbitrary length (in this case 3-tuples (x,y,z))
    def __init__(self, n, *argv):
        self.size = 0
        points = []
        # check format, each point consists of (x,y,z)
        for point in argv:
            if len(point) == 3:
                points.append(point)
                self.size += 1
            else:
                raise TypeError("Element " + str(point) + " needs to have 3 coordinates")

        if len(points) < 3:
            raise TypeError("A Polygon consists of at least 3 points")

        # Slice array into smaller arrays of size n (a cube consists of n=6 polygons)
        poly = []
        while len(points) > n:
            sliced = points[:n]
            poly.append(sliced)
            points = points[1:]

        # e.g.: polygons = [[(a,b,c),(d,e,f),(g,h,i)],[(),(),()],...]
        self.polygons = poly

    def size(self):
        return self.size


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

teeest = Polygon(4, *cube)
print(teeest.size)
print(teeest.polygons)

test = Vector(1, 2, 3, 4, 5, 6)
print(test.length())
testpoint = Point(8, 9, 10)
testpoint2 = Point(4, 7, 10)
test2 = Vector(testpoint.x, testpoint.y, testpoint.z, testpoint2.x, testpoint2.y, testpoint2.z)
