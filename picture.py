"""
picture.py
Author: Rachel Matthew
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

palgreen=Color(0x64FE9E, 1.0)
dargreen=Color(0x133B11, 1.0)
palyellow=Color(0xE4FE9E, 1.0)
cloudy=Color(0xA1A1AA, 0.3)
nocol=Color(0x000000, 0.0)

noline=LineStyle(0, nocol)
darline=LineStyle(2, dargreen)
palline=LineStyle(1, palyellow)

# add your code here /\  /\  /\


myapp = App()
myapp.run()
