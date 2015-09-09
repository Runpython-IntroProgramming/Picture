"""
picture.py
Author: Adam Pikielny
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
# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

#linestyle
line=LineStyle(3,black)

#graphics asset
rectangle=RectangleAsset(500, 500, line, green)
eye=CircleAsset(50, line, green)
mouth=EllipseAsset(150,50,line,red)

#Sprite
Sprite(rectangle, (100,100))
Sprite(eye, (250,200))
Sprite(eye, (450,200))
Sprite(mouth, (350,400))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
