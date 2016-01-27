"""
picture.py
Author: Glen Passow
Credit: Mr. Dennison

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

#colors
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
#yellow = Color(0Xffff00, 1.0)

#line style
thinline = LineStyle(1, black)



rectangle = RectangleAsset(1000, 600, thinline, blue)
circle = CircleAsset(50, thinline, red)
ellipse = EllipseAsset(60, 100, thinline, red)
triangle = PolygonAsset([(50,50),(60,50),(80,80)], thinline, green)

#display the shapes
Sprite(rectangle, (200, 50))
Sprite(circle, (900, 150))
Sprite(ellipse, (400, 400))
Sprite(triangle, (600,600))


# add your code here /\  /\  /\


myapp = App()
myapp.run()
