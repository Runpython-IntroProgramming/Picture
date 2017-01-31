"""
picture.py
Author: Abby
Credit: None

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
from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

lightblue= Color(0x00bfff, 1.0)
green=Color(0x2e8b57,1.0)
brown=Color(0x8b4513, .8)
purple=Color(0x9370db, 1.0)
black = Color(0x000000, 1.0)
blue=Color(0x0000f,1.0)

line=LineStyle(1,black)

Petal=EllipseAsset(50,20,line, lightblue)
petal2=EllipseAsset(20,50,line, lightblue)
Circle=CircleAsset(30, line, purple)
stem=RectangleAsset(5,100,line,green)
pot=PolygonAsset([(300,500), (500,500), (450,600), (350,600), (300,500)], line, brown)

Sprite(Circle, (375,300))
Sprite(Petal, (300,300))
Sprite(Petal, (450,300))
Sprite(petal2, (380,225))
Sprite(stem, (380,400))
Sprite(petal2, (380,375))
petal3=Sprite(petal2,(315,245))
petal3.rotation=3.14/4
petal4=Sprite(petal2,(430,355))
petal4.rotation=3.14/4
petal5=Sprite(petal,(430,245))
petal5.rotation=3.14/4
petal6=Sprite(petal,(315,355))
petal6.rotation=3.14/4

# add your code here /\  /\  /\


myapp = App()
myapp.run()
