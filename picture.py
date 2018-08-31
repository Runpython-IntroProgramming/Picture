"""
picture.py
Author: Rachel Matthew
Credit: none

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

palgreen=Color(0x64FE9E, 1.0)
dargreen=Color(0x133B11, 1.0)
palyellow=Color(0xE4FE9E, 1.0)
cloudy=Color(0xA1A1AA, 0.3)
nocol=Color(0x000000, 0.0)
brown=Color(0xA65711, 1.0)

noline=LineStyle(0, nocol)
darline=LineStyle(2, dargreen)
palline=LineStyle(1, palyellow)

Base=RectangleAsset(1500, 1000, noline, palyellow)
Hill1=EllipseAsset(300, 150, noline, dargreen)
Hill2=EllipseAsset(200, 75, noline, dargreen)
Hill3=EllipseAsset (550, 200, darline, palgreen)
Cloud_s=CircleAsset(57, noline, cloudy)
Cloud_l=CircleAsset(189, noline, cloudy)
House=PolygonAsset([(0,25), (15,10), (30,25), (26,25), (26,30), (40,30), (40, 55), (4,55), (4,25)], noline, brown)

Sprite(Base)
Sprite(Hill1, (80, 400))
Sprite(Hill1, (750, 480))
Sprite(Hill2, (-50, 400))
Sprite(Hill3, (-100,440))
Sprite(Cloud_l, (70,-175))
Sprite(Cloud_l, (900, -88))
Sprite(Cloud_l, (750, -190))
Sprite(Cloud_s, (35, 80))
Sprite(Cloud_s, (300, 50))
Sprite(Cloud_s, (359, 30))
Sprite(Cloud_s, (600, 120))
Sprite(Cloud_s, (807, 10))
Sprite(Cloud_s, (10, 101))
Sprite(Cloud_s, (150, 111))
Sprite(House, (670,430))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
