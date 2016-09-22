"""
picture.py
Author: <xNimbleNavigatorx>
Credit: <notkezar>

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
green = Color(0x6B8E23, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)

mediumline = LineStyle(5, black)
eraserline = LineStyle(5, white)

eye1 = EllipseAsset(80, 50, mediumline, white)
eyerim = EllipseAsset(90, 65, mediumline, green)
rectangleface = RectangleAsset(500, 500, mediumline, green)
lip = RectangleAsset(366, 40, mediumline, red)
rectangel = RectangleAsset(50, 30, mediumline, white)
pupil = CircleAsset(30, mediumline, black)
top = PolygonAsset([(308, 96), (425, 10), (550, 60), (675, 10), (792, 96)], mediumline, green)
chin = PolygonAsset([(700, 600), (900, 600), (900, 500)], eraserline, white)

Sprite(rectangleface, (400, 100))
Sprite(lip, (533, 420))
Sprite(lip, (533, 460))

Sprite(eyerim, (830, 244))
Sprite(eyerim, (700, 244))

Sprite(eye1, (830, 244))
Sprite(eye1, (700, 244))

Sprite(pupil, (845, 260))
Sprite(pupil, (715, 260))

Sprite(top, (100, 0))
Sprite(chin, (0, 0))

# add your code here /\  /\  /\

myapp = App()
myapp.run()