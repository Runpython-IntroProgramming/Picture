"""
picture.py
Author: johari
Credit:http://brythonserver.github.io/ggame/#ggame.Color, megsnyder

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
red = Color(0xff0000, 0.5)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
tan = Color(0xffbb33, .3)
darkertan = Color(0xffbb33, .26)
hazel = Color(0xbbaa44, 1.0)
pink = Color(0xbb0000,0.5)
brown = Color(0x997733, .5)

thinline = LineStyle(1,black) 
lessline = LineStyle(.01, black) 

head = EllipseAsset(150,200, thinline, tan) 
eyeball = CircleAsset(10, thinline, hazel) 
pupil = CircleAsset(3, thinline, black)
nose = PolygonAsset([(50,120), (40,225), (60,225), (50,120)], lessline, darkertan)

lip = EllipseAsset(40, 10, thinline, pink) 
lipline = RectangleAsset(80, 2, lessline, black)

hairright = PolygonAsset([(100,220), (120,525), (290,525), (150,220)], thinline, brown)
hairleft = PolygonAsset([(150,220), (150,525), (0,525), (100,220)], thinline, brown)

#Hair
Sprite(hairright, (500, 50))
Sprite(hairleft, (250,50))

Sprite(head, (300,50))

#Eyes
Sprite(eyeball, (373, 200)) 
Sprite(pupil, (380, 207))
Sprite(eyeball, (502, 200))
Sprite(pupil, (509, 207))

Sprite(nose, (440,220))

#Lips
Sprite(lip, (411, 360))
Sprite(lipline, (411,370))

#Hair
Sprite(hairright, (500, 50))
Sprite(hairleft, (250,50))
# add your code here /\  /\  /\


myapp = App()
myapp.run()
