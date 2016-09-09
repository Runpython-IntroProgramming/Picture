"""
picture.py
Author: Matthew Fenner
Credit: None

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
red = Color(0xff7043, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
yellow = Color(0xffd54f, 0.9)
ltgray = Color(0xe0e0e0, 1.0)
roof = Color(0xbbdefb, 1.0)


thinline = LineStyle(1, black)

housebase = RectangleAsset(100, 50, thinline, red)
houseroof = PolygonAsset(([(300, 700), (400, 700), (350, 650), (350, 700)]), thinline, roof)
houseroof2 = PolygonAsset(([(200, 700), (300, 700), (350, 650), (350, 700)]), thinline, roof)
sun = EllipseAsset(100, 100, thinline, yellow)
pillar = RectangleAsset(2, 50, thinline, red)
door = RectangleAsset(20, 25, thinline, blue)
window = CircleAsset(10, thinline, ltgray)
wbara = RectangleAsset(20, .5, thinline, black)
wbarb = RectangleAsset(0.0005, 20, thinline, black)
chimney = RectangleAsset(12.5, 45, thinline, red)

Sprite(chimney, (325, 640))
Sprite(housebase, (300, 700))
Sprite(houseroof)
Sprite(houseroof2)
Sprite(sun)
Sprite(pillar, (200, 700))
Sprite(door, (340, 725))
Sprite(window, (350, 712.5))
Sprite(wbara, (340, 712.5))
Sprite(wbarb, (350, 702))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
