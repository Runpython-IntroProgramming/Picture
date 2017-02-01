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

# Defining colors
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

# Defining Lines
thinline = LineStyle(1, black)
# Creating Blueprint for each sprite
rectangle = RectangleAsset(400, 30, thinline, red)
rectangle2 = RectangleAsset(600, 30, thinline, red)
rectangle3 = RectangleAsset(200, 210, thinline, blue)
rectangle4 = RectangleAsset(20, 800, thinline, red)
circle = CircleAsset(100, thinline, red)
polygon = PolygonAsset([(300, 200), (350, 200), (350, 350) , (300, 200)], thinline, green)

# Creating sprites
Sprite(rectangle, (300, 100))
Sprite(rectangle, (300, 170))
Sprite(rectangle, (300, 240))
Sprite(rectangle, (200, 600))
Sprite(rectangle2, (100, 310))
Sprite(rectangle2, (100, 380))
Sprite(rectangle2, (100, 450))
Sprite(rectangle3,(100,100))
Sprite(circle, (900, 300))
Sprite(polygon, (200, 300))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
