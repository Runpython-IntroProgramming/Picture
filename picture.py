"""
picture.py
Author: Billy B
Credit: <list sources used, if any>

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

from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
# A graphics asset that represents a rectangle
rectangle = RectangleAsset(300, 60, thinline, blue)

# Now display a rectangle
Sprite(rectangle, (650, 300))

circle =  CircleAsset(50, thinline, blue)

Sprite(circle, (800,250))

rectangle2 = RectangleAsset(100, 60, thinline, blue)

Sprite(rectangle2, (750, 360))

rectangle3=RectangleAsset(150, 60, thinline, blue)

Sprite(rectangle3, (725, 420))

rectangle4=RectangleAsset(50, 100, thinline, blue)

Sprite(rectangle4, (725, 480))

Sprite(rectangle4, (825, 480))

mouth=EllipseAsset(20, 10, thinline, green)

eyes=CircleAsset(5, thinline, green)

Sprite(eyes, (785, 240))

Sprite(eyes, (815, 240))

Sprite(mouth, (800, 275))

hat=PolygonAsset([(750, 210),(850, 210),(850, 190), (825, 190), (825, 50), (775, 50), (775, 190), (750, 190)], thinline, black)

Sprite(hat, (0,0))
myapp = App()
myapp.run()
from ggame import App
myapp = App()


# add your code here /\  /\  /\


myapp = App()
myapp.run()
