"""
picture.py
Author: <your name here>
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

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
darkgreen = Color(0x0e270f, 1.0)
nightsky = Color(0x16152b, 1.0)
ground = Color(0x06471a, 1.0)
wood = Color(0x542a0c, 1.0)
line = LineStyle(2, black)



tri4 = PolygonAsset([(0,100),(200,100),(100,0)], line, darkgreen )
tri3 = PolygonAsset([(0,100),(200,100),(100,0)], line, darkgreen )
tri2 = PolygonAsset([(0,100),(200,100),(100,0)], line, darkgreen )
tri1 = PolygonAsset([(0,100),(200,100),(100,0)], line, darkgreen )
background = RectangleAsset( 1000, 1000, line, nightsky )
ground = RectangleAsset( 1000, 100, line, ground )

Sprite(background, (0, 0))
Sprite(tri4, (20, 400))
Sprite(tri3, (20, 450))
Sprite(tri2, (20, 500))
Sprite(tri1, (20, 550))
Sprite(ground, (0, 700))
# add your code here /\  /\  /\


myapp = App()
myapp.run()
