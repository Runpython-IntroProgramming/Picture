"""
picture.py
Author: <Vinzent>
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
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

darkoragne = Color(0xFF9800, 1.0)
greywhite = Color(0xF5F5F5, 1.0)
lightblue = Color(0x03A9F4, 1.0)
oceanblue = Color(0x283593, 1.0)
beachyellow = Color(0xFFD54F, 1.0)
reflectionyellow = Color(0xFFC107, 1.0)

noline = LineStyle(0, greywhite)
thinline = LineStyle(1, greywhite)

background = RectangleAsset(10, 10, thinline, lightblue)
sun = CircleAsset(180, thinline, darkoragne)
ocean = RectangleAsset(1920, 1000, thinline, oceanblue)
beach = RectangleAsset(1920, 1000, thinline, beachyellow)
reflection = RectangleAsset(30, 30, noline, reflectionyellow)

for x in range(500):

    Sprite(background, (0, 0))

"""
Sprite(background, (0, 0))
Sprite(background, (10, 0))
Sprite(background, (20, 0))
Sprite(background, (30, 0))
Sprite(background, (40, 0))
Sprite(background, (50, 0))
Sprite(background, (60, 0))
Sprite(background, (70, 0))
Sprite(background, (80, 0))
Sprite(background, (90, 0))
Sprite(background, (100, 0))
Sprite(background, (110, 0))
Sprite(background, (120, 0))
Sprite(background, (130, 0))
Sprite(background, (140, 0))
Sprite(background, (150, 0))
Sprite(background, (160, 0))
Sprite(background, (170, 0))
Sprite(background, (180, 0))
Sprite(background, (190, 0))
Sprite(background, (200, 0))
Sprite(background, (210, 0))
Sprite(background, (220, 0))
Sprite(background, (230, 0))
Sprite(background, (240, 0))
Sprite(background, (250, 0))
Sprite(background, (260, 0))
Sprite(background, (270, 0))
Sprite(background, (280, 0))
Sprite(background, (290, 0))
Sprite(background, (300, 0))
Sprite(background, (310, 0))
Sprite(background, (320, 0))
Sprite(background, (330, 0))
Sprite(background, (340, 0))
Sprite(background, (350, 0))
Sprite(background, (360, 0))
Sprite(background, (370, 0))
Sprite(background, (380, 0))
Sprite(background, (390, 0))
Sprite(background, (400, 0))
Sprite(background, (410, 0))
Sprite(background, (420, 0))
Sprite(background, (430, 0))
Sprite(background, (440, 0))
Sprite(background, (450, 0))
Sprite(background, (460, 0))
Sprite(background, (470, 0))
Sprite(background, (480, 0))
Sprite(background, (490, 0))
Sprite(background, (500, 0))

Sprite(background, (0, 10))
Sprite(background, (10, 10))
Sprite(background, (20, 10))
Sprite(background, (30, 10))
Sprite(background, (40, 10))
Sprite(background, (50, 10))
Sprite(background, (60, 10))
Sprite(background, (70, 10))
Sprite(background, (80, 10))
Sprite(background, (90, 10))
Sprite(background, (100, 10))
Sprite(background, (110, 10))
Sprite(background, (120, 10))
Sprite(background, (130, 10))
Sprite(background, (140, 10))
Sprite(background, (150, 10))
Sprite(background, (160, 10))
Sprite(background, (170, 10))
Sprite(background, (180, 10))
Sprite(background, (190, 10))
Sprite(background, (200, 10))
Sprite(background, (210, 10))
Sprite(background, (220, 10))
Sprite(background, (230, 10))
Sprite(background, (240, 10))
Sprite(background, (250, 10))
Sprite(background, (260, 10))
Sprite(background, (270, 10))
Sprite(background, (280, 10))
Sprite(background, (290, 10))
Sprite(background, (300, 10))
Sprite(background, (310, 10))
Sprite(background, (320, 10))
Sprite(background, (330, 10))
Sprite(background, (340, 10))
Sprite(background, (350, 10))
Sprite(background, (360, 10))
Sprite(background, (370, 10))
Sprite(background, (380, 10))
Sprite(background, (390, 10))
Sprite(background, (400, 10))
Sprite(background, (410, 10))
Sprite(background, (420, 10))
Sprite(background, (430, 10))
Sprite(background, (440, 10))
Sprite(background, (450, 10))
Sprite(background, (460, 10))
Sprite(background, (470, 10))
Sprite(background, (480, 10))
Sprite(background, (490, 10))
Sprite(background, (500, 10))

Sprite(background, (0, 20))
Sprite(background, (10, 20))
Sprite(background, (20, 20))
Sprite(background, (30, 20))
Sprite(background, (40, 20))
Sprite(background, (50, 20))
Sprite(background, (60, 20))
Sprite(background, (70, 20))
Sprite(background, (80, 20))
Sprite(background, (90, 20))
Sprite(background, (100, 20))
Sprite(background, (110, 20))
Sprite(background, (120, 20))
Sprite(background, (130, 20))
Sprite(background, (140, 20))
Sprite(background, (150, 20))
Sprite(background, (160, 20))
Sprite(background, (170, 20))
Sprite(background, (180, 20))
Sprite(background, (190, 20))
Sprite(background, (200, 20))
Sprite(background, (210, 20))
Sprite(background, (220, 20))
Sprite(background, (230, 20))
Sprite(background, (240, 20))
Sprite(background, (250, 20))
Sprite(background, (260, 20))
Sprite(background, (270, 20))
Sprite(background, (280, 20))
Sprite(background, (290, 20))
Sprite(background, (300, 20))
Sprite(background, (310, 20))
Sprite(background, (320, 20))
Sprite(background, (330, 20))
Sprite(background, (340, 20))
Sprite(background, (350, 20))
Sprite(background, (360, 20))
Sprite(background, (370, 20))
Sprite(background, (380, 20))
Sprite(background, (390, 20))
Sprite(background, (400, 20))
Sprite(background, (410, 20))
Sprite(background, (420, 20))
Sprite(background, (430, 20))
Sprite(background, (440, 20))
Sprite(background, (450, 20))
Sprite(background, (460, 20))
Sprite(background, (470, 20))
Sprite(background, (480, 20))
Sprite(background, (490, 20))
Sprite(background, (500, 20))
"""
# add your code here /\  /\  /\


myapp = App()
myapp.run()
