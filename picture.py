"""
picture.py
Author: <your name here>
Credit: <list sources used, if any>

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
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
yellow = Color(0xFFFF00, 1.0)

#line style
thinline = LineStyle(1, black)

#shape assets
rectangle = RectangleAsset(50, 20, thinline, blue)
Circle = CircleAsset(50, thinline, yellow)
triangle = PolygonAsset([(0, 0), (100, -200), (200, 0)], thinline, green)
rectangle1 = RectangleAsset(200, 300, thinline, green)
ellipse = EllipseAsset(40, thinline, red)
#display the shapes 

Sprite(rectangle, (50, 20))
Sprite(Circle, (500, 500))
Sprite(triangle, (506, 450))
Sprite(rectangle1, (200, 200))
Sprite(rectangle, (400, 500))
Sprite(ellipse, (40, 70))


# add your code here /\  /\  /\


myapp = App()
myapp.run()
