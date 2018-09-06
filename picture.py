"""
picture.py
Author: Claire Adner
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

# colors
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, .50)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
light_blue = Color(0x0000ff, .05)
orange = Color(0xffa500, 1.0)

# thin black line
thinline = LineStyle(1, black)

# background
ground_snow = RectangleAsset(1500, 275, thinline, blue)

#the snowman body 
base = CircleAsset (80, thinline, light_blue)
middle = CircleAsset (50, thinline, light_blue)
head = CircleAsset (40, thinline, light_blue)
nose = PolygonAsset([(0,0), (0,15), (30,12)], thinline, orange)
eyes = CircleAsset (5, thinline, black)
arm_left = PolygonAsset([(0,0), (15,5), (100,90), (100,100)], thinline, black)
arm_right = PolygonAsset([(210,0), (195,5), (100,90), (100,100)], thinline, black)

#accessories 
hat_base = RectangleAsset(80, 20, thinline, black)
hat_top = EllipseAsset(25, 28, thinline, black)
buttons = CircleAsset(5, thinline, black)

# display
Sprite (ground_snow, (0,400))
Sprite (base, (350, 240))
Sprite (middle, (380, 140))
Sprite (head, (390, 60))
Sprite (nose, (430,100))
Sprite (eyes, (410, 80))
Sprite (eyes, (440, 80))
Sprite (arm_left, (280,100))
Sprite (arm_right, (480,100))
Sprite (hat_base, (390,40))
Sprite (hat_top, (405,4))
Sprite (buttons, (425,200))
Sprite (buttons, (425,180))
Sprite (buttons, (425,160))


# add your code here /\  /\  /\


myapp = App()
myapp.run()
