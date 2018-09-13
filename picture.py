"""
picture.py
Author: Joseph Goff
Credit: None

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

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 0.0)
blue = Color(0x0000ff, 0.5)
black = Color(0x000000, 1.0)

thinline = LineStyle(1, black)
thickline = LineStyle(4, black)
thiccline = LineStyle(23, black)

lefttire = CircleAsset(48, thiccline, green)
Sprite(lefttire, (300, 370))

righttire = CircleAsset(48, thiccline, green)
Sprite(righttire, (670, 370))

leftbottom = RectangleAsset(80, 5, thinline, black)
rightbottom = RectangleAsset(57, 5, thinline, black)
midbottom = RectangleAsset(280, 5, thinline, black)
Sprite(leftbottom, (220, 410))
Sprite(rightbottom, (788, 410)) 
Sprite(midbottom, (400, 410)) 

leftside = RectangleAsset(5, 110, thinline, black)
Sprite(leftside, (220, 300))

rightside = RectangleAsset(5, 110, thinline, black)
Sprite(rightside, (840, 300))

lefttop = RectangleAsset(130, 5, thinline, black)
Sprite(lefttop, (220, 300))

righttop = RectangleAsset(130, 5, thinline, black)
Sprite(righttop, (710, 300))

windshield = RectangleAsset(8, 8, thinline, blue)
Sprite(windshield, (710, 295)) 
Sprite(windshield, (705, 290))
Sprite(windshield, (700, 285)) 
Sprite(windshield, (695, 280)) 
Sprite(windshield, (690, 275)) 
Sprite(windshield, (685, 270)) 
Sprite(windshield, (680, 265)) 
Sprite(windshield, (675, 260)) 
Sprite(windshield, (670, 255)) 
Sprite(windshield, (665, 250)) 
Sprite(windshield, (660, 245)) 
Sprite(windshield, (655, 240)) 
Sprite(windshield, (650, 235)) 
Sprite(windshield, (645, 230)) 
Sprite(windshield, (640, 225)) 

backglass = RectangleAsset(8, 8, thinline, blue)
Sprite(backglass, (345, 295)) 
Sprite(backglass, (350, 290))
Sprite(backglass, (355, 285)) 
Sprite(backglass, (360, 280)) 
Sprite(backglass, (365, 275)) 
Sprite(backglass, (370, 270)) 
Sprite(backglass, (375, 265)) 
Sprite(backglass, (380, 260)) 
Sprite(backglass, (385, 255)) 
Sprite(backglass, (390, 250)) 
Sprite(backglass, (395, 245)) 
Sprite(backglass, (400, 240)) 
Sprite(backglass, (405, 235)) 
Sprite(backglass, (410, 230)) 
Sprite(backglass, (415, 225)) 

top = RectangleAsset(220, 5, thinline, black)
Sprite(top, (420, 220))

top2 = RectangleAsset(200, 5, thinline, black)
Sprite(top2, (430, 230))

mid = RectangleAsset(330, 5, thinline, black)
Sprite(mid, (365, 300))

midline = RectangleAsset(5, 70, thinline, black)
Sprite(midline, (530, 230))

windshield2 = RectangleAsset(5, 5, thinline, black)
Sprite(windshield2, (690, 295)) 
Sprite(windshield2, (685, 290))
Sprite(windshield2, (680, 285)) 
Sprite(windshield2, (675, 280)) 
Sprite(windshield2, (670, 275)) 
Sprite(windshield2, (665, 270)) 
Sprite(windshield2, (660, 265)) 
Sprite(windshield2, (655, 260)) 
Sprite(windshield2, (650, 255)) 
Sprite(windshield2, (645, 250)) 
Sprite(windshield2, (640, 245)) 
Sprite(windshield2, (635, 240)) 
Sprite(windshield2, (630, 235)) 

backglass2 = RectangleAsset(5, 5, thinline, black)
Sprite(backglass2, (365, 295)) 
Sprite(backglass2, (370, 290))
Sprite(backglass2, (375, 285)) 
Sprite(backglass2, (380, 280)) 
Sprite(backglass2, (385, 275)) 
Sprite(backglass2, (390, 270)) 
Sprite(backglass2, (395, 265)) 
Sprite(backglass2, (400, 260)) 
Sprite(backglass2, (405, 255)) 
Sprite(backglass2, (410, 250)) 
Sprite(backglass2, (415, 245)) 
Sprite(backglass2, (420, 240)) 
Sprite(backglass2, (425, 235)) 

steeringwheel = EllipseAsset(8, 19, thickline, red)
Sprite(steeringwheel, (617, 260))

Sprite(windshield2, (650, 295)) 
Sprite(windshield2, (645, 290))
Sprite(windshield2, (640, 285)) 
Sprite(windshield2, (635, 280)) 

seat1 = RectangleAsset(15, 35, thickline, green)
Sprite(seat1, (550, 265))

seat2 = RectangleAsset(15, 35, thickline, green)
Sprite(seat2, (420, 265))
# add your code here /\  /\  /\


myapp = App()
myapp.run()
