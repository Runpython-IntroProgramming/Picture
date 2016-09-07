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
red = Color(0xff4200, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

normalLine = LineStyle(1, black)

ellipse = EllipseAsset(50, 150, normalLine, black)
rectangle = RectangleAsset(700, 200, normalLine, blue)
rectangle2 = RectangleAsset(150, 150, normalLine, blue)
polygon = PolygonAsset([(0, 0), (300, 300), (660, 100), (0, 0)], normalLine, green)
circle = CircleAsset(70, normalLine, red)


Sprite(rectangle2, (550, 200))
Sprite(rectangle, (500, 50))
Sprite(circle, (800, 200))
Sprite(circle, (1100, 200))
Sprite(polygon, (1100, 200))
Sprite(polygon, (800, 200))
Sprite(ellipse, (625, 200))
Sprite(ellipse, (625, 300))
Sprite(ellipse, (625, 400))
Sprite(ellipse, (625, 500))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
