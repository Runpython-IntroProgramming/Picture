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
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/TUTORIAL:-Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
red = Color(0xff0000, 1.0)
green = Color(0x0ff000, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white= Color(100, 1.0)

thinline = LineStyle(2, black)


face= CircleAsset(300, thinline, green)
Pupil= EllipseAsset(10,100,thinline,black)
Mouth= EllipseAsset(100,30,thinline,red)
ring1= CircleAsset(200, thinline, white)

""" Frodo"""
Sprite(face, (400,400))
Sprite(Pupil, (600,400))
Sprite(Pupil, (500,400))
Sprite(Mouth, (550,600))

"""ring"""
Sprite(ring1, (400,400))
# add your code here /\  /\  /\


myapp = App()
myapp.run()
