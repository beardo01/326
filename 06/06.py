"""
This program draws a toothpick grid depending on the parameters that it is given.

Oliver Reid - 2569385
"""

##
# Imports
##
from Tkinter import *
import sys

# Dir: True is vert, False is horz

##
# A recursive method that draws our toothpick grid onto the window.
#
# @param repeats The number of times we are going to add new toothpicks.
# @param length The size that each successive set of toothpicks should be set to, relative of the last set.
##
def drawToothPicks(window, repeats, linelength, ratio, dir, sx, sy, ex, ey):
	# Base case to break out of recursion
	if repeats == 0:
		return

	# Get our new x and y coordinants
	if dir:
		l1x1 = sx
		l1y1 = sy + linelength/2
		l1x2 = sx
		l1y2 = sy - linelength/2
		l2x1 = ex
		l2y1 = ey + linelength/2
		l2x2 = ex
		l2y2 = ey - linelength/2
	else:
		l1x1 = sx + linelength/2
		l1y1 = sy
		l1x2 = sx - linelength/2
		l1y2 = sy
		l2x1 = ex + linelength /2
		l2y1 = ey 
		l2x2 = ex - linelength/2
		l2y2 = ey

	# Do the drawing
	window.create_line(l1x1, l1y1, l1x2, l1y2)
	window.create_line(l2x1, l2y1, l2x2, l2y2)

	# Recursively call drawToothpicks
	if dir:
		drawToothPicks(window, repeats - 1, linelength * ratio, ratio, False, l1x1, l1y1, l1x2, l1y2)
		drawToothPicks(window, repeats - 1, linelength * ratio, ratio, False, l2x1, l2y1, l2x2, l2y2)
	else:
		drawToothPicks(window, repeats - 1, linelength * ratio, ratio, True, l1x1, l1y1, l1x2, l1y2)
		drawToothPicks(window, repeats - 1, linelength * ratio, ratio, True, l2x1, l2y1, l2x2, l2y2)


##
# Main method
##
repeats = int(sys.argv[1])
if len(sys.argv) > 2:
	ratio = float(sys.argv[2])
else:
	ratio = 1

# Create the canvas
master = Tk()
window = Canvas(master)

# Draw our base line and call our recursive function
window.create_line(-50, 0, 50, 0)
drawToothPicks(window, repeats, 100 * ratio, ratio, True, -50, 0, 50, 0)

#Size our window properly
padding = 20
width = 100 + padding
height = 5 + padding
for i in range(1, repeats + 1):
	if i % 2 == 0:
		width += 100 * (ratio**i)
	else:
		height += 100 * (ratio**i)

window.xview_scroll(int(width), "units")
window.yview_scroll(int(height), "units")
window.config(width=width, height=height, scrollregion=((0 - width/2), (0 - height/2), (0 + width/2), (0 + height/2)))

window.pack()

# Draw our window
mainloop()