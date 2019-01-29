"""
picture.py
Author: Andrew Enelow
Credit: stack overflow, brython server, trinket.io, [Alec, Matt (Not for code)]

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
yellow = Color(0xFFFF00, 1.0)
skyblue = Color(0x87CEEB, 1.0)
grey = Color(0x696969, 1.0)
brick = Color(0xA52A2A, 1.0)
khaki = Color(0xF0E68C, 1.0)

thinline = LineStyle(1, black)

sky = RectangleAsset(1500, 500, thinline, skyblue)

sun = CircleAsset(50, thinline, yellow)

grass = RectangleAsset(1500, 100, thinline, green)

roof = PolygonAsset([(0,100), (200,0), (400,100), (0,100)], thinline, grey)

house = RectangleAsset(300, 300, thinline, khaki)

pond = EllipseAsset(50, 20, thinline, blue)

polygon = PolygonAsset([(0,0), (50,50), (50,100), (0,0)], thinline, red)

chim = RectangleAsset(50, 125, thinline, brick)

door = RectangleAsset(100, 175, thinline, brick)

window = RectangleAsset(25, 50, thinline, black)

knob = CircleAsset(5, thinline, khaki)

Sprite(sky, (0, 0))

Sprite(sun, (50, 50))

Sprite(grass, (0, 500))

Sprite(house, (500, 200))

Sprite(chim, (725, 75))

Sprite(roof, (450, 100))

Sprite(pond, (850, 525))

Sprite(door, (600, 325))

Sprite(window, (620, 350))

Sprite(window, (655, 350))

Sprite(knob, (680, 450))

myapp = App()
myapp.width = 1600
myapp.height = 900
myapp.run()
