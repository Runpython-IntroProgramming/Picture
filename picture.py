"""
picture.py
Author: Sarah Dunbar
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
makebrown = Color(0xff0000, 1.0)
plum = Color(0xcc00ff, 1.0)
water = Color(0x0000ff, 0.5)
grassy = Color(0xeeff00, 1.0)
makebrown2 = Color(0x00ff00, 0.5)
black = Color(0x000000, 1.0)
grey = Color(0x000000, 0.5)
white = Color(0x000000, 0.0)
brown = Color(0xA0522D, 1.0)
skinwhite = Color(0xFFE7BA, 1.0)
tunic = Color(0x872657, 1.0)
fishscale = Color(0xEE1289, 1.0)

thinlineblack = LineStyle (1, black)
thinlinegrey = LineStyle (1, grey)

fishhead = EllipseAsset (
fishtail = PolygonAsset ([(0, 0), (0, 30), (50, 15), (0, 0)], thinlinegrey, fishscale)
ocean = RectangleAsset (600, 1600, thinlineblack, water)
land = EllipseAsset (100, 75, thinlinegrey, grassy)
house1 = RectangleAsset (50, 50, thinlineblack, bluedark)
sailboat = PolygonAsset ([(0, 0), (50, 25), (0, 50), (0, 0)], thinlinegrey, white)
roof1 = PolygonAsset ([(25, 0), (50, 50), (0, 50), (25, 0)], thinlinegrey, brown)
ship = PolygonAsset ([(0, 0), (100, 0), (75, 20), (25, 20), (0, 0)], thinlineblack, makebrown)
ship2 = PolygonAsset ([(0, 0), (100, 0), (75, 20), (25, 20), (0, 0)], thinlineblack, makebrown2)
personhead = EllipseAsset (5, 5, thinlinegrey, skinwhite)
personbody = RectangleAsset (10, 15, thinlineblack, tunic)

Sprite (fishtail, (300, 650))
Sprite (land, (650, 500))
Sprite(ocean, (200, 500))
Sprite(house1, (650, 400))
Sprite(roof1, (650, 350))
Sprite(ship, (400, 480))
Sprite(ship2, (400, 480))
Sprite(sailboat, (450, 430))
Sprite(personbody, (420, 465))
Sprite(personhead, (425, 458))


# add your code here /\  /\  /\


myapp = App()
myapp.run()
