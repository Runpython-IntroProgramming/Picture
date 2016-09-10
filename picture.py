"""
picture.py
Author: Daniel M
Credit: Myself, Dad, Internet

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
yellow=Color(0xffff00,1.0)
green=Color(0x32cd32,1.0)
white=Color(0xfffafa,0)
brown=Color(0x8b4513,1.0)
cloudwhite=Color(0xf5f5f5,1.0)

thinline = LineStyle(1, black)

rectangleBlue = RectangleAsset(50, 50, thinline, green)
rectangleRed = RectangleAsset(120, 120, thinline, red)
cloud=EllipseAsset(60,40,thinline,cloudwhite)
sun=CircleAsset(100,thinline,yellow)
borders=RectangleAsset(1200,565,thinline,white)
roof=PolygonAsset([(540,450),(610,450),(500,365),(540,450)],thinline,blue)

Sprite(cloud,(200,150))
Sprite(cloud,(700,100))
Sprite(cloud,(400,250))
Sprite(sun,(0,0))
Sprite(borders,(0,0))
Sprite(rectangleRed,(500,465))
Sprite(roof)
# add your code here /\  /\  /\


myapp = App()
myapp.run()
