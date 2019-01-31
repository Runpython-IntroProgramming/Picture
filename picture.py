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
lightblue = Color(0x7ec0ee,1.0)
brown = Color(0x5D3909, 1.0)
tan = Color(0xFFE4B5, 1.0)
grey = Color(0x8B8989, 1.0)
red = Color(0xCD2626, 1.0)
black = Color(0x000000, 0.7)
black1 = Color(0x000000, 0.7)
green = Color(0x228B22, 1.0)
thinline = LineStyle(1, grey)
thinline1 = LineStyle(1, brown)
thinline2 = LineStyle(1, black1)
thinline3 = LineStyle(1, green)


tank = RectangleAsset(900,600, thinline2, lightblue)
pebbles = RectangleAsset(900, 45, thinline2, tan)
castle = RectangleAsset(350, 190, thinline, grey)
castletop = PolygonAsset([(40,60), (80,-45), (120,60)],thinline, red)
castletop1 = PolygonAsset([(40,60), (62.5,-30), (85,60)],thinline, red)
centertower = RectangleAsset(150, 140, thinline, grey)
centertower1 = RectangleAsset(45, 50, thinline, grey)
tower = RectangleAsset(80, 100, thinline, grey)
ridge = RectangleAsset(10, 25, thinline, lightblue)
ridge1 = RectangleAsset(8, 20, thinline, lightblue)
windows = RectangleAsset(130, 130, thinline, brown)
windows1 = RectangleAsset(40, 50, thinline, black)
windows2 = EllipseAsset(63, 80, thinline1, brown)
windows3 = RectangleAsset(20, 30, thinline1, black)
line = PolygonAsset([(40,60), (40,-105), (40,60)],thinline2, black)
doorknob = EllipseAsset(8, 8, thinline1, black)
plant = RectangleAsset(10, 250, thinline3, green)
plant1 = RectangleAsset(5, 110, thinline3, green)
leaves = EllipseAsset(8, 20, thinline3, green)
leaves1 = RectangleAsset(2, 30, thinline3, green)

Sprite(tank, (100,110))
Sprite(pebbles, (100,665))
Sprite(castle, (600,480))
Sprite(tower, (600,390))
Sprite(castletop, (600,285))
Sprite(tower, (870,390))
Sprite(castletop, (870,285))
Sprite(centertower, (700,350))
Sprite(tower, (735,280))
Sprite(castletop1, (750,140))
Sprite(centertower1, (750,230))
Sprite(ridge, (708,350))
Sprite(ridge, (738,350))
Sprite(ridge, (768,350))
Sprite(ridge, (798,350))
Sprite(ridge, (828,350))
Sprite(ridge1, (740,280))
Sprite(ridge1, (760,280))
Sprite(ridge1, (780,280))
Sprite(ridge1, (800,280))
Sprite(windows, (710,540))
Sprite(windows1, (620,410))
Sprite(windows1, (890,410))
Sprite(windows2, (711,505))
Sprite(windows3, (762.5,238))
Sprite(line, (773,505))
Sprite(plant, (175,417))
a = Sprite(leaves, (186,448))
a.rotation = 2.2
a = Sprite(leaves, (185,450))
a.rotation = 3.9
a = Sprite(leaves, (185,480))
a.rotation = 2.2
a = Sprite(leaves, (185,490))
a.rotation = 3.9
a = Sprite(leaves, (185,515))
a.rotation = 2.2
a = Sprite(leaves, (185,525))
a.rotation = 3.9
a = Sprite(leaves, (185,550))
a.rotation = 2.2
a = Sprite(leaves, (185,560))
a.rotation = 3.9
a = Sprite(leaves, (185,585))
a.rotation = 2.2
a = Sprite(leaves, (185,595))
a.rotation = 3.9
a = Sprite(leaves, (185,620))
a.rotation = 2.2
a = Sprite(leaves, (185,630))
a.rotation = 3.9
a = Sprite(leaves, (185,655))
a.rotation = 2.2
Sprite(plant1, (280,556))
b = Sprite(leaves1, (282,630))
b.rotation = 3.9
b = Sprite(leaves1, (282,655))
b.rotation = 2.2
b = Sprite(leaves1, (282,590))
b.rotation = 3.9
b = Sprite(leaves1, (282,615))
b.rotation = 2.2
b = Sprite(leaves1, (282,575))
b.rotation = 2.2
# add your code here /\  /\  /\


myapp = App()
myapp.run()
