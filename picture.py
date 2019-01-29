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
lightblue = Color(0xBFEFFF,0.8)
brown = Color(0x8B4726, 0.9)
grey = Color(0xCDC9C9, 1.0)
black = Color(0x000000, 1.0)

thinline = LineStyle(1, black)

tank = RectangleAsset(900,600, thinline, lightblue)
pebbles = RectangleAsset(900, 45, thinline, brown)
castle = RectangleAsset(350, 200, thinline, grey)
castletop = PolygonAsset([(40,60), (127.5,-75), (215,60)],thinline, grey)
tower = RectangleAsset(325, 200, thinline, grey)

Sprite(tank, (100,110))
Sprite(pebbles, (100,665))
Sprite(castle, (600,475))
Sprite(castletop, (600,195))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
