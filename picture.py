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
purple = Color(0xedcc9b, 1.0)
green = Color(0xce27d3, 0.5)
white = Color(0xffffff, 1.0)
black = Color(0x000000, 1.0)
thinline = LineStyle(1, black)

rectangle = RectangleAsset(50, 20, thinline, purple)
square = RectangleAsset(100, 100, thinline, green)
ellipse = EllipseAsset(200, 50, thinline, purple)
triangle = PolygonAsset([(100,100), (50, 60), (200,70)], thinline, green)

Sprite(rectangle, (200, 60))
Sprite(square, (210, 50))
Sprite(ellipse, (290, 400))
Sprite(triangle, (300, 300))


# add your code here /\  /\  /\


myapp = App()
myapp.run()
