from PIL import Image, ImageDraw, ImageColor
from vectors import *


class GraphicsContext(object):
    def __init__(self, image=None):
        self.image = image
        self.draw = ImageDraw.Draw(self.image)

    @staticmethod
    def fromWidthAndHeight(width, height, colourMode="RGBA"):
        image = Image.new(colourMode, (width, height))
        graphics = GraphicsContext(image)

        return graphics

    def clear(fillColour="white"):
        e1 = v2(0, 0)
        e2 = v2(self.image.width, 0)
        e3 = v2(self.image.width, self.image.height)
        e4 = v2(0, self.image.height)

        self.drawPath([e1, e2, e3, e4], fillColour, "none", 0)

    def drawCircularArc(centre, radius, fromAngle, toAngle, fillColour = "none", lineColour="black", lineWidth=1, lineDashStyle = []):
        e1 = centre.add(v2(-radius, -radius))
        e2 = centre.add(v2(radius, radius))

        self.draw.arc([(e1.x, e1.y), (e2.x, e2.y)], fromAngle, toAngle, lineColour, lineWidth)

    def drawPath(vertices, fillColour="none", lineColour="black", lineWidth=1, lineDashStyle=[]):
        xy = [(vertex.x, vertex.y) for vertex in vertices]

        self.draw.polygon(xy, ImageColor.getrgb(fillColour),
                          ImageColor.getrgb(lineColour))
