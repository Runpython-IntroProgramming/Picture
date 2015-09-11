"""
picture.py
Author: Jeff
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
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/TUTORIAL:-Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

red = Color(0xff0000, 1.0)
redT = Color(0xff0000, 0.5)
green = Color(0x00ff00, 1.0)
greenT = Color(0x00ff00, 0.45)
blue = Color(0x0000ff, 1.0)
blueT = Color(0x0000ff, 0.4)
black = Color(0x000000, 1.0)

thinline = LineStyle(0, black)

shape1 = CircleAsset(100, thinline, redT)
shape2 = CircleAsset(100, thinline, greenT)
shape3 = CircleAsset(100, thinline, blueT)
oval = EllipseAsset(50, 80, thinline, greenT)
rectangle = RectangleAsset(120, 120, thinline, redT)
hexagon = PolygonAsset([(50,0), (150,0), (200,85), (150,170), (50,170), (0,85)], thinline, blueT)
triangle = PolygonAsset([(0,85), (100,85), (50,0)], thinline, greenT)
shape4 = CircleAsset(80, thinline, redT)
shape5 = RectangleAsset(50, 80, thinline, blueT)

Sprite(shape1, (650,300))
Sprite(shape2, (575,430))
Sprite(shape3, (725,430))
Sprite(oval, (725,250))
Sprite(rectangle, (575,500))
Sprite(hexagon, (400,300))
Sprite(triangle, (725,500))
Sprite(triangle, (300, 300))
Sprite(shape4, (700, 450))
Sprite(shape5, (600, 750))


# add your code here /\  /\  /\


myapp = App()
myapp.run()
