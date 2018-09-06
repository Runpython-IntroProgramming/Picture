"""
picture.py
Author: Patrick Daley
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
black = Color(0x000000, 1.0)
brown = Color(0x8B4513, 1.0)
black1 = Color(0x000000, 0.2)
thinline = LineStyle(1, black)
#House bottom
rectangle = RectangleAsset(500, 500, thinline, brown)
Sprite(rectangle, (250, 250))
#House top
triangle = PolygonAsset([(-250, 250), (0,0), (250, 250)], thinline, brown)
Sprite( triangle, (250, 0))

#Windows Top
window = RectangleAsset(50, 75, thinline, black1)
Sprite( window, (295, 300))

window2 = RectangleAsset(50, 75, thinline, black1)
Sprite( window2, (475, 300))

window3 = RectangleAsset(50, 75, thinline, black1)
Sprite( window3, (655, 300))

#Windows bottom
window4 = RectangleAsset(50, 75, thinline, black1)
Sprite( window4, (295, 425))

window5 = RectangleAsset(50, 75, thinline, black1)
Sprite( window5, (655, 425))

#Door
door = RectangleAsset(50, 125, thinline, black)
Sprite( door, (475, 425))

doorhandle = CircleAsset(5, thinline, brown)
Sprite( doorhandle, (510, 480))

#Window Circle
circle =  CircleAsset(50, thinline, black)
Sprite(circle, (450, 30))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
