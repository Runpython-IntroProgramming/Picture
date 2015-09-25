"""
picture.py
Author: Morgan Meliment
Credit: http://brythonserver.github.io/ggame/#ggame.EllipseAsset

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
brown = Color(0xd38d5f, 1.0)
yellow = Color(0xffd42a, 1.0)
black = Color(0x000000, 1.0)
grey = Color(0x808080, 1.0)
dark = Color(0x333333, 1.0)

stroke = LineStyle(2, black)
nostroke = LineStyle(0, black)
base = RectangleAsset(150, 120, stroke, red)
door = RectangleAsset(40, 60, stroke, brown)
top = PolygonAsset([(90,120), (260,120), (175,50)], stroke, black)
handle = CircleAsset(5, nostroke , black)
floor = EllipseAsset(150, 50, nostroke, green)
sun = CircleAsset(30, nostroke, yellow)
bg = RectangleAsset(350, 350, nostroke, blue)
road = RectangleAsset(350, 150, nostroke, grey)
darkroad = RectangleAsset(350, 50, nostroke, dark)
line = RectangleAsset(350, 5, nostroke, yellow)

Sprite(bg)
Sprite(road, (0, 200))
Sprite(darkroad, (0, 300))
Sprite(line, (0, 320))
Sprite(floor, (170, 230))
Sprite(body, (100, 120))
Sprite(top)
Sprite(door, (155, 180))
Sprite(handle, (185, 210))
Sprite(sun, (50, 50))


myapp = App()
myapp.run()
