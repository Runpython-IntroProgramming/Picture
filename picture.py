"""
picture.py
Author: emBrileg08
Credit: NA

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

black= Color(0x000000, 1.0)
peach= Color(0xffe0bd, 1.0)
thinline = LineStyle(1, black)
face=EllipseAsset(30, 40, thinline, peach)
Sprite(face)



# add your code here /\  /\  /\


myapp = App()
myapp.run()
