"""
picture.py
Author: Funjando
Credit: tiggerntatie, Colorpicker.com

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
green=Color(0x9DE63E, 1.0)
blue=Color(0x0B1ABF, 1.0)
orange=Color(0xE35D09, 1.0)
purple=Color(0x8209AB, 1.0)
windowsheen=Color(0x74E3E3, 1.0)
hobbitgreen=Color(0x09B31D, 1.0)
leprechaungold=Color(0xD4BA15, 1.0)
black=Color(0x000000, 1.0)
yellow=Color(0xF5FC26, 1.0)
whitish=Color(0xC0EDEC, 1.0)

#colored lines
redline=LineStyle(4, red)
greenline=LineStyle(4, green)
blueline=LineStyle(1, blue)
orangeline=LineStyle(7, orange)
purpleline=LineStyle(4, purple)
blackline=LineStyle(1, black)
noline=LineStyle(0, black)

#shapes
grasshill=CircleAsset(550, greenline, green)
house=RectangleAsset(200, 390, blueline, blue)
windowa=EllipseAsset(25, 35, purpleline, windowsheen)
windowb=EllipseAsset(25, 35, redline, windowsheen)
windowg=EllipseAsset(25, 35, greenline, windowsheen)
door=PolygonAsset([(500,500),(550,500), (580, 550), (550, 600), (500, 600), (470, 550)], orangeline, hobbitgreen)
doorknob=CircleAsset(10, noline, leprechaungold)
roof=PolygonAsset([(87, 200), (189, 100), (283, 200)], orangeline, red )
sun=CircleAsset(200, noline, yellow)
moon=CircleAsset(100, noline, whitish)


#Sprites
Sprite(grasshill, (680, 1000))
Sprite(house, (585, 220))
Sprite(windowa, (632, 300))
Sprite(windowb, (730, 390))
Sprite(windowg, (632, 480))
Sprite(door, (200, 0))
Sprite(doorknob, (740, 550))
Sprite(roof, (500, 20))
Sprite(sun)
Sprite(moon, (1300, 0))





# add your code here /\  /\  /\


myapp = App()
myapp.run()
