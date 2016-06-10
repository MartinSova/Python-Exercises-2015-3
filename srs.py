from follow import*

def srs_print(S, n, rules):
	"""This function prints the nth (argument) rewriting
	of the string S (argument) according to the rules given
	in the dictionary 'rules' (argument). If letter in S
	is not in rules, then it is rewritten but unchanged.
	"""
	if n == 0: # no rewritings done
		return S
	s = ""
	for letter in S:
		if letter in rules: # apply the rules to the specific letter (rewrite)
			s += srs_print(rules[letter], n-1, rules)
		else: # if letter is ignored by rules, do not modify for that letter
			s += srs_print(letter, n-1, rules)
		
	return s

def srs_draw(S, n, t, rules, step=2, angle=60):
	"""This function uses the nth (argument) rewriting
	of the string S (argument) according to the rules given
	in the dictionary 'rules' to draw with a turtle t, which
	interprets the string symbols according as:
	F: move forward by fixed distance defined by 'step' argument
	E: same effect as F
	L: turn left by a fixed angle, given by 'angle' argument
	R: turn right by fixed angle ('angle')
	Any other symbols are ignored by the turtle.
	"""
	follow(t, srs_print(S, n , rules), [], step, angle)


if __name__ == "__main__":

	rules = {'A':'AB', 'B':'A', 'E':'FLELF', 'F':'ERFRE'} 
	
	print(srs_print('A', 10, rules))

	bob = Turtle()

	srs_draw('E', 5, bob, rules)

	mainloop()


