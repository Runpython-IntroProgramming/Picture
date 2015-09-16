"""
picture.py
Author: Sam Supattapone
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
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
grey = Color(0x000000, 0.8)
lightgrey = Color(0x000000, 0.2)
white = Color(0xffffff, 1.0)
thinline = LineStyle(1, black)
noline = LineStyle(0, black)
rectangle = RectangleAsset(330, 650, thinline, black)
Sprite(rectangle,(500,50))
rectangle = RectangleAsset(55, 6, thinline, white)
Sprite(rectangle,(640,75))
rectangle = RectangleAsset(55, 6, thinline, grey)
Sprite(rectangle,(640,75))
rectangle1 = RectangleAsset(310, 530, thinline, white)
Sprite(rectangle1,(510,110))
circle = CircleAsset(25, thinline, white)
Sprite(circle,(665,670))
circle = CircleAsset(25, thinline, grey)
Sprite(circle,(665,670))
ellipse = EllipseAsset(25, 40, noline, green)
Sprite(ellipse,(650,370))
rectangle = RectangleAsset(300, 75, noline, lightgrey)
Sprite(rectangle,(515,560))
polygon = PolygonAsset([(0,0),(0,60),(60,70),(80,0)], noline, red)
Sprite(polygon,(550,200))
polygon = PolygonAsset([(0,0),(0,40),(100,60),(60,0)], noline, blue)
Sprite(polygon,(700,450))

myapp = App()
myapp.run()

myapp = App()
myapp.run()