"""
picture.py
Author: Olivia Simon
Credit: I used the how to ue ggame links; and https://htmlcolorcodes.com/ to find the color codes.

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

# colors
skin = Color(0x4BADC1,1.0)
white = Color(0xffffff,1.0)
gill = Color(0x44CA83,1.0)
bubble = Color(0x44CA83,0.5)
tongue = Color(0x16A085,1.0)
black = Color(0x000000,1.0)
clear = Color(0x000000,0.0)
#Lines
thinline = LineStyle(1, black)
thinnline = LineStyle(.5,black)
clearline = LineStyle(1,clear)
#Head pieces
skull = CircleAsset(58,clearline,skin)
jaw = RectangleAsset(95,75,clearline,skin)
lEar = PolygonAsset(((0,0),(0,30),(20,15),(0,0)),thinline,tongue)
rEar = PolygonAsset(((0,20),(20,5),(20,35),(0,20)),thinline,tongue)
#Eye pieces
leye = CircleAsset(17,thinline,white)
reye = CircleAsset(17,thinline,white)
lpupil = CircleAsset(5,thinline, black)
rpupil = CircleAsset(5,thinline,black)
#Mouth pieces
left = EllipseAsset(25,13,thinline,black)
right = EllipseAsset(22,12,thinline,black)
mouthTongue = EllipseAsset(32,8,clearline,tongue)
gill1 = RectangleAsset(10,2,thinnline, gill)
gill2 = RectangleAsset(10,2,thinnline,gill)
gill3 = RectangleAsset(10,2,thinnline,gill)
gill4 = RectangleAsset(10,2,thinnline,gill)
#Other
bubble1 = CircleAsset(15,clearline,bubble)
bubble2 = CircleAsset(10,clearline,bubble)
bubble3 = CircleAsset(25,clearline,bubble)
bubble4 = CircleAsset(10,clearline,bubble)


#Sprites
#Head base
Sprite(rEar,(306,102))
Sprite(skull,(202,50))
Sprite(jaw, (221,94))
Sprite(lEar,(210,100))
#Mouth
Sprite(left,(233,128))
Sprite(right,(265,130))
Sprite(mouthTongue,(239,142))
#Facial Features
Sprite(gill1,(222,151))
Sprite(gill2,(222,154))
Sprite(gill3,(222,157))
Sprite(gill4,(222,160))
#Eyes
Sprite(leye, (230,80))
Sprite(reye, (280,80))
Sprite(lpupil,(245,92))
Sprite(rpupil,(295,92))
#Bubbles
Sprite(bubble1,(295,55))
Sprite(bubble2,(270,96))
Sprite(bubble3,(320,80))
Sprite(bubble4,(290,110))
# add your code here /\  /\  /\


myapp = App()
myapp.run()
