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

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
orange = Color(0xff7400, 1.0)


thickline = LineStyle(5 , red)
circle = CircleAsset(10, thickline, red)
poly = PolygonAsset([(20,20), (30,40), (50,80), (20,20)], thickline, red)
portal1 = EllipseAsset(40, 10, thickline, blue)
rectum = RectangleAsset(40, 60, thickline, green)
portal2 = EllipseAsset(40, 10, thickline, orange)

Sprite(circle, (20, 500)) 
Sprite(poly, (60, 200))
Sprite(portal1, (80, 500))
Sprite(portal2, (80, 150))
Sprite(rectum, (123, 68))


# add your code here /\  /\  /\


myapp = App()
myapp.run()

