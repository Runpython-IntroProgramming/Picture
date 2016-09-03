"""
picture.py
Author: <Vinzent>
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
from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

darkoragne = Color(0xFF9800, 1.0)
greywhite = Color(0xF5F5F5, 1.0)
lightblue = Color(0x03A9F4, 1.0)
oceanblue = Color(0x283593, 1.0)
beachyellow = Color(0xFFD54F, 1.0)
reflectionyellow = Color(0xE65100, 0.7)
palmbrown = Color(0x6D4C41, 1.0)

noline = LineStyle(0, greywhite)
thinline = LineStyle(1, greywhite)

background = RectangleAsset(25, 25, thinline, lightblue)
sun = RectangleAsset(25, 25, thinline, darkoragne)
ocean = RectangleAsset(25, 25, thinline, oceanblue)
beach = RectangleAsset(25, 25, thinline, beachyellow)
reflection = RectangleAsset(25, 25, thinline, reflectionyellow)
palm = RectangleAsset(25, 25, thinline, palmbrown)

#make a 1000px * 600px backgound
y=0
while(y<451):
    for x in range(0,1001, 25):
        Sprite(background, (x, y))
    y=y+25

#make the halfcircle sun
for b in range(800, 900, 25):
    Sprite(sun, (b, 300))
for b in range(750, 930, 25):
    Sprite(sun, (b, 325))
for b in range(725, 951, 25):
    Sprite(sun, (b, 350))
for b in range(725, 951, 25):
    Sprite(sun, (b, 375))
for b in range(700, 976, 25):
    Sprite(sun, (b, 400))
for b in range(700, 976, 25):
    Sprite(sun, (b, 425))
# make the ocean
y=450
while(y<601):
    for x in range(0,1001, 25):
        Sprite(ocean, (x, y))
    y=y+25
#make the beach
y=575
while(y<601):
    for x in range(0,1001, 25):
        Sprite(beach, (x, y))
    y=y+25
#make the reflection
for b in range(700, 976, 25):
    Sprite(reflection, (b, 450))
for b in range(675, 951, 25):
    Sprite(reflection, (b, 475))
for b in range(650, 926, 25):
    Sprite(reflection, (b, 500))
for b in range(625, 901, 25):
    Sprite(reflection, (b, 525))
for b in range(600, 876, 25):
    Sprite(reflection, (b, 550))
#make the palm
for b in range(300, 576, 25):
    Sprite(palm, (50, b))
for b in range(300, 576, 25):
    Sprite(palm, (75, b))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
