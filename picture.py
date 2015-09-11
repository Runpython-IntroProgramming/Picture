"""
picture.py
Author: Dina
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
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/TUTORIAL:-Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/

red= Color(0xff0000, 1.0)
green = Color(0x00ff00, 0.5)
blue = Color(0x0000ff, 1.0)
skin = Color(0xffffee,1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
hair = Color(0x551000, 1.0)

thinline = LineStyle(1, black)
thickline = LineStyle(4, black)
noline = LineStyle(1, white)

rectangle1 = RectangleAsset(600, 400, thinline, yellow)
rectangle2 = RectangleAsset(100, 100, thinline, white)
ellipse1 = EllipseAsset(200, 250, thinline, skin)
triangle = PolygonAsset([(450, 500), (550, 550), (550, 400), (450,500)], thinline, green)
circle = CircleAsset(50, noline, hair)

Sprite(ellipse, (550,300))
Sprite(circle, (550,100))
Sprite(circle, (475,100))
Sprite(circle, (625,125))
Sprite(circle, (550,100))
Sprite(circle, (550,100))
Sprite(circle, (550,100))
Sprite(circle, (550,100))
Sprite(circle, (550,100))
#Sprite(rectangle2, (250, 250))
Sprite(ellipse,(500, 500))
#Sprite(triangle)

# add your code here /\  /\  /\


myapp = App()
myapp.run()