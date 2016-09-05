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

black = Color(0x000000, 1.0)
flute = Color(0xffe6b3, 0.85)
background = Color(0xb3d9ff, 0.85)
line = LineStyle(1, black)

background = RectangleAsset(888, 500, line, background)
flutebody = RectangleAsset(350, 25, line, flute)
fluteheadjoint = RectangleAsset(150, 25, line, flute)
fluteembrochure = EllipseAsset(9, 5, line, black)
flutehole1 = CircleAsset(5, line, black)
flutehole2 = CircleAsset(5, line, black)
flutehole3 = CircleAsset(5, line, black)
flutehole4 = CircleAsset(5, line, black)
flutehole5 = CircleAsset(5, line, black)
flutehole6 = CircleAsset(5, line, black)
notebody = PolygonAsset([(800, 100), (840,100), (840, 150), (838, 150), (838, 110), (802, 110), (802, 150), (800, 150)], line, black)
notehead1 = EllipseAsset(8, 5, line, black)
notehead2 = EllipseAsset(8, 5, line, black)



Sprite(background, (225, 50))
Sprite(flutebody, (520, 375))
Sprite(fluteheadjoint, (370, 375))
Sprite(fluteembrochure, (420,386))
Sprite(flutehole1, (625, 386))
Sprite(flutehole2, (665, 386))
Sprite(flutehole3, (705, 386))
Sprite(flutehole4, (745, 386))
Sprite(flutehole5, (785, 386))
Sprite(flutehole6, (825, 386))
Sprite(notebody, (100,120))
Sprite(notehead1, (894,268))
Sprite(notehead2, (932, 268))

myapp = App()
myapp.run()
