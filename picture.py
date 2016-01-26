"""
picture.py
Author: Mary Feyrer
Credit: colorpicker.com

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
yellow = Color(0xF2EC41, 1.0)
darkgreen = Color(0x278F28, 1.0)
brown = Color(0x693C0E, 1.0)
lightblue = Color(0x7EE7F2, 1.0)
thinline = LineStyle(1, black)

sky = RectangleAsset(300, 250, thinline, lightblue)
ground = RectangleAsset(300, 50, thinline, green)
sun = CircleAsset(20, thinline, yellow)
trunk = RectangleAsset(20, 40, thinline, brown)
tree = PolygonAsset([(180,10),(140,90),(220,90)], thinline, darkgreen)
tree2 = PolygonAsset([(180,10),(135,90),(225,90)], thinline, darkgreen)
stem = RectangleAsset(5,15, thinline, green)

Sprite(sky)
Sprite(ground, (0, 200))
Sprite(sun, (30,30))
Sprite(trunk, (170, 170))
Sprite(tree2, (0, 90))
Sprite(tree, (0, 45))
Sprite(stem, (60, 180))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
