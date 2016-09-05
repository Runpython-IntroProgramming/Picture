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
"""
fluteheadjoint
fluteembrochure
flutehole1
flutehole1
flutehole1
flutehole1
flutehole1
flutehole1
notebody
notehead1
notehead2
"""


Sprite(background, (225, 50))
Sprite(flutebody, (520, 375))
Sprite(fluteheadjoint

myapp = App()
myapp.run()
