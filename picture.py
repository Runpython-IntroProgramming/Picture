"""
picture.py
Author: Eamon
Credit: Github, Nintendo Wikia - Fandom (mario image)

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
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
brown = Color(0x654321, 1.0)
thinline = LineStyle(1, black)
thinbrown = LineStyle(1, brown)
medline = LineStyle(2, black)
thickgreen = LineStyle(7, green)
thingreen = LineStyle(1, green)
ground = RectangleAsset(500, 20, thinline, brown)
Sprite((ground), (0, 220))
pipe1 = RectangleAsset(30, 50, thingreen, green)
Sprite((pipe1), (350, 180))
pipe2 = EllipseAsset(25, 10, thickgreen, black)
Sprite((pipe2), (337.5, 170))
block = RectangleAsset(15, 15, thinline, brown)
Sprite((block), (200, 100))
Sprite((block), (230, 100))
Sprite((block), (215, 100))
#goomba = 
# add your code here \/  \/  \/


Sprite(ImageAsset("Small-mariogood5.png"), (100,200))
app = App(500,500)  
app.run()


# add your code here /\  /\  /\



