from follow import*
from srs import srs_print

def srs_draw(S, n, t, rules, stack=[], step=4, angle=25):
	"""This function uses the nth (argument) rewriting
	of the string S (argument) according to the rules given
	in the dictionary 'rules' to draw with a turtle t, which
	interprets the string symbols according as:
	F: move forward by fixed distance defined by 'step' argument
	E: same effect as F
	L: turn left by a fixed angle, given by 'angle' argument
	R: turn right by fixed angle ('angle')
	[: add the location and heading to the 'stack' argument
	]: retrieve location and heading from stack
	Any other symbols are ignored by the turtle.
	"""

	t.left(90)
	# initial angle of turtle changed so desired image is printed upwards
	penup(t)
	t.sety(-350)
	pendown(t)
	# initial y-position of turtle changed so drawn fern can be seen in the window
	
	follow(t, srs_print(S, n , rules), stack, step, angle)



if __name__ == "__main__":

	rules = {'A':'FL[[A]RA]RF[RFA]LA', 'F': 'FF'}

	bob = Turtle()

	srs_draw('A', 6, bob, rules)

	mainloop()
