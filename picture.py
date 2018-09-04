"""
picture.py
Author: Emma Dunbar
Credit: I used wikipedia to find more hexadecimal codes

Assignment: picture

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
green=Color(0x00ff00,1.0)
blue=Color(0x0000ff,1.0)
black=Color(0x000000,1.0)
yellow=Color(0xffff00,1.0)
brown=Color(0x8b4513,1.0)
lightblue=Color(0xADD8E6,1.0)
white=Color(0xffffff,1.0)

tline=LineStyle(1, black)

sun=CircleAsset(30,tline,yellow)
house=RectangleAsset(80,80,tline,blue)
roof=PolygonAsset([(0,0),(40,-40),(80,0)],tline,red)
grass=EllipseAsset(2000,300,tline,green)
door=RectangleAsset(20,40,tline,brown)
sky=RectangleAsset(2000,2000,tline,lightblue)
cloud=EllipseAsset(100,40,tline,white)
bhouse=RectangleAsset(200,200,tline,white)
broof=PolygonAsset([(0,0),(100,-100),(200,0)],tline,red)
bdoor=RectangleAsset(50,100,tline,brown)


Sprite(sky)
Sprite(grass,(-500,200))
Sprite(sun,(600,60))
Sprite(house,(60,300))
Sprite(roof,(60,260))
Sprite(door,(90,340))
Sprite(cloud,(100,40))
Sprite(bhouse,(500,290))
Sprite(broof,(500,190))
Sprite(bdoor,(550,390))




# add your code here /\  /\  /\


myapp = App()
myapp.run()
