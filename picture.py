"""
picture.py
Author: Andrew Enelow
Credit: stack overflow, brython server

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

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

thinline = LineStyle(1, black)

rectangle = RectangleAsset(50, 20, thinline, blue)

circle = CircleAsset(50, thinline, green)

ellipse = EllipseAsset(50, 20, thinline, red)

polygon = PolygonAsset([(0,0), (50,50), (50,100), (0,0)], thinline, red)

Sprite(rectangle, (200, 50))

Sprite(circle, (400, 50))

Sprite(ellipse, (200, 100))

Sprite(polygon, (400, 100))

Sprite(rectangle, (300, 50))

Sprite(rectangle, (400, 50))

Sprite(rectangle, (500, 50))

Sprite(rectangle, (600, 50))

Sprite(rectangle, (700, 50))

Sprite(rectangle, (800, 50))

myapp = App()
myapp.run()
