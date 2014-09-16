import tkinter
from tkinter import font

HEIGHT = 500
WIDTH = 500
AXIS_SIZE = 50


def draw(points, x_label, y_label):
	Window = tkinter.Tk()
	f = font.Font(root=Window, family='Arial', size=10)
	c = tkinter.Canvas(Window, height=HEIGHT, width=WIDTH, bg="white")
	c.pack()
	
	X_max = 0
	Y_max = 0
	
	for point in points:
		if point[0] > X_max:
			X_max = point[0]
		if point[1] > Y_max:
			Y_max = point[1]
	
	X_ratio = (WIDTH-AXIS_SIZE) / X_max * 0.95
	Y_ratio = (HEIGHT-AXIS_SIZE) / Y_max * 0.95
	
	#Draw axis
	c.create_line(AXIS_SIZE, HEIGHT-AXIS_SIZE, WIDTH, HEIGHT-AXIS_SIZE)
	c.create_line(AXIS_SIZE, HEIGHT-AXIS_SIZE, AXIS_SIZE, 0)
	c.create_text(250, HEIGHT-10, text=x_label ,font=f)
	c.create_text(10, 250, text=y_label ,font=f, width=1)
	
	#Draw points
	for point in points:
		plot_point(c, point[0]*X_ratio, point[1]*Y_ratio, 2)
	
	Window.mainloop()


def plot_point(c, x, y, s):
	c.create_rectangle(
		x - s + AXIS_SIZE,
		HEIGHT - (y-s) - AXIS_SIZE,
		x + s + AXIS_SIZE,
		HEIGHT - (y+s) - AXIS_SIZE,
		fill="black"
	)



#points = [(0,0), (1,1), (2,4), (3,9), (4,16)]
#draw(points, "X axis", "Y axis")
