"""
picture.py
Author: Andy Kotz
Credit: Kezar helped me kn

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

red = Color(0xff0000, 1.0)
yellow = Color(0xdbd20f, 1.0)
gray = Color(0xa7a7a7, 1.0)
black = Color(0x000000, 1.0)

thinline = LineStyle(1, black)

rectanglesand = RectangleAsset (500, 500, thinline, yellow)
polygonhouse = PolygonAsset ([(450,450), (475,450), (475,425), (462,410), (450,425)], thinline, red)
ellipsecaveentr = EllipseAsset (50, 20, thinline, black)
circlecaverock = CircleAsset (50, thinline, gray)

Sprite (rectanglesand, (300, 450))
Sprite (polygonhouse)
Sprite (ellipsecaveentr)
Sprite (circlecaverock)
# add your code here /\  /\  /\


myapp = App()
myapp.run()
