from vectors import *


class Matrix2D(object):
    def __init__(self, a11=0, a12=0, a21=0, a22=0):
        self.a11 = a11
        self.a12 = a12
        self.a21 = a21
        self.a22 = a22

    def times(self, vector):
        v = Vector2D()

        v.x = self.a11 * vector.x + self.a12 * vector.y
        v.y = self.a21 * vector.x + self.a22 * vector.y

        return v


class RotationMatrix2D(Matrix2D):
    def __init__(self, theta=0):
        super().__init__(cos(theta), -sin(theta), sin(theta), cos(theta))

        self.theta = theta
        self.thetaR = toRadians(theta)


class Matrix3D(object):
    def __init__(self, a11=0, a12=0, a13=0, a21=0, a22=0, a23=0, a31=0, a32=0, a33=0):
        self.a11 = a11
        self.a12 = a12
        self.a13 = a13
        self.a21 = a21
        self.a22 = a22
        self.a23 = a23
        self.a31 = a31
        self.a32 = a32
        self.a33 = a33

    def timesVector(self, vector):
        x = self.a11 * vector.x + self.a12 * vector.y + self.a13 * vector.z
        y = self.a21 * vector.x + self.a22 * vector.y + self.a23 * vector.z
        z = self.a31 * vector.x + self.a32 * vector.y + self.a33 * vector.z

        return v3(x, y, z)

    def timesMatrix(self, matrix):
        m = Matrix3D()

        m.a11 = self.a11 * matrix.a11 + self.a12 * matrix.a21 + self.a13 * matrix.a31
        m.a12 = self.a11 * matrix.a12 + self.a12 * matrix.a22 + self.a13 * matrix.a32
        m.a13 = self.a11 * matrix.a13 + self.a12 * matrix.a23 + self.a13 * matrix.a33
        m.a21 = self.a21 * matrix.a11 + self.a22 * matrix.a21 + self.a23 * matrix.a31
        m.a22 = self.a21 * matrix.a12 + self.a22 * matrix.a22 + self.a23 * matrix.a32
        m.a23 = self.a21 * matrix.a13 + self.a22 * matrix.a23 + self.a23 * matrix.a33
        m.a31 = self.a31 * matrix.a11 + self.a32 * matrix.a21 + self.a33 * matrix.a31
        m.a32 = self.a31 * matrix.a12 + self.a32 * matrix.a22 + self.a33 * matrix.a32
        m.a33 = self.a31 * matrix.a13 + self.a32 * matrix.a23 + self.a33 * matrix.a33

        return m
