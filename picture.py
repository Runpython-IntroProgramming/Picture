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



rectangle = RectangleAsset(500, 600, thinline, blue)
circle = CircleAsset(50, thinline, red)
ellipse = EllipseAsset(60, 100, thinline, red)
triangle = PolygonAsset([(50,50),(100,200),(0,80)], thinline, green)
rectangle2 = RectangleAsset(100, 100, thinline, blue)
circle2 = CircleAsset(250, thinline, black)
rectangle3 = RectangleAsset(50, 600, thinline, red)
ellipse2 = EllipseAsset(300, 100, thinline, green)
triangle2 = PolygonAsset([(50,50),(100,200),(500,80)], thinline, red)
triangle3 = PolygonAsset([(89,500),(300,200),(0,80)], thinline, blue)
triangle4 = PolygonAsset([(300,100),(100,260),(0,80)], thinline, green)

#display the shapes
Sprite(rectangle, (600, 50))
Sprite(circle2, (900, 150))
Sprite(circle, (900, 150))
Sprite(ellipse, (400, 400))
Sprite(triangle, (500,600))
Sprite(rectangle2, (200, 50))
Sprite(rectangle3, (500, 50))
Sprite(ellipse2, (400, 0))
Sprite(triangle2, (300,400))
Sprite(triangle3, (100,450))
Sprite(triangle4, (345,90))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
