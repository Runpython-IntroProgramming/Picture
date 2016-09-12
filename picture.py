"""
picture.py
Author: Johannes Testorf
Credit: none

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
yellow = Color(0xffff00, 1.0)
brown = Color(0xf4a460, 1.0)

thinline = LineStyle(1, black)

sky=RectangleAsset(100000000000000,1000000000000, thinline ,blue)
sun=CircleAsset(500, thinline, yellow)
grass= RectangleAsset(100000000,1000, thinline ,green)  
pond= EllipseAsset(200,100,thinline, blue)
Fish= PolygonAsset([(500,700),(550,750),(580,700)],thinline,red)
Smoke= CircleAsset(100,thinline,black)
Sprite(sky)
Sprite(sun)
Sprite(grass, (0,600))
Sprite(pond, (500, 750))
Sprite(Fish)
Sprite(Smoke, (200,600))
# add your code here /\  /\  /\


myapp = App()
myapp.run()
