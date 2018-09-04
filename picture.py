"""
picture.py
Author: Emma Tysinger
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
red=Color(0xff0000,1.0)
pink=Color(0xFFB6C1,1.0)
yellow=Color(0xFFFF00,1.0)
green=Color(0x66CD00,0.5)
black=Color(0x000000,1.0)
brown=Color(0x8B4513,1.0)

thinline=LineStyle(1,black)
thinline2=LineStyle(1,green)
barn=PolygonAsset([(25,0),(50,20),(50,70),(0,70),(0,20),(25,0)],thinline,red)
sun=CircleAsset(10,thinline,yellow)
door=RectangleAsset(10,20,thinline,brown)
pigbody=EllipseAsset(15,10,thinline,pink)
pighead=CircleAsset(6,thinline,pink)
pigleg=RectangleAsset(2,12,thinline,pink)
grass=RectangleAsset(150,15,thinline2,green)

Sprite(barn,(100,40))
Sprite(sun)
Sprite(door,(115,90))
Sprite(door,(125,90))
Sprite(pigbody,(40,80))
Sprite(pighead,(60,70))
Sprite(pigleg,(43,98))
Sprite(pigleg,(50,98))
Sprite(pigleg,(56,98))
Sprite(pigleg,(64,98))
Sprite(grass,(0,110))

print("Welcome to the farm!")

# add your code here /\  /\  /\


myapp = App()
myapp.run()
