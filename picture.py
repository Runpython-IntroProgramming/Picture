"""
picture.py
Author: Nils Kingston
Credit: none

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
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/TUTORIAL:-Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

thinline = LineStyle(1, black)

MainHouse = RectangleAsset (300,325, thinline, black)
Sprite(MainHouse, (100,175))

door = RectangleAsset (50, 100, thinline, blue)
Sprite(door, (225, 400))

SecondHouse = RectangleAsset (275, 200, thinline, black)
Sprite(SecondHouse, (400, 300))

DoorHandle = CircleAsset (3, thinline, red)
Sprite(DoorHandle, (260, 445))
 
roof1 = PolygonAsset ([(100, 175), (250, 110), (400, 175)],  thinline, green)
Sprite(roof1)

roof2 = PolygonAsset ([(400, 300), (400, 175), (675, 300)],  thinline, green)
Sprite(roof2)

# add your code here /\  /\  /\



myapp = App()
myapp.run()
