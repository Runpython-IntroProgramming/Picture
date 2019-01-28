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
wah = Color(0xedcc9b, 1.0)
purple= Color(0xce27d3, 1.0)
white = Color(0xffffff, 1.0)
black = Color(0x000000, 1.0)
blue = Color(0x00ffff, 1.0)
thinline = LineStyle(1, black)

eyeshadow = EllipseAsset(25, 15, thinline, blue)
eye = EllipseAsset(25, 15, thinline, white)
face = EllipseAsset(100, 100, thinline, wah)
rectangle = RectangleAsset(50, 20, thinline, purple)
hat = EllipseAsset(100, 70, thinline, purple)
triangle = PolygonAsset([(100,100), (50, 60), (200,70)], thinline, wah)

Sprite(face, (289, 120))
Sprite(eyeshadow, (305, 230))
Sprite(eye, (305, 225))
Sprite(eye, (420, 225))
Sprite(hat, (290, 100))
Sprite(rectangle, (200, 60))



# add your code here /\  /\  /\


myapp = App()
myapp.run()
