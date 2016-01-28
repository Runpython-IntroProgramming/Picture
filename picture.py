"""
picture.py
Author: Adam Glueck
Credit: Asked Avery for some help on CircleAsset Notation and looked at http://brythonserver.github.io/ggame/ for notation help

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
thinlinered = LineStyle(1, red)
thinlineblack = LineStyle(1, black)
thinlinegreen = LineStyle(1, green)
thinlineblue = LineStyle(1, blue)
thinlineyellow = LineStyle(1, yellow)
thinlinegreen = LineStyle(1, green)
thinlinewhite = LineStyle(1, white)
thinlinegrey = LineStyle(1, grey)
thinlinedarkgrey = LineStyle(1, darkgrey)
bluesky = RectangleAsset(1280, 720, thinlineblue, blue)
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
mountain3 =PolygonAsset([(490,720), (690,720,), (590,420)], thinlinedarkgrey, darkgrey)
mountaincap3 =PolygonAsset([(565,495), (615,495,), (590,420)], thinlinewhite, white)
Sprite(mountain3)
Sprite(mountaincap3)
mountain4 =PolygonAsset([(650,720), (850,720,), (750,520)], thinlinegrey, grey)
mountaincap4 =PolygonAsset([(725,570), (775,570,), (750,520)], thinlinewhite, white)
Sprite(mountain4)
Sprite(mountaincap4)
mountain5 =PolygonAsset([(790,720), (990,720,), (890,420)], thinlinedarkgrey, darkgrey)
mountaincap5 =PolygonAsset([(865,495), (915,495,), (890,420)], thinlinewhite, white)
Sprite(mountain5)
Sprite(mountaincap5)
mountain6 =PolygonAsset([(900,720), (1280,720,), (1150,360)], thinlinegrey, grey)
mountaincap6 =PolygonAsset([(1176,430), (1100,430,), (1150,360)], thinlinewhite, white)
Sprite(mountain6)
Sprite(mountaincap6)
whiteness =RectangleAsset(1280, 720, thinlinewhite, white)
Sprite(whiteness,(0,1280))
ground =PolygonAsset([(1280,720,), (0,720,), (0,700,), (1280,700,)], thinlinegreen, green)
Sprite(ground)
coicle =CircleAsset(70, thinlineyellow, yellow)
Sprite(coicle,(250,250))
Boird =PolygonAsset([(0,0,),(10,5,),(15,5),(10,-10),(20,-5,),(25,5,),(30,5,),(30,0,),(32.5,-3,),(35,-5,),(37.5,-3,),(40,0),(45,2.5),(35,7.5,),(30,15,),(20,15,),(10,12.5,)],thinlineblack, red)
ellipse=EllipseAsset(1.2,1.0, thinlineblack, black)
Sprite(Boird, (100,100))
Sprite(ellipse, (137,101))
Sprite(Boird, (250,120))
Sprite(ellipse, (287,121))
Sprite(Boird, (300,370))
Sprite(ellipse, (337,371))
Sprite(Boird, (370,200))
Sprite(ellipse, (407,201))
Sprite(Boird, (150,420))
Sprite(ellipse, (187,421))


# add your code here /\  /\  /\


myapp = App()
myapp.run()
