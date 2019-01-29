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
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, LineAsset

# add your code here \/  \/  \/
light_blue = Color(0x00bfff,1.0)
brownishred = Color(0xa52a2a,1.0)
black = Color(0x000000,1.0)
brown = Color(0x593C1F,1.0)
green = Color(0x50C878,1.0)
yellow = Color(0xffff00,1.0)
white = Color(0xffffff,1.0)
darkgreen = Color(0x006400, 1.0)

thinline = LineStyle(1,black)
rayline = LineStyle(4,yellow)
thickerline = LineStyle(5,black)
treeline = LineStyle(1,darkgreen)

background = RectangleAsset(1000,500, thinline, light_blue)
house_wall = RectangleAsset(300,200, thinline, brownishred)
grass = RectangleAsset(1000,50, thinline, green)
roof = PolygonAsset(((-170,100),(0,-100),(170,100),(-170,100)), thinline, brown)
sun = CircleAsset(50,thinline, yellow)
sunray = LineAsset(70,0,rayline)
sunray1 = LineAsset(70,-20,rayline)
sunray2 = LineAsset(70,-40,rayline)
sunray3 = LineAsset(40,-70,rayline)
sunray4 = LineAsset(0,-80,rayline)
window = RectangleAsset(80,100,thickerline,white)
door = RectangleAsset(80,150,thinline,brown)
doorknob = CircleAsset(7,thinline,black)
windowpane = LineAsset(80,0,thickerline)
windowpane1 = LineAsset(0,100,thickerline)
treetrunk = RectangleAsset(50,150,thinline,brown)
leaves = EllipseAsset(80,100,treeline,darkgreen)
leaves1 = EllipseAsset(80,100,treeline,darkgreen)
leaves2 = EllipseAsset(80,100,treeline,darkgreen)

Sprite(background)
Sprite(house_wall,(350,250))
Sprite(grass, (0,450))
Sprite(roof,(330,50))
Sprite(sun, (850,20))
Sprite(sunray, (770,30))
Sprite(sunray1, (760,70))
Sprite(sunray2, (760,100))
Sprite(sunray3, (820,120))
Sprite(sunray4, (900,130))
Sprite(window, (380,300))
Sprite(door, (540,300))
Sprite(doorknob, (600,370))
Sprite(windowpane, (380,347.5))
Sprite(windowpane1, (417.5,300))
Sprite(treetrunk, (120,300))
Sprite(leaves, (105,150))
Sprite(leaves1, (25,150))
Sprite(leaves2, (65,70))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
