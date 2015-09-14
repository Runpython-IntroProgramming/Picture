"""
picture.py
Author: Jasmine Lou
Credit: The internet, classmates

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/TUTORIAL:-Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset


# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
seafoam = Color(0x58FAD0, 1.0)
navy = Color(0x08088A, 1.0)
gray = Color(0xA4A4A4, 1.0)
darkgray = Color(0x585858, 1.0)
white = Color(0xffffff, 1.0)


thinline = LineStyle(1, black)
mediumline = LineStyle(3, black)
thickline = LineStyle(5, black)
redline = LineStyle(3, red)
noline = LineStyle(0, red)

rectangle = RectangleAsset(500, 200, noline, navy)
rectangle2 = RectangleAsset(500, 200, noline, seafoam)
circle = CircleAsset(30, noline, darkgray)
road = RectangleAsset(2000, 30, noline, gray)
cartriangle1 = PolygonAsset([(0, 0), (0, 125), (175, 0)], noline, white)
cartriangle2 = PolygonAsset([(0, 100), (0, 0), (-30, 0)], noline, white)

# Now display a rectangle
Sprite(rectangle, (100, 200))
Sprite(circle, (475, 400))
Sprite(circle, (225, 400))
Sprite(cartriangle1, (100, 200))
Sprite(cartriangle2, (600, 200))

Sprite(rectangle2, (700, 200))
Sprite(circle, (1075, 400))
Sprite(circle, (825, 400))
Sprite(cartriangle1, (700, 200))
Sprite(cartriangle2, (1200, 200))

Sprite(road, (0, 430))

myapp = App()
myapp.run()
