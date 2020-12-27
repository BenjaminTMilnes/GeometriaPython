import math


def toRadians(degrees):
    return (degrees / 360) * 2 * math.pi


def toDegrees(radians):
    return (radians / (2 * math.pi)) * 360


def normaliseAngle(degrees):
    if degrees < 0:
        degrees += math.ceil(-degrees / 360) * 360

    degrees = degrees % 360

    return degrees


def sin(degrees):
    return math.sin(toRadians(degrees))


def cos(degrees):
    return math.cos(toRadians(degrees))


def tan(degrees):
    return math.tan(toRadians(degrees))


def asin(x):
    return toDegrees(math.asin(x))


def acos(x):
    return toDegrees(math.acos(x))


def atan(x):
    return toDegrees(math.atan(x))


def between(minimum, value, maximum):
    if value < minimum:
        return minimum
    elif value > maximum:
        return maximum
    else:
        return value


class Vector2D(object):
    def __init__(self, x=0, y=0):

        self.x = x
        self.y = y

    @staticmethod
    def fromRAndTheta(r, theta):
        return Vector2D(r * cos(theta), r * sin(theta))

    @property
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    @property
    def m(self):
        return self.magnitude

    @property
    def unitVector(self):
        if (self.m == 0):
            return self
        else:
            return self.times(1 / self.m)

    @property
    def u(self):
        return self.unitVector

    @property
    def normalUnitVector(self):
        return self.u.rotate(90)

    @property
    def n(self):
        return self.normalUnitVector

    @property
    def argument(self):
        if self.x == 0:
            if self.y == 0:
                return 0
            elif self.y > 0:
                return 90
            elif self.y < 0:
                return 270

        # the angle between the vector and the nearest side of the x-axis
        theta = atan(abs(self.y / self.x))

        if self.x > 0 and self.y >= 0:
            return theta
        elif self.x < 0 and self.y >= 0:
            return 180 - theta
        elif self.x < 0 and self.y < 0:
            return 180 + theta
        elif self.x > 0 and self.y < 0:
            return 360 - theta

    @property
    def a(self):
        return self.argument

    def argumentFromAxis(self, axis="+x"):
        if axis == "+y":
            return normaliseAngle(self.a - 90)
        if axis == "-x":
            return normaliseAngle(self.a - 180)
        if axis == "-y":
            return normaliseAngle(self.a - 270)

        return self.a

    def add(self, vector):
        v = Vector2D()

        v.x = self.x + vector.x
        v.y = self.y + vector.y

        return v

    def subtract(self, vector):
        v = Vector2D()

        v.x = self.x - vector.x
        v.y = self.y - vector.y

        return v

    def times(self, scalar):
        return self.scale(scalar, scalar)

    def dot(self, vector):
        return self.x * vector.x + self.y * vector.y

    def translate(self, dx=0, dy=0):
        v = Vector2D()

        v.x = self.x + dx
        v.y = self.y + dy

        return v

    def translateX(self, dx):
        return self.translate(dx, 0)

    def translateY(self, dy):
        return self.translate(0, dy)

    def scale(self, sfx=1, sfy=1):
        v = Vector2D()

        v.x = self.x * sfx
        v.y = self.y * sfy

        return v

    def scaleX(self, sfx):
        return self.scale(sfx, 1)

    def scaleY(self, sfy):
        return self.scale(1, sfy)

    def reflect(self):
        return self.scale(-1, -1)

    def reflectX(self):
        return self.scaleX(-1)

    def reflectY(self):
        return self.scaleY(-1)

    def rotate(self, theta):
        v = Vector2D()

        v.x = self.x * cos(theta) + self.y * (-sin(theta))
        v.y = self.x * sin(theta) + self.y * cos(theta)

        return v

    def rotateAboutPoint(self, theta, point):
        v = self.subtract(point)
        v = v.rotate(theta)
        v = v.add(point)

        return v
