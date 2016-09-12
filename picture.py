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

thinline = LineStyle(1, hotpink)

rec = RectangleAsset(169,169, thinline, Aquamarine)
#poly = PolygonAsset([
Sprite(rec, (500, 400))
#Sprite(

# add your code here /\  /\  /\


myapp = App()
myapp.run()
