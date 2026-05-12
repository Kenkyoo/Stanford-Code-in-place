"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
THIS_BIG = 144
CENTER_X = 160
CENTER_Y = 160

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_rectangle(
		CENTER_X - THIS_BIG / 2,
		CENTER_Y - THIS_BIG / 2,
		CENTER_X + THIS_BIG / 2,
		CENTER_Y + THIS_BIG / 2
	)

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
