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
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x00BFFF, 1.0)
black = Color(0x000000, 1.0)
yellow = Color(0xFFFF00, 1.0)
green = Color(0x09FF00, 1.0)
white = Color(0xFFFFFF, 1.0)
grey = Color(0x666666, 1.0)
darkgrey =Color(0x3D3D3D, 1.0)
thinlineblack = LineStyle(1, black)
thinlinegreen = LineStyle(1, green)
thinlineblue = LineStyle(1, blue)
thinlineyellow = LineStyle(1, yellow)
thinlinegreen = LineStyle(1, green)
thinlinewhite = LineStyle(1, white)
thinlinegrey = LineStyle(1, grey)
thinlinedarkgrey = LineStyle(1, darkgrey)
bluesky = RectangleAsset(1280, 720, thinlinegreen, blue)
Sprite(bluesky)
mountain =PolygonAsset([(0,720), (200,720,), (100,520)], thinlinegrey, grey)
mountaincap =PolygonAsset([(75,570), (125,570,), (100,520)], thinlinewhite, white)
Sprite(mountain)
Sprite(mountaincap)
mountain1 =PolygonAsset([(190,720), (390,720,), (290,420)], thinlinedarkgrey, darkgrey)
mountaincap1 =PolygonAsset([(265,495), (315,495,), (290,420)], thinlinewhite, white)
Sprite(mountain1)
Sprite(mountaincap1)
mountain2 =PolygonAsset([(300,720), (500,720,), (400,520)], thinlinegrey, grey)
mountaincap2 =PolygonAsset([(375,570), (425,570,), (400,520)], thinlinewhite, white)
Sprite(mountain2)
Sprite(mountaincap2)
# add your code here /\  /\  /\


myapp = App()
myapp.run()
