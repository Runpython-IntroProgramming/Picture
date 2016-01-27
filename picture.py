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

# https://www.mathsisfun.com/numbers/hexadecimal-color-names.html

Size = 15
SkyWidth = Size*90
SkyHeight = Size*40
GroundHeight = SkyHeight/10
MountWidth = Size*20
MountHeight = MountWidth*1.6
OffSide = SkyWidth/20

Yellow = Color(0xFFFF00, 1.0)
Black = Color(0x000000, 1.0)
SkyBlue = Color(0x87CEFA, 1.0)
GroundCol = Color(0x556B2F, 1.0)
MountCol = Color(0xD2B48C, 1.0)

ThinLine = LineStyle(1, Black)

Back = RectangleAsset(SkyWidth, SkyHeight, ThinLine, SkyBlue)
Ground = RectangleAsset(SkyWidth, GroundHeight, ThinLine, GroundCol)
Sun = CircleAsset(SkyWidth/15, ThinLine, Yellow)
Mount = PolygonAsset([(SkyWidth-(MountWidth/2)-OffSide, SkyHeight-MountHeight), (SkyWidth-MountWidth-OffSide, SkyHeight), (SkyWidth-OffSide, SkyHeight)], ThinLine, MountCol)
# Snow = PolygonAsset([(SkyWidth-(MountWidth/2)-OffSide, SkyHeight-MountHeight), (

Sprite(Back)
Sprite(Ground, (0, SkyHeight))
Sprite(Sun, (SkyWidth-OffSide, SkyHeight-MountHeight))
Sprite(Mount)

# add your code here /\  /\  /\


myapp = App()
myapp.run()
