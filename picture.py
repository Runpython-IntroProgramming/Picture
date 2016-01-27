"""
picture.py
Author: Eli Woloshin
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
from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
turqoise = Color(0x00e5ee, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
thickline = LineStyle (2, green)

# A graphics asset that represents a rectangle
rectangle = RectangleAsset(500, 400,thinline, blue)
circle = CircleAsset(4, thinline, red)
ellipse = EllipseAsset(40, 70, thinline, green)
polygon = PolygonAsset([(500,0), (250,-150), (0,0)], thickline, black)
window1 = RectangleAsset(100, 100, thinline, black)
window2 = RectangleAsset(100,100, thinline, red)
door = RectangleAsset(100, 200, thinline, turqoise)
pane1 = RectangleAsset(10, 100, thinline, turqoise)
pane2 = RectangleAsset(100, 10, thinline, turqoise)
window3 = CircleAsset(40, thinline, black)


# Now display a rectangle
Sprite(rectangle, (200, 150))
Sprite(polygon, (200, 150))
Sprite(window1, (285, 200))
Sprite(window2, (485, 200))
Sprite(door, (485, 350))
Sprite(circle, (565, 450))
Sprite(ellipse, (325, 440))
Sprite(pane1, (330, 200))
Sprite(pane2, (285, 245))
Sprite(window3, (535, 250))



myapp = App()
myapp.run()


# add your code here /\  /\  /\


myapp = App()
myapp.run()
