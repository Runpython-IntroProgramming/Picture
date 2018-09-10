"""
picture.py
Author: Joe Richter
Credit: https://www.webucator.com/blog/2015/03/python-color-constants-module/, and myself

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
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/


# add your code here /\  /\  /\
from ggame import App
myapp = App()
myapp.run()
hair=Color(0x8B4C39, 1.0)
black=Color(0x000000, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
white = Color(0xf8f8ff, 1.0)
thinline = LineStyle(1, black)
rectangle = RectangleAsset(15, 50, thinline, red)
rectangleRed = RectangleAsset(75, 20, thinline, red)
circle = CircleAsset (200, thinline, white)
ellipse = EllipseAsset (45, 45, thinline, blue)
polygon = PolygonAsset ([(2,5), (1,0), (2,5)], thinline, green)
rectangleLong = RectangleAsset(200, 20, thinline, red)
line1 = RectangleAsset(1, 20, thinline, black)
line2 = RectangleAsset(20, 1, thinline, black)
line3 = RectangleAsset(20, 1, thinline, black)
line4 = RectangleAsset(1, 20, thinline, black)
line5 = RectangleAsset(1, 20, thinline, black)
Sprite(circle, (10, 0))
#Face
Sprite(rectangleRed, (120,50))
#Brow1
Sprite(rectangleRed, (230,50))
#Brow2
Sprite(ellipse, (113, 75))
#Eye1
Sprite(ellipse, (225, 75))
#Eye2
Sprite(rectangle, (205, 160))
#Nose
Sprite(rectangleLong, (115, 250))
#Mouth
Sprite(line1, (210, 400))
#UpperBody
Sprite(line2, (210,405))
Sprite(line3, (190,405))
Sprite(line4, (212,419))
Sprite(line5, (208,419))
Sprite(polygon, (0,0))