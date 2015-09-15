from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
seafoam = Color(0x58FAD0, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
mediumline = LineStyle(3, black)
thickline = LineStyle(5, black)
redline = LineStyle(3, red)
# A graphics asset that represents a rectangle
rectangle = RectangleAsset(500, 200, mediumline, seafoam)
circle = CircleAsset(30, redline, blue)

# Now display a rectangle
Sprite(rectangle, (100, 200))
Sprite(circle, (500, 400))
Sprite(circle, (200, 400))

myapp = App()
myapp.run()
