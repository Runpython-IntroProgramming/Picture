"""
picture.py
Author: Dimitri
Credit: Mr. Dennison

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
black = Color(0x000000, 0.9)
brown = Color(0x77583A, 1.0)
white = Color(0xFFFFFF, 1.0)

thinline = LineStyle(1, black)
whiteline = LineStyle(1, white)

background = RectangleAsset(500, 500, thinline, green)
ground = RectangleAsset(500, 200, thinline, brown)
sky = RectangleAsset(500, 250, thinline, blue)
clouds = CircleAsset(30, whiteline, white)
cloud = EllipseAsset(50, 20, whiteline, white)
tree = PolygonAsset(([0, 60], [75, 0], [150, 60]), thinline, red)
trunk = RectangleAsset(20, 95, thinline, brown)
rock = CircleAsset(60, thinline, black)

Sprite(background)
Sprite(ground, (0, 300))
Sprite(sky)
Sprite(clouds, (50, 50))
Sprite(clouds, (75, 75))
Sprite(cloud, (100, 50))
Sprite(clouds, (150, 75))
Sprite(bush, (350, 100))
Sprite(trunk, (415, 159))
Sprite(rock, (250, 240))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
