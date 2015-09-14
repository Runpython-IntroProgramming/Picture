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
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/TUTORIAL:-Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
white= Color(0xffffff, 1.0)
black= Color(0x000000, 1.0)
redroof= Color(0xff0000, 1.0)
thinline = LineStyle(1, black)
rectanglehouse = RectangleAsset(500, 500, thinline, white)
Sprite(rectanglehouse, (550,250))
triangle= PolygonAsset([(550, 250), (1050, 250), (800, 50)], thinline, redroof)
Sprite(triangle)
chimney= RectangleAsset(50, 100, thinline, redroof)
Sprite(chimney, (550, 250))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
