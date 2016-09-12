"""
picture.py
Author: Wilson
Credit: None

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
windowcolor=Color(0xCCFFFF, 1.0)
roofcolor=Color(0x660000, 1.0)
doorcolor=Color(0x000066,1.0)
knobcolor=Color(0xFFCC00, 1.0)
bushcolor=Color(0x006600, 1.0)
edge=LineStyle(1,black)
building=RectangleAsset(300,200, edge, buildingcolor)
window=RectangleAsset(30,30,edge,windowcolor)
roof=PolygonAsset([(0,200), (155,75), (300,200), (0,200)], edge, roofcolor)
door=RectangleAsset(30,60,edge,doorcolor)
knob=CircleAsset(2.5,edge,knobcolor)
circlewindow=CircleAsset(15,edge,windowcolor)
bush=EllipseAsset(30,15,edge,bushcolor)
Sprite(building, (0,200))
Sprite(window, (50,330))
Sprite(window, (220,330))
Sprite(window, (50,250))
Sprite(window, (220,250))
Sprite(roof)
Sprite(door, (135,340))
Sprite(knob,(142,370))
Sprite(circlewindow, (150,240))
Sprite(bush, (200,385))
Sprite(bush, (100,385))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
