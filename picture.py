"""
picture.py
Author: Meg
Credit: Picture tutorial, http://brythonserver.github.io/ggame/, Johari

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
#from tutorial
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
yellow = Color(0xffff00, 1.0)

line = LineStyle(1, black)

trunk = RectangleAsset(10, 40, line, black)
orn1 = CircleAsset(5, line, red)
orn2 = CircleAsset(5, line, blue)
base = EllipseAsset(40, 10, line, black)
third = PolygonAsset([(25,0), (0,90), (50,90), (25,0)], line, green)
second = PolygonAsset([(25,0), (0,70), (50,70), (25,0)], line, green)
first = PolygonAsset([(25,0), (0,50), (50,50), (25,0)], line, green)
star = PolygonAsset([(25,0), (15,25), (40,10), (10,10), (35,25), (25,0)], line, yellow)
pres = RectangleAsset(30, 30, line, red)
rib = RectangleAsset(5

Sprite(trunk, (220, 130))
Sprite(third, (200, 50))
Sprite(second, (200, 50))
Sprite(first, (200, 50))
Sprite(orn1, (215, 75))
Sprite(orn2, (220, 100))
Sprite(orn2, (225, 85))
Sprite(orn1, (225, 125))
Sprite(base, (185, 160))
Sprite(star, (210, 40))
Sprite(pres, (235, 140))


# add your code here /\  /\  /\


myapp = App()
myapp.run()
