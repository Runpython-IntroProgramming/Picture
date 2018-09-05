"""
picture.py
Author: <Kyle Rozzi>
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

face = Color(0xFFD39B, 1.0)
white = Color(0xF0F8FF, 1.0)
eyes = Color(0x458B74, 1.0)
black = Color(0x000000, 1.0)

thinline = LineStyle(1, black)
ellipse = EllipseAsset(64,80, thinline, face)
Sprite(ellipse,(64,80))


eye1 = CircleAsset(16, thinline, white)
Sprite(eye1,(90,130))


eye2 = CircleAsset(16, thinline, white)
Sprite(eye2,(140,130))

pupil1 = CircleAsset(8, thinline, eyes)
Sprite(pupil1,(148,138))

pupil1 = CircleAsset(8, thinline, eyes)
Sprite(pupil1,(98,138))

pupil2 = CircleAsset(3, thinline, black)
Sprite(pupil2,(103,143))

pupil2 = CircleAsset(3, thinline, black)
Sprite(pupil2,(153,143))

mouth = CircleAsset(13, thinline, black)
Sprite(mouth,(125,190))

nose = RectangleAsset(20,12, thinline, face)
Sprite(nose,(122,168))


# add your code here /\  /\  /\


myapp = App()
myapp.run()
