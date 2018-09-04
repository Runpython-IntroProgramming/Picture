"""
picture.py
Author: Jack Meehan
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

green = Color(0x00ff00, 1.0)
blue = Color(0x0f0fff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
thinline = LineStyle(2, blue)
rectangle = RectangleAsset(200, 100, thinline, green)
Sprite(rectangle, (200, 200))

roof = PolygonAsset([(305, 100), (210, 150), (407, 150)], thinline, black)
Sprite(roof, (200, 150))

door = RectangleAsset(30, 60, thinline, blue)
Sprite(door, (255, 240))

doorwindow = RectangleAsset(29, 22, thinline, black)
Sprite(doorwindow, (255, 242))

window = CircleAsset(22, thinline, black)
Sprite(window, (318, 230))

path = PolygonAsset([(310, 300), (260, 360), (250, 360), (300, 300)], thinline, black)
Sprite(path, (300, 300))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
