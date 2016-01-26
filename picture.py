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

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
thickline = LineStyle (2, green)

# A graphics asset that represents a rectangle
rectangle = RectangleAsset(500, 400,thinline, blue)
circle = CircleAsset(4, thinline, red)
ellipse = EllipseAsset(5, 4, thinline, green)
polygon = PolygonAsset([(0,0), (-100,-100), (500,100), (0,0)], thickline, black)
window1 = RectangleAsset(50, 50, thinline, black)



# Now display a rectangle
Sprite(rectangle, (200, 150))
Sprite(circle, (50, 30))
Sprite(ellipse, (80, 210))
Sprite(polygon, (200, 150))
Sprite(window1, (285, 200))

myapp = App()
myapp.run()


# add your code here /\  /\  /\


myapp = App()
myapp.run()
