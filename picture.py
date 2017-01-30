"""
picture.py
Author: <your name here>
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
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
yellow = Color(192-275-170, 1.0)
orange = Color(0xffbc53, 1.0)

thinline = LineStyle(1, black)
door = RectangleAsset(90, 170, thinline, yellow)
walls=RectangleAsset(300, 300, thinline, blue)
roof=PolygonAsset([(370,200),(730,200),(550,50)],thinline,black)
bottom=CircleAsset(110, thinline, white)
mid=CircleAsset(90, thinline, white)
top=CircleAsset(70, thinline, white)
nose=RectangleAsset(90, 170, thinline, yellow)

Sprite (walls,(400,200))
Sprite (door,(500,330))
Sprite (roof)
Sprite (bottom, (1000,530))
Sprite (mid,(1000,350))
Sprite (top,(1000,200))

myapp = App()
myapp.run()









# add your code here /\  /\  /\


myapp = App()
myapp.run()
