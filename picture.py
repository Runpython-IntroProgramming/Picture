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
gold = Color(0xFFD700, 1.0)
golder = Color(0xFFC900, 1.0)

#defining line
thinlineblue = LineStyle(1, cornflowerblue) 
thinlinewhite = LineStyle(1, white)
thinlineblack = LineStyle(1, black)
thinlinegold = LineStyle(1, gold)
thinlinegolder = LineStyle(1, golder) #I played around to get this one

#Defining Shapes
triangle = PolygonAsset([(500,500), (1000,500), (750, 500+ 250*sqrt(3))],thinlineblue, cornflowerblue)
circle = CircleAsset(100,thinlineblue, cornflowerblue)
smalltriangle = PolygonAsset([(725,600), (775,600), (750, 600+ 25*sqrt(3))],thinlineblack, black)
whiteeye = CircleAsset(32,thinlinewhite,white)
pupil = CircleAsset(12,thinlineblack,black)
whisker = RectangleAsset(100,7,thinlineblack,black)
cheese = RectangleAsset(180, 70, thinlinegold, gold)
cheesetop = PolygonAsset([(650,245), (830, 245), (780, 205), (650, 245)], thinlinegolder, golder)
cheesehole = EllipseAsset(17,10, thinlinegolder, golder)
alsocheesehole = EllipseAsset(9,6, thinlinegolder, golder)
alsoalsocheesehole = EllipseAsset(11,8, thinlinegolder, golder)
#print
    #head
s=Sprite(triangle, (120,120))
s.scale=0.8
    #ears
Sprite(circle, (60,45))
Sprite(circle, (380,45))
    #nose
Sprite(smalltriangle, (294.5,420))
    #eyes
Sprite(whiteeye, (225,200))
Sprite(whiteeye, (350,200))
Sprite(pupil, (255, 220))
Sprite(pupil, (380, 220))
    #whiskers
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
    #cheese
c=Sprite(cheese, (650, 245))
Sprite(cheesetop, (650, 205))
Sprite(cheesehole, (663, 260))
Sprite(cheesehole, (730, 280))
Sprite(alsocheesehole, (717, 255))
Sprite(alsocheesehole, (680, 295))
Sprite(alsoalsocheesehole, (785, 292))
Sprite(alsocheesehole, (800, 265))
Sprite(alsoalsocheesehole, (766, 256))
#s.rotation=inradians
# add your code here /\  /\  /\


myapp = App()
myapp.run()
