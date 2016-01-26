"""
picture.py
Author: Funjando
Credit: tiggerntatie

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

#Colors
red=Color(0x910101, 1.0)
green=Color(0x79E310, 1.0)
blue=Color(0x0B1ABF, 1.0)
orange=Color(0xE35D09, 1.0)
purple=Color(0x8209AB, 1.0)
windowsheen=Color(0x74E3E3, 1.0)

#colored lines
redline=LineStyle(1, red)
greenline=LineStyle(1, green)
blueline=LineStyle(1, blue)
orangeline=LineStyle(1, orange)
purpleline=LineStyle(1, purple)

#shapes
grasshill=CircleAsset(550, greenline, green)
house=RectangleAsset(200, 390, blueline, blue)
windowa=EllipseAsset(25, 35, purpleline, windowsheen)
windowb=EllipseAsset(25, 35, redline, windowsheen)
windowg=EllipseAsset(25, 35, greenline, windowsheen)
door=PolygonAsset([(500,500),(600,500), (650, 1000), (450, 1200), (350, 800)], orangeline, green)
#pos 1, 2

#Sprites
Sprite(grasshill, (680, 1000))
Sprite(house, (585, 220))
Sprite(windowa, (632, 300))
Sprite(windowb, (730, 390))
Sprite(windowg, (632, 480))
Sprite(door, (100, 0))




# add your code here /\  /\  /\


myapp = App()
myapp.run()
