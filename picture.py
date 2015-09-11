"""
picture.py
Author: Ryan Kynor
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
thickline = LineStyle(2, black)
blueline = LineStyle(1, blue)
redline = LineStyle(1, red)
greenline = LineStyle(1, green)



rectangle1 = RectangleAsset(25000, 15000, thinline, red)
#rectangle2 = RectangleAsset(50, 20, thinline, red)
#rectangle3 = RectangleAsset(50, 20, thinline, red)
#rectangle4 = RectangleAsset(50, 20, thinline, red)

#circle1 = CircleAsset(200, thinline, green)
#circle2 = CircleAsset(200, thinline, green)
#circle3 = CircleAsset(200, thinline, green)
#circle4 = CircleAsset(200, thinline, green)

#ellipse1 = EllipseAsset()
#ellipse2 = EllipseAsset()
#ellipse3 = EllipseAsset()
#ellipse4 = EllipseAsset()

#polygon1 = PolygonAsset()
#polygon2 = PolygonAsset()
#polygon3 = PolygonAsset()
#polygon4 = PolygonAsset()



Sprite(rectangle1)
#Sprite(circle1, (400, 30))
#Sprite()
#Sprite()
#Sprite()
#Sprite()
#Sprite()
#Sprite()
#Sprite()
#Sprite()
#Sprite()



# add your code here /\  /\  /\


myapp = App()
myapp.run()
