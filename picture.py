"""
picture.py
Author: Dina
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

red= Color(0xff0000, 1.0)
pink = Color(0xff55f0, 1.0)
blue = Color(0x1010ff, 1.0)
skin = Color(0xffffee,1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
hair1 = Color(0x551000, 1.0)
hair2 = Color(0x5512020, 1.0)

thinline = LineStyle(1, black)
thickline = LineStyle(4, black)
noline = LineStyle(0, white)

corner1= 440
corner2= 250
corner3= 480
corner4= 250
corner5= 550
corner6= 250
corner7= 250
corner8= 250

rectangle1 = RectangleAsset(600, 400, thinline, skin)
rectangle2 = RectangleAsset(100, 100, thinline, white)
ellipse1 = EllipseAsset(200, 250, thinline, skin)
triangle1 = PolygonAsset([(corner1, corner2), (460, 230), (460, 270), (corner1, corner2)], thinline, pink)
triangle2 = PolygonAsset([(corner3, corner4), (460, 230), (460, 270), (corner3, corner4)], thinline, pink)
triangle3 = PolygonAsset([(corner5, corner6), (460, 230), (460, 270), (corner5, corner6)], thinline, pink)
triangle4 = PolygonAsset([(corner7, corner8), (460, 230), (460, 270), (corner7, corner8)], thinline, pink)
circle1 = CircleAsset(50, thinline, hair1)
circle2 = CircleAsset(55, thinline, hair2)
circle3 = CircleAsset(20, thinline, blue)
ellipse2 = EllipseAsset(100, 50, thinline, red)

#head
Sprite(ellipse1, (550,300))
#level 2 light hair
Sprite(circle2, (390, 80)) #2left3
Sprite(circle2, (500, 20)) #2left1
Sprite(circle2, (600, 25)) #2right1
Sprite(circle2, (720, 90)) #2right3
#level 2 dark hair
Sprite(circle1, (350, 130)) #2left4
Sprite(circle1, (420, 40)) #2left2
Sprite(circle1, (550, 10)) #2top
Sprite(circle1, (670, 50)) #2right2
Sprite(circle1, (760, 150)) #2right4
#level 1 lighthair
Sprite(circle2, (490, 100)) #left1
Sprite(circle2, (620, 95)) #right1
Sprite(circle2, (390, 170)) #left3
Sprite(circle2, (715, 180)) #right3
#level 1 dark hair
Sprite(circle1, (550, 90)) #top
Sprite(circle1, (440, 130)) #left2
Sprite(circle1, (680, 130)) #right2
Sprite(circle1, (350, 220)) #left4
Sprite(circle1, (750, 230)) #right4
#eyes
Sprite(triangle1)
Sprite(circle3, (450, 250))


#Sprite(rectangle2, (250, 250))
#mouth
Sprite(ellipse2,(550, 450))
#Sprite(triangle)

# add your code here /\  /\  /\


myapp = App()
myapp.run()