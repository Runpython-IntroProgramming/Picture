"""
picture.py
Author: James Eiler
Credit: Instruction and Tutorials From Mr Dennison

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
app=App()
app.run()
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
linea = LineStyle(1, blue)
lineb = LineStyle(1, green)
linec = LineStyle(1, red)
rectangle1 = RectangleAsset(20, 80, linea, red)
circle1 = CircleAsset(20, lineb, green)
polygon1 = PolygonAsset([(10,20),(5,10),(3,2)], linec, blue)
Ellipse1 = EllipseAsset(10, 20, linea, red)
circle2 = CircleAsset(20, linec, blue)
Sprite(rectangle1, (250, 10))
Sprite(polygon1, (50, 10))
Sprite(Ellipse1, (50, 10))
Sprite(circle1, (275, 375))
Sprite(circle1, (300, 400))
Sprite(rectangle1, (500, 10))
Sprite(polygon1, (2, 3))
Sprite(Ellipse1, (10, 13))
Sprite(rectangle1, (250, 355))
Sprite(circle2, (300, 350))
Sprite(circle2, (325, 375))


# add your code here /\  /\  /\


myapp = App()
myapp.run()
