import tkinter
from tkinter import font
from math import log10, floor


HEIGHT = 500
WIDTH = 500
AXIS_SIZE = 70


def draw(points, x_label, y_label, functions=None):
	'''The function object needs a get_point metheod the takes an x vaule and returns a y'''
	Window = tkinter.Tk()
	f = font.Font(root=Window, family='Arial', size=10)
	c = tkinter.Canvas(Window, height=HEIGHT, width=WIDTH, bg="white", bd=0)
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
	r = (X_ratio, Y_ratio)
	
	#Draw axis
	c.create_line(AXIS_SIZE, HEIGHT-AXIS_SIZE, WIDTH, HEIGHT-AXIS_SIZE)
	c.create_line(AXIS_SIZE, HEIGHT-AXIS_SIZE, AXIS_SIZE, 0)
	c.create_text(250, HEIGHT-10, text=x_label ,font=f)
	c.create_text(10, 250, text=y_label ,font=f, width=1)
	
	draw_scale(c, (X_max,Y_max), f)
	
	#Draw points
	if len(points) > 1:
		for point in points:
			point = (point[0]*r[0], point[1]*r[1])
			plot_point(c, point, 2)
	
	#Draw functions
	if functions != None:
		for function in functions:
			draw_function(c, function, r)
	
	Window.mainloop()

def SigFig(x, n):
	if x == 0: return 0.0;
	return round(x, -int(floor(log10(x))) + (n - 1))


def plot_point(c, point, s, colour="black"):
	#The Y axis must be inverted
	c.create_rectangle(
		point[0] - s + AXIS_SIZE ,
		HEIGHT - (point[1]-s) - AXIS_SIZE,
		point[0] + s + AXIS_SIZE,
		HEIGHT - (point[1]+s) - AXIS_SIZE,
		fill = colour
	)


def plot_line(c, p_new, p_old, colour="black"):
	#The Y axis must be inverted
	if p_old != None:
		c.create_line(
			p_new[0 ]+ AXIS_SIZE,
			HEIGHT - p_new[1] - AXIS_SIZE,
			p_old[0] + AXIS_SIZE,
			HEIGHT - p_old[1] - AXIS_SIZE,
			fill=colour
		)
	return p_new


def draw_scale(c, point, f):
	xinc = (WIDTH - AXIS_SIZE)/10
	yinc = (HEIGHT - AXIS_SIZE)/10
	
	for i in range(10):
		x = AXIS_SIZE + xinc*i
		y = AXIS_SIZE + yinc*i
		
		x_num = str(SigFig(point[0]/10*i, 2))
		y_num = str(SigFig(point[1]/10*i, 2))
		
		c.create_line(
			x,
			HEIGHT - AXIS_SIZE,
			x,
			HEIGHT - AXIS_SIZE*0.9,
		)
		c.create_line(
			AXIS_SIZE,
			HEIGHT - y,
		AXIS_SIZE*0.9,
			HEIGHT - y,
		)
		
		c.create_text(x, HEIGHT - AXIS_SIZE*0.75, text=x_num ,font=f)
		c.create_text(AXIS_SIZE*0.6, HEIGHT - y, text=y_num ,font=f)
	


def draw_function(c, function, r):
	x_points = list(range(0, WIDTH))
	old_point = None
	for x in x_points:
		y = function.get_point(x / r[0])*r[1]
		old_point = plot_line(c, (x, y), old_point, colour="red")
