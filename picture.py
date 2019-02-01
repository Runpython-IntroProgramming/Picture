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

from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
gold = Color(0xffff00, 1.0)
white = Color(0xfffafa, 1.0)
brown = Color(0x8b4513, 1.0)
# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
# A graphics asset that represents a rectangle

# Now display a rectangle


myapp = App()
myapp.run()

polygon = PolygonAsset([(0,0), (-5,10,), (5,10), (0,0)], thinline, black)
polygon2 = PolygonAsset([(0,0), (1,60), (-1, 60), (0,0)], thinline, green)
rectangle = RectangleAsset(10, 150, thinline, brown)
circle = CircleAsset(15, thinline, gold)
circle2 = CircleAsset(25, thinline, red)
circle3 = CircleAsset(35, thinline, blue)
circle4 = CircleAsset(45, thinline, black)
circle5 = CircleAsset(55, thinline, white)
circle6 = CircleAsset(3, thinline, black)
ellipse = EllipseAsset(5, 30, thinline, green)

Sprite(polygon, (459.5, 300))
Sprite(ellipse, (453, 403))
Sprite(ellipse, (467, 403))
Sprite(rectangle, (460, 310))
Sprite(circle5, (410, 160))
Sprite(circle4, (420, 170))
Sprite(circle3, (430, 180))
Sprite(circle2, (440, 190))
Sprite(circle, (450, 200))
Sprite(circle6, (462, 212))
Sprite(polygon2, (463.5, 400))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
