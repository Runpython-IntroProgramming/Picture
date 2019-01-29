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
white = Color(0xffffff, 1.0)
flesh = Color (0xeac086, 1.0)
noseflesh = Color (0xeac190, 1.0)

thinline = LineStyle(1, flesh)
line = LineStyle(1, black)
line2 = LineStyle(1, green)

background = RectangleAsset(2000, 2000, line, red)
ellipse = EllipseAsset(200, 250, line, flesh)
eyerim = EllipseAsset(50, 25, line, white)
iris = CircleAsset(25, line2, green)
pupil = CircleAsset(10, line, black)
nose = EllipseAsset(20, 50, line, noseflesh)
mouthrim = EllipseAsset(100, 20, line, white)
lineobject = RectangleAsset(200, 1, line, black)
neck = RectangleAsset(150, 200, line, flesh)
hair = RectangleAsset(400, 200, line, black)

Sprite(background)
Sprite(neck, (350, 500))
Sprite(ellipse, (250, 50))
Sprite(eyerim, (300, 200))
Sprite(eyerim, (500, 200))
Sprite(iris, (325, 200))
Sprite(iris, (525, 200))
Sprite(pupil, (340, 215))
Sprite(pupil, (540, 215))
Sprite(nose, (425, 260))
Sprite(mouthrim, (350, 425))
Sprite(lineobject, (350, 445))
Sprite(hair, (250, -30))
# add your code here /\  /\  /\


myapp = App()
myapp.run()
