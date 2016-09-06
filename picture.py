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
black=Color(0x000000, 1.0)
buildingcolor=Color(0x996633, 1.0)
window=Color(0xCCFFFF, 1.0)
roofcolor=Color(0x660000, 1.0)
edge=LineStyle(1,black)
building=RectangleAsset(300,200, edge, buildingcolor)
Sprite(building, (0,200))
roof=PolygonAsset([(0,200), (75,0), (300,200), (0,200)], edge, roofcolor)
Sprite(roof)


# add your code here /\  /\  /\


myapp = App()
myapp.run()
