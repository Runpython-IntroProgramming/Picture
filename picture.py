"""
picture.py
Author: miViriaz15
Credit: I used the internet for drawing inspiration, https://www.rapidtables.com/web/color/html-color-codes.html for color codes 

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
from math import sqrt
# add your code here \/  \/  \/
#defining colors
cornflowerblue = Color(0x6495ED, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xFFFFFF, 1.0)

#defining line
thinlineblue = LineStyle(1, cornflowerblue) 
thinlinewhite = LineStyle(1, white)
thinlineblack = LineStyle(1, black)

#Defining Shapes
triangle = PolygonAsset([(500,500), (1000,500), (750, 500+ 250*sqrt(3))],thinlineblue, cornflowerblue)
circle = CircleAsset(100,thinlineblue,cornflowerblue)
smalltriangle = PolygonAsset([(725,600), (775,600), (750, 600+ 25*sqrt(3))],thinlineblack, black)
whiteeye = CircleAsset(32,thinlinewhite,white)
pupil = CircleAsset(12,thinlineblack,black)
whisker = RectangleAsset(100,7,thinlineblack,black)
#print
s=Sprite(triangle, (120,120))
s.scale=0.8
Sprite(circle, (60,45))
Sprite(circle, (380,45))
Sprite(smalltriangle, (294.5,420))
Sprite(whiteeye, (225,200))
Sprite(whiteeye, (350,200))
Sprite(pupil, (230, 220))
Sprite(pupil, (355, 220))
w=Sprite(whisker, (370, 330))
w.rotation=.3
W=Sprite(whisker, (370, 335))
W.rotation=0
m=Sprite(whisker, (370, 340))
m.rotation=-.3
r=Sprite(whisker, (174, 301))
r.rotation=-.3
k=Sprite(whisker, (170, 335))
k.rotation=0
l=Sprite(whisker, (174, 368))
l.rotation=.3

#s.rotation=inradians
# add your code here /\  /\  /\


myapp = App()
myapp.run()
