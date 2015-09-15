"""
picture.py
Author: Anoushka Alavilli
Credit: html website, Sarah Dunbar, Dina

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
white= Color(0xffffff, 1.0)
black= Color(0x000000, 1.0)
blackroof= Color(0x000000, 1.0)
redchimney= Color (0xB40404,1.0)
windowblue= Color(0xCEE3F6, 0.5)
gray= Color(0xD8D8D8, 1.0)
thinline = LineStyle(1, black)
noline= LineStyle(0, black)
rectanglehouse = RectangleAsset(500, 500, thinline, white)
Sprite(rectanglehouse, (550,250))
triangle= PolygonAsset([(550, 250), (1050, 250), (800, 50)], thinline, blackroof)
Sprite(triangle)
chimney= RectangleAsset(68, 150, thinline, redchimney)
Sprite(chimney, (550, 100))
window1= RectangleAsset(125, 125, thinline, windowblue)
Sprite(window1, (600, 300))
window2= RectangleAsset(125, 125, thinline, windowblue)
Sprite(window2, (875, 300))
windowvertline1= RectangleAsset(7, 125, thinline, white)
Sprite(windowvertline1, (659, 300))
windowvertline2= RectangleAsset(7, 125, thinline, white)
Sprite(windowvertline2, (934, 300))
windowhorizline1= RectangleAsset(125, 7, thinline, white)
Sprite(windowhorizline1, (600, 359))
windowhorizline2= RectangleAsset(125, 7, thinline, white)
Sprite(windowhorizline2, (875, 359))
door= RectangleAsset(125, 200, thinline, redchimney)
Sprite(door, (738, 550))
doorknob= EllipseAsset(8, 8, thinline, black)
Sprite(doorknob, (842, 650))
smoke= CircleAsset(30, noline, gray)
Sprite(smoke, (584, 65))
Sprite(smoke, (555, 58))
Sprite(smoke, (555, 40))
Sprite(smoke, (540, 40))
Sprite(smoke, (500, 60))


# add your code here /\  /\  /\


myapp = App()
myapp.run()
