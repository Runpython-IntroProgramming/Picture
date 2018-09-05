"""
picture.py
Author: Patrick Daley
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
from ggame import App, Color, LineStyle, Sprite
black = Color(0x000000, 1.0)
brown = COlor(0x1654242, 1.0
thinline = LineStyle(1, black)
rectangle = RectangleAsset(500, 500, thinline, black)
Sprite(rectangle, (250, 250))

triangle = PolygonAsset([(-250, 250), (0,0), (250, 250)], thinline, black)
Sprite( triangle, (250, 0))
#poly = PolygonAsset([(250, 250), (100, 100), (100, 250)], thinline, black)
#Sprite(poly, (250,250))
#circle =  CircleAsset(200, thinline, black)
#Sprite(circle, (200, 250))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
