"""
picture.py
Author: Milo Wilcox
Credit: http://www.w3schools.com/tags/ref_colorpicker.asp

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
red=Color(0xff0000,1.0)
green=Color(0x00ff00,1.0)
blue=Color(0x006699,0.5)
black=Color(0x000000,1.0)
brown= #insert brown hexadecimal here
yellow=Color(0xFF9900, 0.75)
linea=LineStyle(1,yellow)
sun=CircleAsset(750,linea,yellow)
Sprite(sun,(760,800))
lineb=LineStyle(1,blue)
ocean=RectangleAsset(1500,200,lineb,blue) 
Sprite(ocean,(0,1000)
linec=(1,black)
hull+PolygonAsset(760,100,500,760,linec,brown) #fix size
Sprite(hull,()) #add location
# add your code here /\  /\  /\


myapp = App()
myapp.run()
