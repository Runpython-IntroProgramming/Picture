"""
picture.py
Author: Noah Pikielny
Credit: 

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
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
yellow = Color(0xffff00, 1.0)
brown = Color(0x9C661F, 1.0)
cyan = Color(0x98F5FF, 1.0)


thinLine = LineStyle(1, black)
mouthCoverLine = LineStyle(0, yellow)

house = RectangleAsset(300, 300, thinLine, brown)
roof = PolygonAsset([(0,0), (150,-150), (300,0)], thinLine, red)
ground = RectangleAsset(1070, 70, thinLine, green)
sun = CircleAsset(60, thinLine, yellow)
eyeLeft = RectangleAsset(10, 10, thinLine, black)
eyeRight = RectangleAsset(10, 10, thinLine, black)
mouth = EllipseAsset(40, 10, thinLine, black)
mouthCover = EllipseAsset(40, 10, mouthCoverLine, yellow)
window = RectangleAsset(100, 100, thinLine, cyan)

# add your code here /\  /\  /\
Sprite(roof, (300,300 - 150))
Sprite(house, (300, 300))
Sprite(ground, (0,601))
Sprite(sun, (0,0))
Sprite(eyeLeft, (30, 30))
Sprite(eyeRight, (80, 30))
Sprite(mouth, (20,60))
Sprite(mouthCover, (20, 55))
Sprite(window, (300 + 100, 300 + 100))

myapp = App()
myapp.run()
