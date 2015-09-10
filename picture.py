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
http://www.w3schools.com/tags/ref_colorpicker.asp
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
red=Color(0xff0000,1.0)
green=Color(0x00ff00,1.0)
blue=Color(0x006699,1.0)
black=Color(0x331A00,1.0)
yellow=Color(0xFF9900, 0.75)
linea=LineStyle(1,yellow)
sun=CircleAsset(600,linea,yellow)
Sprite(sun,(590,600))
lineb=LineStyle(1,blue)
ocean=RectangleAsset(1500,200,lineb,blue) 
Sprite(ocean,(0,500))

#add location
# add your code here /\  /\  /\


myapp = App()
myapp.run()
