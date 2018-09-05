"""
picture.py
Author: Jackson Tolliday
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
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
clear = Color(0xffffff, 0.0)
brown = Color(0x6E2c00, 1.0)
grey = Color(0x707b7c, 1.0)

thinline = LineStyle(1, black)
thickline = LineStyle(2, black)
noline = LineStyle(1, clear)

base = RectangleAsset(40, 50, thinline, brown)
leaf = PolygonAsset([(0,0), (100,-75), (200,0), (0,0)], thickline, green)
leaf2 = PolygonAsset([(0,0), (150,-100), (300,0), (0,0)], thickline, green)
smalleaf = PolygonAsset([(0,0), (50,-50), (100,0), (0,0)], thickline, green)
apple = CircleAsset(10, noline, red)
appleaf = EllipseAsset(6,3, thinline, green)
ground = EllipseAsset(400,100, noline, brown)
grass = EllipseAsset(300,75, noline, green)
rock = EllipseAsset(30,20, thinline, grey)
rockblock = RectangleAsset(65, 45, noline, green)

Sprite(ground,(0,300))
Sprite(grass, (0,300))
Sprite(rock, (275,315))
Sprite(rockblock, (274, 340))
Sprite(base, (175,310))
Sprite(leaf2, (43,210))
Sprite(leaf, (93,170))
Sprite(smalleaf, (143,140))
Sprite(apple, (143,210))
Sprite(appleaf, (140,210))

Sprite(apple, (176,160))
Sprite(appleaf, (173,160))

Sprite(apple, (203,260))
Sprite(appleaf, (200,260))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
