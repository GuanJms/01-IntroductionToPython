"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Shengjun Guan.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
samuel= rg.SimpleTurtle()
james = rg.SimpleTurtle()
samuel.pen = rg.Pen('midnight blue', 3)
samuel.speed = 40
james.speed = 200
size = 180
for k in range(6):
    samuel.draw_square(size)
    samuel.pen_up()
    samuel.right(40)
    samuel.left(30)
    samuel.right(30)
    samuel.backward(40)
    samuel.pen_down()
    size = size - 20

james = rg.SimpleTurtle('triangle')
james.pen = rg.Pen('magenta', 1)
size2 = 20
window.tracer(2)
james.left(130)
for k in range(6):
    for g in range(6):
        james.forward(10)
        james.draw_square(size)
    james.backward(30)
window.close_on_mouse_click()





