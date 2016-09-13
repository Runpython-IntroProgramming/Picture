"""
picture.py
Author: John Warhold
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
blueviolet = Color(0x8a2be2, 1.0)
hotpink = Color(0xff69b4, 1.0)
Aquamarine =Color(0x7fffd4, 1.0)
brown = Color(0xcd5c5c, 1.0)
green = Color(0x00ff7f, .5)
thist = Color(0xd8bfd8, 1.0)
thinline = LineStyle(1, hotpink)

rec = RectangleAsset(169,169, thinline, Aquamarine)
poly = PolygonAsset([(500,400), (669,400), (584.5, 350), (500, 400)], thinline, blueviolet)
circ = CircleAsset(67, thinline, hotpink) 
rek = RectangleAsset(50,100, thinline, brown)
lol = CircleAsset(100, thinline, green)
rrr = EllipseAsset(75,25, thinline, thist)
rekt = RectangleAsset(12,24, thinline, brown)
Sprite(rec, (500, 400))
Sprite(poly)
Sprite(circ, (67,67))
Sprite(rek, (800,469 ))
Sprite(lol, (825,390))
Sprite(rrr, (500,200))
Sprite(rekt, (444,400))
# add your code here /\  /\  /\


myapp = App()
myapp.run()
