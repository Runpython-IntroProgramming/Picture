"""
picture.py
Author: Kezar
Credit: Kotz, xnimblenavigatorx

Assignment:picture

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
yellow = Color(0xfff400, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
# A graphics asset that represents a rectangle
rectangle = RectangleAsset(150, 150, thinline, yellow)
rectangle1 = RectangleAsset(25, 25 ,thinline, black) 
rectangle2 = RectangleAsset(100,1 ,thinline, black)
ellipse = EllipseAsset(12,30, thinline, black)
ellipse2 = EllipseAsset(50, 7, thinline, black)


# Now display a rectangle
Sprite(rectangle, (800,400))
Sprite(rectangle1, (820, 425))
Sprite(rectangle1, (900, 425))
Sprite(rectangle2, (820, 435))
Sprite(ellipse, (873, 477))
Sprite(ellipse2, (873, 525))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
