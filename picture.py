"""
picture.py
Author: Sawyer Hanlon
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
background = Color(0xafeeee, 1.0)
clouds = Color(0xf5f5f5, 1.0)

thinline=LineStyle(1, black)

background=RectangleAsset(1000000000, 100000000, thinline, background)
Sprite(background, (10, 1))

elipse=EllipseAsset(200, 75, thinline, Sawyer)
Sprite(elipse, (600, 700))

rectangle=RectangleAsset(100200, 500, thinline, blue)
Sprite(rectangle, (10, 700))

mast=RectangleAsset(15, 450, thinline, Sawyer)
Sprite(mast, (600, 200))

sail=PolygonAsset([(600,400), (850,300), (600,200), (600,400)], thinline, red)
Sprite(sail, (0,0))

sun=CircleAsset(80, thinline, yellow)
Sprite(sun, (900, 20))

float=EllipseAsset(75, 14, thinline, red)
Sprite(float, (80, 700))

float2=PolygonAsset([(30,700), (130,700), (80, 600), (30,700)], thinline, red)
Sprite(float2, (0,0))

float3=CircleAsset(25, thinline, green)
Sprite(float3, (80, 600))

cloud=EllipseAsset(200, 75, thinline, clouds)
Sprite(cloud, (200, 100))





# add your code here /\  /\  /\


myapp = App()
myapp.run()
