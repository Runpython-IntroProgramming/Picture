"""
picture.py
Author: Christopher Lee
Credit: https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics


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
#Colors
red = Color(0xff0000, 1.0)
green = Color(0xff000, 1.0)
blue = Color(0x5499C7, 1.0)
yellow = Color(0xffff00, 1.0)
brown = Color(0x6F4017, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
orange = Color(0xE67E22, 1.0)
#Line
line = LineStyle(1,black)
linegreen = LineStyle(1, green)
linebrown = LineStyle(1, brown)
#Asset
rectangle = RectangleAsset(100, 100, line, blue)
circle = CircleAsset(50, line, yellow)
ellipse = EllipseAsset(200, 100, line, blue)
poly = PolygonAsset([(0,300), (0,400), (2000, 400), (2000, 300)], linegreen, green)
dirt = PolygonAsset([(0, 300), (0, 2000), (2000, 2000), (2000, 300)], linebrown, brown)
tri = PolygonAsset([(0,100), (50, 0), (100, 100)], line, orange)
window = RectangleAsset(25, 25, line, white)
fish = EllipseAsset(15, 10, line, orange)
tail = PolygonAsset([(0,0), (5, 10), (5, -10)], line, orange)
eye = CircleAsset(2, line, black)
#Sprite
Sprite(poly, (0, 300)) #Land
Sprite(circle) #Sun
Sprite(dirt, (0, 400))

#House 1
Sprite(rectangle, (300, 200)) #house
Sprite(tri, (300, 100)) #roof
Sprite(window, (310, 250))
Sprite(window, (365, 250))
#House 2
Sprite(rectangle, (500, 200))
Sprite(tri, (500, 100))
Sprite(window, (510, 250))
Sprite(window,(565, 250))
#
Sprite(ellipse, (500, 500))
Sprite(fish, (600, 600))
Sprite(tail, (630, 600))
Sprite(eye, (605, 605))
# add your code here /\  /\  /\


myapp = App()
myapp.run()
