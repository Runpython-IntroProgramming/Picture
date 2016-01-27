"""
picture.py
Author: <your name here>
Credit: Andreas and colorpicker.com

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
teal = Color(0x24B5B5, 1.0)
yellow = Color(0xFFF700, 1.0)
purple = Color(0x6F00FF, 1.0)
orange = Color(0xFF6A00, 1.0)
white = Color(0xFFFFFF, 1.0)

#lines
thinline = LineStyle(1, black)
thickerline = LineStyle(10, green)
greenline = LineStyle(1, green)
redline = LineStyle(1, red)
blueline = LineStyle(1, blue)
tealline = LineStyle(1, teal)
yellowline = LineStyle(1, yellow)
purpleline = LineStyle(1, purple)
orangeline = LineStyle(1, orange)

#shapes
house = RectangleAsset(300, 300, thinline, teal)
grassyhill = CircleAsset(600, greenline, green)
sun = CircleAsset(150, yellowline, yellow)
roof = PolygonAsset([(5,120), (165,1), (335,120)], tealline, purple)
windowa = RectangleAsset(85, 85, thinline, blue)
windowb = RectangleAsset(85, 85, thinline, blue)
windowc = RectangleAsset(85, 85, thinline, blue)
windowd = RectangleAsset(85, 85, thinline, blue)
door = RectangleAsset(70, 90, thinline, red)
knob = CircleAsset(10, thinline, black)
sandyhill = CircleAsset(600, orangeline, orange)
moon = CircleAsset(150, thinline, white)


#sprites
Sprite(sandyhill, (300, 1100))
Sprite(grassyhill, (680, 1000))
Sprite(house, (520, 240))
Sprite(sun, (1020, 150))
Sprite(roof, (500, 119))
Sprite(windowa, (540, 270))
Sprite(windowb, (720, 270))
Sprite(windowc, (540, 400))
Sprite(windowd, (720, 400))
Sprite(door, (640, 440))
Sprite(knob, (700, 490))
Sprite(moon, (320, 150))
# add your code here /\  /\  /\


myapp = App()
myapp.run()

# add your code here /\  /\  /\


myapp = App()
myapp.run()
