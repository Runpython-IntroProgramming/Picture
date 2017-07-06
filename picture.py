"""
picture.py
Author: smeds1
Credit: None

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

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
white = Color(0xffffff, 1.0)
black = Color(0x000000, 1.0)

blackLine = LineStyle(1,black)

outline = RectangleAsset(600,400,blackLine,white)
circle = CircleAsset(50,blackLine,red)
ellipse = EllipseAsset(20,40,blackLine,green)
polygon = PolygonAsset([(20,30),(150,60),(190,200)],blackLine,blue)

Sprite(outline)
Sprite(circle,(100,200))
Sprite(ellipse,(300,300))
Sprite(polygon)
Sprite(circle,(100,400))
Sprite(ellipse,(400,200))
Sprite(polygon,(100,20))
Sprite(circle,(600,200))
Sprite(ellipse,(700,400))
Sprite(polygon,(500,500))


myapp = App()
myapp.run()
