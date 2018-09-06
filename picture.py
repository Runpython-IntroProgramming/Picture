"""
picture.py
Author: Pierre Mayo
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
Tan = Color(0xFFEBCD, 1.0)
White = Color(0xFFFFFF, 1.0)
DarkBlue = Color(0x00008B, 1.0)
Red = Color(0xff0000, 1.0)
Black = Color(0x000000, 1.0)
Gold = Color(0xFFB90F, 1.0)
Brown = Color(0x9C661F, 1.0)

thinline = LineStyle(1, Black)
thickline = LineStyle(2,Black)

Head=RectangleAsset(82, 80, thinline, Tan)
Eye1=RectangleAsset(15,20, thinline, White)
Eye2=RectangleAsset(5, 10, thinline, Black)
Mouth=EllipseAsset(20,10, thinline, Black)
Tongue=EllipseAsset(8,5, thinline, Red)
Hair=RectangleAsset(2,8, thinline, Gold)
Body=PolygonAsset([(80,80),(80,200),(160,200),(160,80)], thickline, DarkBlue)
Pocket=RectangleAsset(20,20, thickline, DarkBlue)
Arm=RectangleAsset(30,100, thinline, Tan)
Sleve=RectangleAsset(36,40, thickline, DarkBlue)
Leg=RectangleAsset(35,110, thickline, Brown)
Shoe=CircleAsset(20, thickline, Black)


Sprite(Head, (80,80))
Sprite(Eye1, (95, 100))
Sprite(Eye1, (130, 100))
Sprite(Eye2, (95,100))
Sprite(Eye2, (140,110))
Sprite(Mouth, (100,130))
Sprite(Tongue, (113,140))
Sprite(Hair, (80,75))
Sprite(Hair, (85,75))
Sprite(Hair, (90,75))
Sprite(Hair, (95,75))
Sprite(Hair, (100,75))
Sprite(Hair, (105,75))
Sprite(Hair, (110,75))
Sprite(Hair, (115,75))
Sprite(Hair, (120,75))
Sprite(Hair, (125,75))
Sprite(Hair, (130,75))
Sprite(Hair, (135,75))
Sprite(Hair, (140,75))
Sprite(Hair, (145,75))
Sprite(Hair, (150,75))
Sprite(Hair, (155,75))
Sprite(Hair, (160,75))
Sprite(Body, (80,160))
Sprite(Pocket, (130,180))
Sprite(Arm, (163,160))
Sprite(Arm, (50,160))
Sprite(Sleve, (45,160))
Sprite(Sleve, (162,160))
Sprite(Leg, (83,280))
Sprite(Leg, (125,280))
Sprite(Shoe,(80,365))
Sprite(Shoe,(123,365))



# add your code here /\  /\  /\


myapp = App()
myapp.run()
