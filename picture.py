"""
picture.py
Author: Jack Meehan
Credit: https://www.webucator.com/blog/2015/03/python-color-constants-module/
I used this website to find additional colors.

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
treegreen = Color(0x458B00, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0f0fff, 1.0)
black = Color(0x000000, 1.0)
slategrey = Color(0x8B8878, 1.0)
white = Color(0xffffff, 1.0)
brown = Color(0xCD661D, 1.0)
khaki = Color(0xF0E68C, 1.0)
thinline = LineStyle(2, black)

rectangle = RectangleAsset(200, 100, thinline, khaki)
Sprite(rectangle, (200, 200))

roof = PolygonAsset([(305, 100), (210, 150), (407, 150)], thinline, slategrey)
Sprite(roof, (200, 150))

door = RectangleAsset(30, 60, thinline, blue)
Sprite(door, (255, 240))

doorwindow = RectangleAsset(24, 22, thinline, slategrey)
Sprite(doorwindow, (258, 244))

window = CircleAsset(22, thinline, slategrey)
Sprite(window, (318, 230))

path = PolygonAsset([(230, 300), (160, 360), (150, 360), (200, 300)], thinline, brown)
Sprite(path, (204, 300))

tree1 = PolygonAsset([(350, 55), (310, 150), (400, 150)], thinline, treegreen)
Sprite(tree1, (440, 234))

stump1 = RectangleAsset(18, 22, thinline, brown)
Sprite(stump1, (473, 330))

tree2 = PolygonAsset([(350, 55), (310, 150), (400, 150)], thinline, treegreen)
Sprite(tree2, (390, 252))

stump2 = RectangleAsset(18, 22, thinline, brown)
Sprite(stump2, (423, 350))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
