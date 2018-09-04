"""
picture.py
Author: Christopher Lee
Credit: https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics


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
#Colors
red = Color(0xff0000, 1.0)
green = Color(0xff000, 1.0)
blue = Color(0x0000ff, 1.0)
yellow = Color(0xffff00, 1.0)
#Line
line = LineStyle(1,red)
linegreen = LineStyle(1, green)
#Asset
rectangle = RectangleAsset(100, 100, line, red)
rectanglebig = RectangleAsset(100, 100, linegreen, green)
rectangleblue = RectangleAsset(100, 100, line, blue)
circle = CircleAsset(50, line, yellow)
circleblue = CircleAsset(50, line, blue)
ellipse = EllipseAsset(35, 35, line, green)
poly = PolygonAsset([(0,300), (0,400), (700, 400), (700, 300)], linegreen, green)
tri = PolygonAsset([(0,100), (50, 0), (100, 100), ], line, blue
#Sprite

Sprite(rectangle, (300, 200)) #house
Sprite(circle) #Sun
Sprite(poly, (0, 300)) #Land
Sprite(tri)
# add your code here /\  /\  /\


myapp = App()
myapp.run()
