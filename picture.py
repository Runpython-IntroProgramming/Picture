"""
picture.py
Author: maCucyrt07
Credit: Kyle, Mr. Dennison

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


# add your code here /\  /\  /\


yellow = Color(0xFCF4A3, 1.0)
black = Color(0x000000, 1.0)
red = Color(0xDFF2800, 1.0)
thinline = LineStyle(1, black)
rectangle = RectangleAsset(100, 50, thinline, black)
rectangle2 = RectangleAsset(150,150, thinline, yellow)
Sprite(rectangle, (600,300))
circle = CircleAsset (150, thinline, red)
circle2 = CircleAsset (100, thinline, yellow)
Sprite(circle, (20, 20))
ellipse = EllipseAsset(75,50, thinline, yellow)
Sprite(ellipse)
polygon = PolygonAsset([(100,200),(250,300),(150,600),(700,300)], thinline, red)
polygon2 = PolygonAsset([(25, 50), (75, 100), (125, 100), (175, 150)], thinline, black)
Sprite(polygon, (100,100))
Sprite(circle, (200,400))
Sprite(rectangle, (800, 300))
Sprite(circle2, (250,200))
Sprite(rectangle2, (500, 350))
Sprite(ellipse, (900, 600))
Sprite(polygon2, (800,400))
myapp = App()
myapp.run()