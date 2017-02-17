"""
picture.py
Author: Kyle Postans
Credit: none ever
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
rot = Color(0xff0000, 0.8)
grun = Color(0x00ff00, 1.0)
blau = Color(0x0000ff, 1.0)
schwartz = Color(0x000000, 1.0)
orange = Color(0xffa500, 1.0)
gelb = Color(0xffff00, 0.7)

porklein = LineStyle (1, schwartz)

brick = RectangleAsset(190, 68, porklein, rot) #brick
face = EllipseAsset(68,76, porklein, gelb) #face
hair = EllipseAsset(65, 20, porklein, orange)
eyes = CircleAsset(10, porklein, schwartz) #eyes
mouth = CircleAsset(13, porklein, rot)
haircurl = PolygonAsset([(7,1), (5, 1), (60, 1)], porklein, schwartz)


Sprite(brick, (100, 265))
Sprite(brick, (290, 265))
Sprite(brick, (480, 265))
Sprite(brick, (670, 265))

Sprite(brick, (90,333))
Sprite(brick, (280, 333))
Sprite(brick, (470, 333))
Sprite(brick, (660, 333))
Sprite(face, (180, 190))
#Sprite(hair, (175, 126))
Sprite(eyes, (170, 170))
Sprite(eyes, (210, 170))
Sprite(mouth, (190, 210))
Sprite(haircurl, (150, 126))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
