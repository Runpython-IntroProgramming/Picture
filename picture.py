"""
picture.py
Author: Eric Goodney
Credit: Peers

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
blue = Color(0x000ff, 1.0)
black = Color(0x000000, 1.0)

thinline = LineStyle(1, black)
rectangle = RectangleAsset(250,250, thinline, red)
triangle = PolygonAsset([(200,0), (325,-100),  (450,0)], thinline, blue)
rectangle2 = RectangleAsset(50,100, thinline, black)
window1 = RectangleAsset(40,90, thinline, red)
window2 = RectangleAsset(40,90, thinline, red)
thing1 = EllipseAsset(40,40, thinline, green)
thing2 = CircleAsset(25, thinline, black)


Sprite(rectangle,(400,200))
Sprite(triangle,(400,100))
Sprite(rectangle2,(500,350))
Sprite(window1,(430,210))
Sprite(window2,(570,210))
Sprite(thing1,(480,210))
Sprite(thing2,(500,140))

# add your code here /\  /\  /\

myapp = App()
myapp.run()



