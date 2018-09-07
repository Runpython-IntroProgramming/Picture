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
tongue = Color(0x16A085,1.0)
black = Color(0x000000,1.0)
clear = Color(0x000000,0.0)
#Lines
thinline = LineStyle(1, black)
clearline = LineStyle(1,clear)
#Head pieces
skull = CircleAsset(58,clearline,skin)
jaw = RectangleAsset(90,75,clearline,skin)
#Eye pieces
leye = CircleAsset(17,thinline,white)
reye = CircleAsset(17,thinline,white)
lpupil = CircleAsset(5,thinline, black)
rpupil = CircleAsset(5,thinline,black)
#Mouth pieces
left = EllipseAsset(25,13,thinline,black)
right = EllipseAsset(22,12,thinline,black)
mouthTongue = EllipseAsset(25,10,thinline,tongue)
gills1 = RectangleAsset(30,10,thinline, gill)
gills2 = RectangleAsset(30,10,thinline,gill)
gills3 = RectangleAsset(30,10,thinline,gill)
gills4 = RectangleAsset(30,10,thinline,gill)


#Sprites
#Head base
Sprite(skull,(202,50))
Sprite(jaw, (226,94))
#Mouth
Sprite(left,(233,128))
Sprite(right,(265,130))
Sprite(mouthTongue,(248,136))
#Facial Features
Sprite(leye, (230,80))
Sprite(reye, (280,80))
Sprite(lpupil,(245,92))
Sprite(rpupil,(295,92))


Sprite(gills1)

# add your code here /\  /\  /\


myapp = App()
myapp.run()
