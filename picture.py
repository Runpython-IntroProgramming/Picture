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


# add your code here /\  /\  /\


myapp = App()
myapp.run()
from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
orange = Color(0xffa500, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
# A graphics asset that represents a rectangle
rectangle = RectangleAsset(300, 200, thinline, green)

# Now display a rectangle
Sprite(rectangle, (100, 150))

poly=PolygonAsset([(100,150), (400,150), (245,50), (100,150)], thinline, red)
rectangle = RectangleAsset(50, 100, thinline, blue)
Sprite(rectangle, (300, 250))
Sprite(poly)
Circle= CircleAsset(5, thinline, green)
Sprite(Circle, (340, 310))
Ellipse= EllipseAsset(20, 20, thinline, black)
Sprite(Ellipse, (170, 200))
Sprite(Ellipse, (325, 200))
Circle2= CircleAsset(50, thinline, orange)
Sprite(Circle2, (550, 100))
rectangle2 = RectangleAsset(100, 50, thinline, blue)
Sprite(rectangle2, (600, 300))
rectangle3 = RectangleAsset(150, 35, thinline, blue)
Sprite(rectangle3, (575, 330))
Circle3= CircleAsset(13, thinline, black)
Sprite(Circle3, (600, 370))
Sprite(Circle3, (700, 370))
myapp = App()
myapp.run()
