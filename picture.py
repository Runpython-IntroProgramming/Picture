"""
picture.py
Author: emBrileg08
Credit: www.colorhexa.com for the color hexadecimals

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects. Done
2. Ten different Sprite objects. 3/10
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects. Done
5. One (or more) EllipseAsset objects. Done
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
brown= Color(0x654321, 1.0)
thinline = LineStyle(1, black)

face=EllipseAsset(135, 160, thinline, peach)
pupil=CircleAsset(10, thinline, brown)
something=PolygonAsset(10,thinline,brown)

Sprite(face, (160,160))
Sprite(pupil, (220,260))
Sprite(pupil, (350, 260))
Sprite(something (10,10))


# add your code here /\  /\  /\


myapp = App()
myapp.run()
