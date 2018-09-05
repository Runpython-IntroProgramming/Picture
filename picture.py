"""
picture.py
Author: Eric Goodney
Credit: Peers and the internet

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

clear = Color(0xBFBFBF, 1.0) 
brown = Color(0xCD5B45, 1.0)
black = Color(0x000000, 1.0)
drkgreen = Color(0x006400, 1.0)
houseclr = Color(0xFFF8DC, 1.0)
yellow = Color(0xEEEE00, 1.0)

thinline = LineStyle(1, brown)

rectangle = RectangleAsset(250,250, thinline, houseclr)
triangle = PolygonAsset([(200,0), (325,-100),  (450,0)], thinline, black)
door = RectangleAsset(50,100, thinline, brown)
window1 = RectangleAsset(60,60, thinline, clear)
window2 = RectangleAsset(60,60, thinline, clear)
circlewindow = CircleAsset(25, thinline, brown)
tree1 = PolygonAsset([(100,0), (150,-100),  (200,0)], thinline, drkgreen)
tree2 = PolygonAsset([(100,0), (150,-100),  (200,0)], thinline, drkgreen)
tree3 = PolygonAsset([(100,0), (150,-100),  (200,0)], thinline, drkgreen)
tree4 = PolygonAsset([(100,0), (150,-100),  (200,0)], thinline, drkgreen)
doorknob = RectangleAsset(10,10, thinline, black)
sun = EllipseAsset(20,24, thinline, yellow)

Sprite(rectangle,(400,200))
Sprite(triangle,(400,100))
Sprite(door,(500,350))
Sprite(window1,(420,230))
Sprite(window2,(570,230))
Sprite(circlewindow,(500,140))
Sprite(tree1,(250,350))
Sprite(tree2,(300,350))
Sprite(tree3,(650,350))
Sprite(tree4,(700,350))
Sprite(doorknob,(508,390))
Sprite(sun, (700,35))

# add your code here /\  /\  /\

myapp = App()
myapp.run()



