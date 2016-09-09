"""
picture.py
Author: Bauti Gallino
Credit: Liam S.

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

thickline=LineStyle(3,black)

rectangle=RectangleAsset(200,140,thickline,red)
circle=CircleAsset(50, thickline, green)
ellipse=EllipseAsset(100,70,thickline,blue)
polygon=PolygonAsset([(0,0), (100,100), (25,50), (0,0)], thickline, black)
cow=RectangleAsset(100,140,thickline,blue)

Sprite(circle, (500, 100))
Sprite(rectangle,(100, 130))
Sprite(ellipse, (200, 200))
Sprite(polygon)
Sprite(cow, (700, 200))
Sprite(circle, (300, 600))
Sprite(ellipse, (700, 700))
Sprite(polygon, (60, 60))
Sprite(rectangle,(200, 260))
Sprite(cow, (500, 200))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
