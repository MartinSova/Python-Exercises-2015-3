from exturtle import forward, left, right, mainloop, Turtle, heading, position, goto, setheading, penup, pendown

def follow(t, S, stack, step=10, angle=90):
    """
    Cause the turtle, t, to interpret the symbols in the string S.

    Arguments:
    t     -- the turtle
    S     -- string to be interpreted 
    step  -- size of a step in pixels
    angle -- angle to turn through

    Commands:
    E, F  -- draw forward by step
    L     -- turn left by angle
    R     -- turn right by angle
    
    All other symbolss are ignored.
    """
 

    for char in S:

        if char == 'E' or char == 'F':
            forward(t, step)
        elif char == 'L':
            left(t, angle)
        elif char == 'R':
            right(t, angle)
        elif char == '[':
# both position and heading values are appended
            stack.append(position(t))
            stack.append(heading(t))
        elif char == ']':
                penup(t)
                goto(t, stack.pop(-2))
# position always appended first, so placed before heading in stack
                setheading(t, stack.pop(-1))
                pendown(t)
