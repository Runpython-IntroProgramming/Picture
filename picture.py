"""
picture.py
Author: Tess Snyder
Credit: http://www.colorpicker.com/ , 

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
black1 = Color(0x000000, .5)
black2 = Color(0x000000, 1.0)
purple = Color(0xA642C9, 1.0)
white = Color(0xFFFFFF, 1.0)
yellowish = Color(0xF1F2D5, 1.0)

thinline = LineStyle(1, black)

sky = RectangleAsset(800,400, thinline, black1)
moon = CircleAsset(40, thinline, yellowish)
water = RectangleAsset(800, 400, thinline, blue)
fish = EllipseAsset(50,20, thinline, red)
fin = PolygonAsset([(40,470),(50,440),(60,470)], thinline, red)
eye = CircleAsset(2, thinline, black2)
star = CircleAsset(2, thinline, white)

Sprite(sky, (0,0))
Sprite(water, (0, 400))
Sprite(moon, (200, 50))
Sprite(fish, (50, 480))
Sprite(fin, (0,0))
Sprite(eye, (80, 480))
Sprite(star, (400, 40))
Sprite(star, (100, 80))
Sprite(star, (50, 200))
# add your code here /\  /\  /\


myapp = App()
myapp.run()
