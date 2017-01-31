"""
picture.py
Author: <Jett>
Credit: <None>

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

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
brown = Color(0x633C1F, 1.0)
white = Color(0xFFFFFF, 1.0)

thinline = LineStyle(1, black)
House = RectangleAsset(700, 700, thinline, brown)
Swindow=CircleAsset(70, thinline, white)
window= RectangleAsset(100,100, thinline, white)
ellipse=EllipseAsset(30, 20, thinline, white)
polygon=PolygonAsset([(0,0), (700,0), (350,-300), (0,0)], thinline, black)
door= RectangleAsset(100,200, thinline, black)


Sprite(House,(500,400))
Sprite(polygon,(500,400))
Sprite(Swindow, (850,400))
Sprite(window, (550, 550))
Sprite(window, (1050, 550))
Sprite(door, (800, 680))
Sprite(ellipse,(850,705))


# add your code here /\  /\  /\


myapp = App()
myapp.run()
