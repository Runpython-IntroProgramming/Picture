from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
print("I'm going to draw you some cars and trucks!!")

Lgreen = Color (0x7CFC00, 0.95)
turqo = Color (0x40E0D0, 0.99)
Orange = Color (0xFF8600, 1)
black = Color (0x000000, 0.85)
purp = Color (0x68228B, 0.9)
brn = Color (0x5C3317, 0.9)
clearsh = Color (0xD1EEEE, 0.55)
dkgr = Color (0x474747, 0.82)
medgr = Color (0x525C65, 0.79)
wit = Color (0xFCFCFC, 1)

bl_line = LineStyle(3, black)
thinline = LineStyle(1, black)

car1 = RectangleAsset(120, 70, bl_line, Orange)
car2 = RectangleAsset(125, 60, bl_line, Lgreen)
wheel = CircleAsset (12, bl_line, black)
road = RectangleAsset(1200, 280, thinline, dkgr)
window = CircleAsset (10, thinline, clearsh)
stripe = RectangleAsset(990, 10, thinline, wit)
truck = RectangleAsset(210, 80, bl_line, purp)
trkfrt = PolygonAsset ([(10,0), (80,0), (80,90), (0,91), (10,0)], thinline, brn)
bgwheels = CircleAsset(16, bl_line, medgr)
bgwinw = RectangleAsset(50, 55, thinline, clearsh)

Sprite(road, (15,1))
Sprite(stripe, (117,108))
myapp = App()
myapp.run()

import picture
picture.my2app.run()

Sprite(car1, (680,40))
Sprite(car2, (820,40))
Sprite(wheel, (700,115))
Sprite(wheel, (780,115))
Sprite(wheel, (840,100))
Sprite(wheel, (920,100))
Sprite(window, (700,60))
Sprite(window, (740,60))
Sprite(window, (780,60))
Sprite(window, (840,65))
Sprite(window, (882,65))
Sprite(window, (925,66))
Sprite(truck, (850,136))
Sprite(trkfrt, (770,130))
Sprite(bgwheels, (840,215))
Sprite(bgwheels, (790,215))
Sprite(bgwheels, (960,212))
Sprite(bgwheels, (1025,212))
Sprite(bgwinw, (795,140))


my3app = App()
my3app.run()
