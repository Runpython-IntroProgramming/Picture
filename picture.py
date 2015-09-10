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
x=1366
y=768
red=Color(0xff0000,1.0)
green=Color(0x00ff00,1.0)
blue=Color(0x006699,1.0)
lbrown=Color(0x996633,1.0)
dbrown=Color(0x1F0F00,1.0)
yellow=Color(0xFF9900,0.75)
white=Color(0xFFFFFF,1.0)
black=Color(0x000000,1.0)
linea=LineStyle(1,yellow)
sun=CircleAsset(600,linea,yellow)
Sprite(sun,(592,600))
lineb=LineStyle(1,blue)
ocean=RectangleAsset(1500,500,lineb,blue) 
Sprite(ocean,(0,500))
linee=LineStyle(1,white)
sail=EllipseAsset(40,5,linee,white)
Sprite(sail,(680,610))
lined=LineStyle(1,dbrown)
mast=RectangleAsset(2,50,lined,dbrown)
Sprite(mast,(680,595))
linec=LineStyle(1,lbrown)
hull=PolygonAsset([(703,680),(723,640),(643,640),(663,680),(703,680)],linec,lbrown)
Sprite(hull)
linef=LineStyle(2,black)
cloud=CircleAsset(20,linef,white)
Sprite(cloud,(60,70))
Sprite(cloud,(60,50))
Sprite(cloud,(50,60))
Sprite(cloud,(70,60))
Sprite(cloud,(60,60))
line=PolygonAsset([(60,95),(50,200),(60,95)],linef,black)
Sprite(line)
#add location
# add your code here /\  /\  /\


myapp = App()
myapp.run()
