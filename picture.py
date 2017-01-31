"""
picture.py
Author: <your name here>
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
black = Color(0x000000, 1.0)
red = Color(0xff0000, 1.0)
white = Color(0xff0000, 1.0)
yellow = Color(0xffff00, 1.0)

thinline = LineStyle(1, black)

rectangle1 = RectangleAsset(300, 250, thinline, red)
rectangle2 = RectangleAsset(50,100, thinline, black)
poly = PolygonAsset([(400,200), (550,50), (700, 200)], thinline, black)

Sprite(rectangle1, (400,200))
Sprite(rectangle2, (525,350))
Sprite(poly)
# add your code here /\  /\  /\


myapp = App()
myapp.run()
