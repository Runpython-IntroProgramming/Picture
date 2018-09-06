"""
picture.py
Author: Olivia Simon
Credit: I used the how to ue ggame links; and https://htmlcolorcodes.com/ to find the color codes.

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

# colors
skin = Color(0x4BADC1)
white = Color(0xffffff)
gill = Color(ox44CA83)
#mouth
tongue = Color(0x16A085)
black = Color(0x000000)
#Lines
thinLine = LineStyle(1, black)
#Head
skull = CircleAsset()
jaw = RectangleAsset()
#Eyes
leye = CircleAsset(20,20,thinline,white)
reye = CircleAsset(20,20,thinline,white)
lpupil = CircleAsset(5,5,thinline, black)
rpupil = CircleAsset(5,5,thinline,black)
#Mouth
left = EllipseAsset(50,20,thinline,black)
right = EllipseAsset(50,20,thinline,black)
mouthTongue = EllipseAsset(,thinline,tongue)
gills1 = RectangleAsset(30,10,thinline, gill)
gills2 = RectangleAsset(30,10,thinline,gill)
gills3 = RectangleAsset(30,10,thinline,gill)
gills4 = RectangleAsset(30,10,thinline,gill)
#Sprites
Sprite(gills1)

# add your code here /\  /\  /\


myapp = App()
myapp.run()
