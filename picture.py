"""
picture.py
Author: maBottnn14
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
red = Color(0xff8080, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x6495ED, 1.0)
black = Color(0x000000, 1.0)
clearish = Color(0xE0FFFF, 1.0)
yellow = Color(0xFFFF00, 1.0)
brown = Color(0xB8860B, 1.0)
pink = Color(0xFFC0CB, 1.0)
Grey = Color(0xD3D3D3, 1.0)
thinline = LineStyle(1, black)
rectangle = RectangleAsset(1300, 1000, thinline, blue)
Sprite(rectangle)

# The grass
rectangle = RectangleAsset(13000, 350, thinline, green)
Sprite(rectangle, (0, 500))

# A nice house
rectangle = RectangleAsset(400, 300, thinline, red)
Sprite(rectangle, (450, 200))

# Window 1
circle = CircleAsset(40, thinline, clearish)
Sprite(circle, (490, 230))


# Window 2
circle = CircleAsset(40, thinline, clearish)
Sprite(circle, (720, 230))

# Door
rectangle = RectangleAsset(70, 120, thinline, brown)
Sprite(rectangle, (580, 380))

# Doorknob 
circle = CircleAsset(6, thinline, red)
Sprite(circle, (630, 420))

circle = CircleAsset(2, thinline, black)
Sprite(circle, (634, 424))

# The Sun
circle = CircleAsset(55, thinline, yellow)
Sprite(circle, (70, 30))


# flower 1
ellipse = EllipseAsset(10, 50, thinline, green)
Sprite(ellipse, (80, 400))

circle = CircleAsset(10, thinline, yellow)
Sprite(circle, (74, 400))

circle = CircleAsset(10, thinline, yellow)
Sprite(circle, (80, 385))

circle = CircleAsset(10, thinline, yellow)
Sprite(circle, (86, 400))


# flower 2
ellipse = EllipseAsset(10, 50, thinline, green)
Sprite(ellipse, (110, 400))

circle = CircleAsset(10, thinline, yellow)
Sprite(circle, (104, 400))

circle = CircleAsset(10, thinline, yellow)
Sprite(circle, (110, 385))

circle = CircleAsset(10, thinline, yellow)
Sprite(circle, (116, 400))


# flower 3
ellipse = EllipseAsset(10, 50, thinline, green)
Sprite(ellipse, (95, 400))

circle = CircleAsset(10, thinline, pink)
Sprite(circle, (89, 400))

circle = CircleAsset(10, thinline, pink)
Sprite(circle, (95, 385))

circle = CircleAsset(10, thinline, pink)
Sprite(circle, (101, 400))

# chimney
rectangle = RectangleAsset(40, 80, thinline, brown)
Sprite(rectangle, (800, 120))

# smoke from chimney
circle = CircleAsset(5, thinline, Grey)
Sprite(circle, (803, 100))

circle = CircleAsset(5, thinline, Grey)
Sprite(circle, (820, 90))

circle = CircleAsset(5, thinline, Grey)
Sprite(circle, (806, 80))

circle = CircleAsset(5, thinline, Grey)
Sprite(circle, (825, 105))
#
circle = CircleAsset(5, thinline, Grey)
Sprite(circle, (820, 65))

circle = CircleAsset(5, thinline, Grey)
Sprite(circle, (806, 55))
#
circle = CircleAsset(5, thinline, Grey)
Sprite(circle, (820, 40))

circle = CircleAsset(5, thinline, Grey)
Sprite(circle, (806, 30))

circle = CircleAsset(5, thinline, Grey)
Sprite(circle, (825, 55))
#
circle = CircleAsset(5, thinline, Grey)
Sprite(circle, (803, 50))

circle = CircleAsset(5, thinline, Grey)
Sprite(circle, (820, 15))

circle = CircleAsset(5, thinline, Grey)
Sprite(circle, (806, 5))

circle = CircleAsset(5, thinline, Grey)
Sprite(circle, (825, 30))

# roof
roof = PolygonAsset(((-200, 0),(0,-120),(200,0),(-200,0)), thinline, black)
Sprite(roof,(450,80))



# add your code here /\  /\  /\


myapp = App()
myapp.run()
