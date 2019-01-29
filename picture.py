"""
picture.py
Author: waSclthu11
Credit: The tutorial and the ggame core API (tells you how to use everything).

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
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, TextAsset
app = App()

# add your code here \/  \/  \/
wah = Color(0xedcc9b, 1.0)
purple= Color(0xce27d3, 1.0)
white = Color(0xffffff, 1.0)
black = Color(0x000000, 1.0)
blue = Color(0x00ffff, 1.0)
wahh = Color(0xffb6c1, 1.0)
thinline = LineStyle(1, black)
noline = LineStyle(0, white)
print("BEHOLD, Waluigi!")
eyeshadow = EllipseAsset(25, 15, thinline, blue)
eye = EllipseAsset(25, 15, thinline, white)
face = EllipseAsset(100, 100, noline, wah)
rectangle = RectangleAsset(50, 20, thinline, purple)
hat = EllipseAsset(100, 70, thinline, purple)
nose = EllipseAsset(20, 40, thinline, wahh)
chin = PolygonAsset([(-45, 60), (-70, 0), (70, 0), (45, 60)], noline, wah)
www = PolygonAsset([(-10, 70), (-45, 0), (-45, -50), (-40, -50), (-40, 0), (40, 0), (40, -50), (45, -50), (45, 0), (10, 70)], noline, wah)
dot = CircleAsset(7, thinline, black)
stache = PolygonAsset([(-100, 0), (-50, 10), (0, 0), (50, 10), (100, 0), (50, 30), (0, 10), (-50, 30), (-100, 0)])
logo = CircleAsset(35, noline, white)
A = TextAsset("L", style="bold 40pt Arial", width=250, fill=Color(0x1122FF, 1.0))


Sprite(chin, (316, 290))
Sprite(face, (289, 120))
Sprite(eyeshadow, (305, 230))
Sprite(eyeshadow, (420, 230))
Sprite(eye, (305, 225))
Sprite(eye, (420, 225))
Sprite(hat, (290, 100))
Sprite(www, (342, 345))
Sprite(nose, (367, 235))
Sprite(dot, (325, 230))
Sprite(dot, (435, 230))
Sprite(stache, (285, 330))
Sprite(logo, (353, 150))
Sprite(A, (353, 150))




# add your code here /\  /\  /\


myapp = App()
myapp.run()
