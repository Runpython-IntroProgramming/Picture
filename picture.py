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
from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xf8f8ff, 1.0)
pwhite = Color(0xfffafa,1.0) 
thinline = LineStyle(1, black)
thinline1 = LineStyle(1, pwhite)

circle = CircleAsset(50, thinline, red)
Sprite(circle, (50, 50))

base = RectangleAsset(200, 200, thinline, blue)
Sprite(base, (900, 400))

roof = PolygonAsset([(0,0), (200,0), (100, -120)], thinline, black)
Sprite(roof, (900, 400))

window1 = RectangleAsset(50, 80, thinline, white)
Sprite(window1, (920, 430))

window2 = RectangleAsset(50, 80, thinline, white)
Sprite(window2, (1030, 430))

door = CircleAsset(50, thinline, green)
Sprite(door, (1000, 600))

door1 = RectangleAsset(200, 200, thinline1, white)
Sprite(door1, (899, 600))

floor = PolygonAsset([(0,0), (200,0), (200, 1), (0,1)], thinline, green)
Sprite(floor, (0, 400))
# add your code here /\  /\  /\


myapp = App()
myapp.run()
