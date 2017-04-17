"""
picture.py
Author: Ethan Adner
Credit: Hex color codes

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

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
orange = Color(0xff7400, 1.0)
beige = Color(0xffffd8, 1.0)
white = Color(0xffffff, 1.0)

noline = LineStyle(2 , black)
nlu = LineStyle(5 , blue)
thickline = LineStyle(5 , red)
thickline2 = LineStyle(5, orange)
circle = CircleAsset(10, noline, beige)


poly = PolygonAsset([(20,20), (30,40), (50,160), (20,100)], thickline, red)
portal1 = EllipseAsset(40, 10, nlu, white)
rectum = RectangleAsset(40, 60, thickline2, orange)
portal2 = EllipseAsset(40, 10, thickline2, white)
rectum2 = RectangleAsset(40, 30, thickline2, orange)
legs = RectangleAsset(5, 30, thickline2, orange)
#arm1 =
#arm2 = 

arm1 = Sprite(legs, (130, 480))
arm2 = Sprite(legs, (30, 480))
arm1.rotation=-1
arm2.rotation=1
#arm1.roation=.5

Sprite(circle, (80, 478)) 
Sprite(poly, (90, 530))
Sprite(portal1, (80, 150))
Sprite(portal2, (80, 550))
Sprite(rectum, (60, 490))
Sprite(rectum2, (60, 150))
Sprite(legs, (60, 180))
Sprite(legs, (95, 180))


# add your code here /\  /\  /\


myapp = App()
myapp.run()

