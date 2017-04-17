"""
picture.py
Author: J Napier
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
thinline2=LineStyle(1, blue)
thinline = LineStyle(1, black)
circle1=CircleAsset(100, thinline, black)
circle=CircleAsset(385,thinline,green)
iris=CircleAsset(40, thinline2, blue)
ellipse=EllipseAsset(200,75, thinline, red)
eyebrow=RectangleAsset(200, 20, thinline, black)
poly=PolygonAsset([(685, 410), (715, 410), (700, 380), (685, 410)], thinline, red)
poly2=PolygonAsset([(1085, 410), (1115, 410), (1100, 380), (1085, 410)], thinline, red) 
tri1=PolygonAsset([(800, 230), (1000, 230), (900, 70), (800, 230)], thinline, blue)
tri2=PolygonAsset([(800, 230), (900, 230), (850, 150), (800, 230)], thinline, black)
tri3=PolygonAsset([(900, 230), (1000, 230), (950, 150), (900, 230)], thinline, black)
tri4=PolygonAsset([(850, 150), (950, 150), (900, 70), (850, 150)], thinline, black)
sp=Sprite(circle, (900,395))
Sprite(circle1, (700, 395))
Sprite(circle1, (1100, 395))
Sprite(ellipse, (900, 630))
Sprite(eyebrow, (600, 250))
Sprite(eyebrow, (1000, 250))
Sprite(iris, (700, 395))
Sprite(iris, (1100, 395))
Sprite(poly, (0,0))
Sprite(poly2, (0,0,))
Sprite(tri1, (0,0))
Sprite(tri2, (0,0))
Sprite(tri3, (0,0))
Sprite(tri4, (0,0))
# add your code here /\  /\  /\


myapp = App()
myapp.run()
