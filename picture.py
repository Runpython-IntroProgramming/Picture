"""
picture.py
Author: David Wilson
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

MountWidth = 1

Black = Color(0x000000, 1.0)
MountCol = Color(0xFAEBD7, 1.0)

ThinLine = LineStyle(1, Black)

Mount = PolygonAsset([((MountWidth/2), 0), (0, (MountWidth*(9/4))), (MountWidth, (MountWidth*(9/4)))], ThinLine, MountCol)

Sprite(Mount)

# add your code here /\  /\  /\


myapp = App()
myapp.run()
