"""
picture.py
Author: Andrew Chen
Credit: https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics

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
red = Color(0xff0000, 1)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, .3)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
line1 = LineStyle(1, black)
line0 = LineStyle(0, black)

sky = RectangleAsset(1500, 1000, line0, blue)
Sprite(sky)

grass = RectangleAsset(1500, 500, line1, green)
Sprite(grass, (0,300))

house = RectangleAsset(200, 200, line1, red)
Sprite(house, (400,200))

windowsky = RectangleAsset(80, 80, line1, white)
Sprite(windowsky, (420,250))

window = RectangleAsset(80, 80, line1, blue)
Sprite(window, (420,250))

roof = PolygonAsset([(0,0), (100,-150), (200,0)], line1, green)
Sprite(roof, (400,50))

circlesky = CircleAsset(20, line1, white)
Sprite(circlesky, (480,150))

circle = CircleAsset(20, line1, blue)
Sprite(circle, (480,150))

trunk = RectangleAsset(30, 80, line1, red)
Sprite(trunk, (835,350))

tree = EllipseAsset(50, 100, line1, green)
Sprite(tree, (800,200))

trunk2 = RectangleAsset(30, 80, line1, red)
Sprite(trunk2, (135,350))

tree2 = EllipseAsset(50, 100, line1, green)
Sprite(tree2, (100,200))

# add your code here /\  /\  /\

myapp = App()
myapp.run()


