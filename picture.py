"""
picture.py
Author: Ella Edmonds
Credit: Your Tutorial and this link that was on it: http://brythonserver.github.io/ggame/#ggame.Color

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
red = Color(0xff0000, .7)
green = Color(0x00ff00, .7)
blue = Color(0x0000ff, .7)
black = Color(0x000000, 1)

#the window itself
thinline = LineStyle(1, black)
rect = RectangleAsset(400,5, thinline, black)
Sprite(rect, (20,40))

thinline = LineStyle(1, black)
rect = RectangleAsset(400,5, thinline, black)
Sprite(rect, (20,300))

thinline = LineStyle(1, black)
rect = RectangleAsset(5,265, thinline, black)
Sprite(rect, (20,40))

thinline = LineStyle(1, black)
rect = RectangleAsset(5,265, thinline, black)
Sprite(rect, (415,40))

thinline = LineStyle(1, black)
rect = RectangleAsset(5,265, thinline, black)
Sprite(rect, (217.5,40))

thinline = LineStyle(1, black)
rect = RectangleAsset(400,5, thinline, black)
Sprite(rect, (20,170))

#bluewindow

blue = Color(0x0000ff, 1)
thinline = LineStyle(3, blue)
rect = RectangleAsset(20,30, thinline, blue)
Sprite(rect, (25,45))

blue = Color(0x0000ff, .8)
thinline = LineStyle(3, blue)
rect = RectangleAsset(20,30, thinline, blue)
Sprite(rect, (65,45))

blue = Color(0x0000ff, .7)
thinline = LineStyle(3, blue)
rect = RectangleAsset(20,30, thinline, blue)
Sprite(rect, (105,45))

blue = Color(0x0000ff, .6)
thinline = LineStyle(3, blue)
rect = RectangleAsset(20,30, thinline, blue)
Sprite(rect, (145,45))

blue = Color(0x0000ff, .5)
thinline = LineStyle(3, blue)
rect = RectangleAsset(20,30, thinline, blue)
Sprite(rect, (185,45))
 
 #row two
 
blue = Color(0x0000ff, .8)
thinline = LineStyle(3, blue)
rect = RectangleAsset(20,30, thinline, blue)
Sprite(rect, (45,75))

blue = Color(0x0000ff, .7)
thinline = LineStyle(3, blue)
rect = RectangleAsset(20,30, thinline, blue)
Sprite(rect, (85,75))

blue = Color(0x0000ff, .6)
thinline = LineStyle(3, blue)
rect = RectangleAsset(20,30, thinline, blue)
Sprite(rect, (125,75))

blue = Color(0x0000ff, .5)
thinline = LineStyle(3, blue)
rect = RectangleAsset(20,30, thinline, blue)
Sprite(rect, (165,75))

blue = Color(0x0000ff, .4)
thinline = LineStyle(3, blue)
rect = RectangleAsset(12.5,30, thinline, blue)
Sprite(rect, (205,75))

#row three

blue = Color(0x0000ff, .8)
thinline = LineStyle(3, blue)
rect = RectangleAsset(20,30, thinline, blue)
Sprite(rect, (25,105))

blue = Color(0x0000ff, .7)
thinline = LineStyle(3, blue)
rect = RectangleAsset(20,30, thinline, blue)
Sprite(rect, (65,105))

blue = Color(0x0000ff, .6)
thinline = LineStyle(3, blue)
rect = RectangleAsset(20,30, thinline, blue)
Sprite(rect, (105,105))

blue = Color(0x0000ff, .5)
thinline = LineStyle(3, blue)
rect = RectangleAsset(20,30, thinline, blue)
Sprite(rect, (145,105))

blue = Color(0x0000ff, .4)
thinline = LineStyle(3, blue)
rect = RectangleAsset(20,30, thinline, blue)
Sprite(rect, (185,105))

#row four

blue = Color(0x0000ff, .7)
thinline = LineStyle(3, blue)
rect = RectangleAsset(20,30, thinline, blue)
Sprite(rect, (45,135))

blue = Color(0x0000ff, .6)
thinline = LineStyle(3, blue)
rect = RectangleAsset(20,30, thinline, blue)
Sprite(rect, (85,135))

blue = Color(0x0000ff, .5)
thinline = LineStyle(3, blue)
rect = RectangleAsset(20,30, thinline, blue)
Sprite(rect, (125,135))

blue = Color(0x0000ff, .4)
thinline = LineStyle(3, blue)
rect = RectangleAsset(20,30, thinline, blue)
Sprite(rect, (165,135))

blue = Color(0x0000ff, .3)
thinline = LineStyle(3, blue)
rect = RectangleAsset(12.5,30, thinline, blue)
Sprite(rect, (205,135))

#row 5

blue = Color(0x0000ff, .6)
thinline = LineStyle(3, blue)
rect = RectangleAsset(20,5, thinline, blue)
Sprite(rect, (25,165))

blue = Color(0x0000ff, .5)
thinline = LineStyle(3, blue)
rect = RectangleAsset(20,5, thinline, blue)
Sprite(rect, (65,165))

blue = Color(0x0000ff, .4)
thinline = LineStyle(3, blue)
rect = RectangleAsset(20,5, thinline, blue)
Sprite(rect, (105,165))

blue = Color(0x0000ff, .3)
thinline = LineStyle(3, blue)
rect = RectangleAsset(20,5, thinline, blue)
Sprite(rect, (145,165))

blue = Color(0x0000ff, .2)
thinline = LineStyle(3, blue)
rect = RectangleAsset(20,5, thinline, blue)
Sprite(rect, (185,165))

#red square

thinline = LineStyle(1, red)
ellipse = EllipseAsset(35, 10, thinline, red)
Sprite(ellipse, (146, 177))

thinline = LineStyle(1, red)
ellipse = EllipseAsset(35, 10, thinline, red)
Sprite(ellipse, (85.5, 177))

thinline = LineStyle(1, red)
ellipse = EllipseAsset(35, 10, thinline, red)
Sprite(ellipse, (26, 177))

thinline = LineStyle(1, red)
ellipse = EllipseAsset(35, 10, thinline, red)
Sprite(ellipse, (146, 201))

thinline = LineStyle(1, red)
ellipse = EllipseAsset(35, 10, thinline, red)
Sprite(ellipse, (85.5, 201))

thinline = LineStyle(1, red)
ellipse = EllipseAsset(35, 10, thinline, red)
Sprite(ellipse, (26, 201))

thinline = LineStyle(1, red)
ellipse = EllipseAsset(35, 10, thinline, red)
Sprite(ellipse, (146, 226))

thinline = LineStyle(1, red)
ellipse = EllipseAsset(35, 10, thinline, red)
Sprite(ellipse, (85.5, 226))

thinline = LineStyle(1, red)
ellipse = EllipseAsset(35, 10, thinline, red)
Sprite(ellipse, (26, 226))

thinline = LineStyle(1, red)
ellipse = EllipseAsset(35, 10, thinline, red)
Sprite(ellipse, (146, 251))

thinline = LineStyle(1, red)
ellipse = EllipseAsset(35, 10, thinline, red)
Sprite(ellipse, (85.5, 251))

thinline = LineStyle(1, red)
ellipse = EllipseAsset(35, 10, thinline, red)
Sprite(ellipse, (26, 251))

thinline = LineStyle(1, red)
ellipse = EllipseAsset(35, 10, thinline, red)
Sprite(ellipse, (146, 276))

thinline = LineStyle(1, red)
ellipse = EllipseAsset(35, 10, thinline, red)
Sprite(ellipse, (85.5, 276))

thinline = LineStyle(1, red)
ellipse = EllipseAsset(35, 10, thinline, red)
Sprite(ellipse, (26, 276))

#green square

green = Color(0x00ff00, .7)
thinline = LineStyle(1, green)
polygon = PolygonAsset([(0, 0),(190,0),(95,125)], thinline, green)
Sprite(polygon, (223.5,175))

green = Color(0x00ff00, .3)
thinline = LineStyle(1, green)
polygon = PolygonAsset([(0, 0),(0,125),(95,125)], thinline, green)
Sprite(polygon, (223.5,175))

green = Color(0x00ff00, .3)
thinline = LineStyle(1, green)
polygon = PolygonAsset([(0, 0),(95,-125),(95,0)], thinline, green)
Sprite(polygon, (318.5,175))

#rawinbow

purple = Color(0xbfffff, .6)
thinline = LineStyle(1, purple)
circ = CircleAsset(22, thinline, purple)
Sprite(circ, (225,47))

purple = Color(0xffbffb, .8)
thinline = LineStyle(1, purple)
circ = CircleAsset(22, thinline, purple)
Sprite(circ, (273,47))

purple = Color(0xfbffbb, 1)
thinline = LineStyle(1, purple)
circ = CircleAsset(22, thinline, purple)
Sprite(circ, (321,47))

purple = Color(0xbbffbb, .8)
thinline = LineStyle(1, purple)
circ = CircleAsset(22, thinline, purple)
Sprite(circ, (369,47))

#row three

purple = Color(0xffbbfb, .7)
thinline = LineStyle(1, purple)
circ = CircleAsset(22, thinline, purple)
Sprite(circ, (225,124))

purple = Color(0xfbbfbb, .6)
thinline = LineStyle(1, purple)
circ = CircleAsset(22, thinline, purple)
Sprite(circ, (273,124))

purple = Color(0xbbbfbb, .4)
thinline = LineStyle(1, purple)
circ = CircleAsset(22, thinline, purple)
Sprite(circ, (321,124))

purple = Color(0xbbfbff, .9)
thinline = LineStyle(1, purple)
circ = CircleAsset(22, thinline, purple)
Sprite(circ, (369,124))

#row two

purple = Color(0xbfbbff, .3)
thinline = LineStyle(1, purple)
circ = CircleAsset(22, thinline, purple)
Sprite(circ, (249,85.5))

purple = Color(0xbbffff, .6)
thinline = LineStyle(1, purple)
circ = CircleAsset(22, thinline, purple)
Sprite(circ, (297,85.5))

purple = Color(0xbbbfff, .5)
thinline = LineStyle(1, purple)
circ = CircleAsset(22, thinline, purple)
Sprite(circ, (345,85.5))


# add your code here /\  /\  /\


myapp = App()
myapp.run()
