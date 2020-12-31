from PIL import Image, ImageDraw, ImageColor
from geometria.vectors import *


class RadialGradient (object):
    def __init__(self, centre = None, radius = None):
        self.centre = centre 
        self.radius = radius 
        self.colourStops = []

    def addColourStop(self, position, colour):
        self.colourStops.append((position, colour))

    def _getColourAtPosition(self, position):
        orderedColourStops = sorted(self.colourStops, key=lambda c: c[0])
        stop1 = orderedColourStops[0]
        stop2 = orderedColourStops[0]

        for stop in orderedColourStops:
            if stop[0] <= position:
                stop1 = stop 
                stop2 = stop 
            if stop[0] >= position:
                stop2 = stop 
                break 

        colour1 = ImageColor.getrgb(stop1[1])
        colour2 = ImageColor.getrgb(stop2[1])
        dp = stop2[0] - stop1[0]
        cr = 0 if dp == 0 else (position - stop1[0]) / dp

        r1 = colour1[0]
        g1 = colour1[1]
        b1 = colour1[2]
        #a1 = colour1[3]
        
        r2 = colour2[0]
        g2 = colour2[1]
        b2 = colour2[2]
        #a2 = colour2[3]

        dr = r2 - r1 
        dg = g2 - g1 
        db = b2 - b1 

        r3 = int( r1 + dr * cr)
        g3 = int( g1 + dg * cr)
        b3 = int( b1 + db * cr)
        #a3 = (a1 + a2) / 2

        return (r3, g3, b3)

    def getColourAtPosition(self, position):
        m = separation(position, self.centre)
        p = m / self.radius 

        return self._getColourAtPosition(p)





class GraphicsContext(object):
    def __init__(self, image=None):
        self.image = image
        self.draw = ImageDraw.Draw(self.image)

    @staticmethod
    def fromWidthAndHeight(width, height, colourMode="RGBA"):
        image = Image.new(colourMode, (width, height))
        graphics = GraphicsContext(image)

        return graphics

    def clear(self, fillColour="white"):
        e1 = v2(0, 0)
        e2 = v2(self.image.width, 0)
        e3 = v2(self.image.width, self.image.height)
        e4 = v2(0, self.image.height)

        self.drawPath([e1, e2, e3, e4], fillColour, "none", 0)

    def _drawRadialGradient(self, gradient):
        w = self.image.width 
        h = self.image.height 

        for x in range(w):
            for y in range(h):
                self.image.putpixel((x, y), gradient.getColourAtPosition(v2(x,y)))

    def drawCircle(self, centre, radius,  fillColour = "none", lineColour="black", lineWidth=1, lineDashStyle = []):
        self.drawCircularArc(centre, radius, 0, 360, fillColour, lineColour, lineWidth, lineDashStyle)

    def drawCircularArc(self, centre, radius, fromAngle, toAngle, fillColour = "none", lineColour="black", lineWidth=1, lineDashStyle = []):
        e1 = centre.add(v2(-radius, -radius))
        e2 = centre.add(v2(radius, radius))

        if isinstance(fillColour, RadialGradient):
            self._drawRadialGradient(fillColour)
        else:
            fc = None if fillColour == "none" else  ImageColor.getrgb(fillColour)
            lc = None if lineColour == "none" else  ImageColor.getrgb(lineColour)

            self.draw.pieslice([(e1.x, e1.y), (e2.x, e2.y)], fromAngle, toAngle, fill=fc)

    def drawPath(self, vertices, fillColour="none", lineColour="black", lineWidth=1, lineDashStyle=[]):
        xy = [(vertex.x, vertex.y) for vertex in vertices]
        fc = None if fillColour == "none" else  ImageColor.getrgb(fillColour)
        lc = None if lineColour == "none" else  ImageColor.getrgb(lineColour)

        self.draw.polygon(xy, fc, lc)

    def drawLine(self, vertex1, vertex2, lineColour="black", lineWidth=1, lineDashStyle=[] ):
        xy = [(vertex1.x, vertex1.y), (vertex2.x, vertex2.y)]
        lc = None if lineColour == "none" else  ImageColor.getrgb(lineColour)

        self.draw.line(xy, lc, lineWidth, None)
