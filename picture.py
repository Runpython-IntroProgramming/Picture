"""
picture.py
Author: <Suhan Gui>
Credit: <http://www.color-hex.com/>

Assignment: Picture

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
white= Color(0xfffffff, 1.0)
gold= Color(0xffd700, 1.0)
skin= Color(0xffefdb, 1.0)
blue=
pale=

thinline = LineStyle(2, black)

face= CircleAsset(200, thinline, skin)
Pupil= EllipseAsset(5,75,thinline,black)
Mouth= EllipseAsset(75,20,thinline,red)
ring1= CircleAsset(30, thinline, white)
ring2= CircleAsset(40, thinline, gold)
face2= CircleAsset(
Geyes= CircleAsset(
Gmouth= EllipseAsset(
WierdEar= PolygonAsset(
Ground= RectangleAsset(

""" Frodo"""
Sprite(face, (400,400))
Sprite(Pupil, (600,350))
Sprite(Pupil, (500,350))
Sprite(Mouth, (550,600))

"""ring"""
Sprite(ring2, (900,150))
Sprite(ring1, (900,150))

"""gollum"""
Sprite(face2, (850,850))
Sprite(Geyes,
Sprite(Geyes,
Sprite(Gmouth,
Sprite(Nose,

Sprite(Ground,
# add your code here /\  /\  /\


myapp = App()
myapp.run()

