"""
picture.py
Author: Robbie
Credit: RGB Colors in Python

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
yellow= Color(0xffff00, 1.0)
brown= Color(0x8b4513, 1.0)
cyan = Color(0x40e0d0, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
thickline = LineStyle(1, brown)
rectangle = RectangleAsset (100, 100, thinline, blue)
triangle = PolygonAsset ([(550, 300), (500, 400), (550, 400), (600, 400)], thinline, red)
sun = EllipseAsset (100, 100, thinline, yellow)
tree = CircleAsset (50, thinline, green)
trunk = RectangleAsset (30, 50, thinline, brown)
chimney = RectangleAsset (30, 50, thickline, brown)
chimneypart = PolygonAsset ([(575, 360), (605, 360), (605, 380), (603, 405)], thickline, brown)
window = RectangleAsset (25, 25, thinline, cyan)
door = RectangleAsset (25, 50, thinline, brown)
# add your code here /\  /\  /\
Sprite (rectangle, (500, 400))
Sprite (triangle)
Sprite (sun)
Sprite (tree, (300, 400))
Sprite (trunk, (285, 450))
Sprite (chimney, (575, 310))
Sprite (chimneypart)
Sprite (window, (560, 425))
Sprite (window, (510, 425))
Sprite (door, (535, 450))
# add your code here /\  /\  /\


myapp = App()
myapp.run()
