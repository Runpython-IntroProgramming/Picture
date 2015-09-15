"""
picture.py
Author: Roger Danilek
Credit: 

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

thinline = LineStyle(1, black)
noline = LineStyle(1, red)
rectangle = RectangleAsset(500, 500, thinline, blue)
circle = CircleAsset(200, thinline, red)
eyes = EllipseAsset(50, 30, thinline, Color(0x073d91, 1.0))
pupils = EllipseAsset(20, 30, thinline, Color(0xffffff, .8))
mouth = EllipseAsset(100, 50, thinline, Color(0x008000, 1.0))
mouth2 = EllipseAsset(100, 40, noline, red)
triangle = PolygonAsset([(270,270), (330,270), (300,250), (270,270)], thinline, black)
teeth = PolygonAsset([(260,345), (280,345), (270,360), (260,345)], thinline, Color(0xffffff, 1.0))
teeth2 = PolygonAsset([(340,345), (320,345), (330,360), (340,345)], thinline, Color(0xffffff, 1.0))
Sprite(rectangle, (50,30))
Sprite(circle, (300, 250))
Sprite(eyes, (240, 200))
Sprite(eyes, (370, 200))
Sprite(mouth, (300, 320))
Sprite(mouth2, (300, 305))
Sprite(triangle, (0, 0))
Sprite(pupils, (240, 200))
Sprite(pupils, (370, 200))
Sprite(teeth, (0,0))
Sprite(teeth2, (0,0))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
