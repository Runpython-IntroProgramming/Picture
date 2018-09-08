"""
picture.py
Author: Jackson Lake
Credit: Schoology tutorial

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
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset


red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
grey = Color(0xCDC0B0, 1.0)
firebrick1 = Color(0xFF3030, 1.0)
purple = Color(0xBF3EFF, 1.0)
gold = Color(0xFFD700, 1.0)
fade1 = Color(0xff0000, 0.6)
fade2 = Color(0xff0000, 0.4)
fade3 = Color(0xff0000, 0.2)
white = Color(0xF8F8FF, 1.0)
violet = Color(0xd147c5, 1.0)

thinline = LineStyle(1, black)
thinner = LineStyle(.4, red)

head = RectangleAsset(120, 100, thinline, grey)
neck = RectangleAsset(40, 28, thinline, grey)
body = RectangleAsset(200, 200, thinline, grey)
leg1 = RectangleAsset(45, 90, thinline, grey)
leg2 = RectangleAsset(45, 90, thinline, grey)
eye1 = CircleAsset(15, thinline, firebrick1)
eye2 = CircleAsset(15, thinline, firebrick1)
shoulder1 = CircleAsset(20, thinline, grey)
shoulder2 = CircleAsset(20, thinline, grey)
arm1 = RectangleAsset(100, 40, thinline, grey)
arm2 = RectangleAsset(100, 40, thinline, grey)
antenna = EllipseAsset(5, 40, thinline, purple)
mouth = EllipseAsset(30, 8, thinline, gold)
lip = RectangleAsset(59, 1, thinline, black)
wave1 = CircleAsset(10, thinner, fade1)
wave2 = CircleAsset(25, thinner, fade2)
wave3 = CircleAsset(42, thinner, fade3)
emblem = CircleAsset(37, thinline)
design = PolygonAsset([(0,0), (20, 50), (40,0)], thinline, violet)

Sprite(antenna, (485, 65))
Sprite(head, (432, 100))
Sprite(neck, (470, 200))
Sprite(body, (400, 228))
Sprite(leg1, (400, 428))
Sprite(leg2, (555, 428))
Sprite(eye1, (440, 115))
Sprite(eye2, (510, 115))
Sprite(arm1, (600, 228))
Sprite(arm2, (300, 228))
Sprite(shoulder1, (580, 228))
Sprite(shoulder2, (380, 228))
Sprite(mouth, (460, 165))
Sprite(lip, (460, 173))
Sprite(wave1, (480, 60))
Sprite(wave2, (465, 43))
Sprite(wave3, (447, 26))
Sprite(emblem, (465, 260))
Sprite(design, (480, 275))




# add your code here /\  /\  /\


myapp = App()
myapp.run()
