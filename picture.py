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
Sawyer = Color(0x9e0000, 1.0)
yellow = Color(0Xffff00, 1.0)

thinline=LineStyle(1, black)

elipse=EllipseAsset(200, 75, thinline, Sawyer)
Sprite(elipse, (600, 700))
float=EllipseAsset(75, 14, thinline, red)
Sprite(float, (80, 500))
rectangle=RectangleAsset(100200, 500, thinline, blue)
Sprite(rectangle, (10, 700))
mast=RectangleAsset(15, 450, thinline, Sawyer)
Sprite(mast, (600, 200))
sail=PolygonAsset([(600,400), (850,300), (600,200), (600,400)], thinline, red)
Sprite(sail, (0,0))
sun=CircleAsset(80, thinline, yellow)
Sprite(sun, (900, 20))
float=ElipseAsset(75, 14, thinline, red)



# add your code here /\  /\  /\


myapp = App()
myapp.run()
