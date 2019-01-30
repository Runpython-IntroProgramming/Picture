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

thinline = LineStyle(1, grey)
thinline1 = LineStyle(1,grey)

tank = RectangleAsset(900,600, thinline, lightblue)
pebbles = RectangleAsset(900, 45, thinline, brown)
castle = RectangleAsset(350, 190, thinline, grey)
castletop = PolygonAsset([(40,60), (80,-45), (120,60)],thinline, grey)
castletop2 = PolygonAsset([(40,60), (62.5,-30), (85,60)],thinline, grey)
tower = RectangleAsset(80, 100, thinline, grey)
centertower = RectangleAsset(150, 140, thinline, grey)
centertower2 = RectangleAsset(45, 50, thinline, grey)

Sprite(tank, (100,110))
Sprite(pebbles, (100,665))
Sprite(castle, (600,480))
Sprite(tower, (600,390))
Sprite(castletop, (600,285))
Sprite(tower, (870,390))
Sprite(castletop, (870,285))
Sprite(centertower, (700,350))
Sprite(tower, (735,280))
Sprite(castletop2, (750,140))
Sprite(centertower2, (750,230))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
