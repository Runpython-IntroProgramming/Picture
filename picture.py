"""
picture.py
Author: Katie Naughton
Credit: I worked alone. 

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

# 4 colors, no transparency
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

#line
thinline=LineStyle(1, black)
#rectangle representation
rectangle=RectangleAsset (250, 250, thinline, black)
#rectangle 
Sprite(rectangle,(350, 150))

rectangle2=RectangleAsset (1010, 200, thinline, green)
Sprite(rectangle2, (0, 400))

rectangle3=RectangleAsset (100, 100, thinline, red)
Sprite(rectangle3, (400, 300))

ellipse=EllipseAsset (20, 20, thinline, blue)
Sprite(ellipse, (425, 325))









myapp = App()
myapp.run()
