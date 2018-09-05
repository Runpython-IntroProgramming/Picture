"""
picture.py
Author: Eamon
Credit: Github

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
#from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/

from ggame import App, ImageAsset, Sprite
# Create a displayed object at 100,100 using an image asset
Sprite(ImageAsset("Small-mario.png"), (100,100))
# Create the app, with a 500x500 pixel stage
app = App(500,500)  
# Run the app
app.run()


# add your code here /\  /\  /\


#myapp = App()
#myapp.run()
