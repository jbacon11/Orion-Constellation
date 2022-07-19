# The Orion Constellation Program
#Jeremy Bargy
#Jan. 31, 2020
# 
# This program draws the stars of the Orion constellation,
# the names of the stars, and the constellation lines using turtle graphics.

import turtle

# Set the window size.
turtle.setup(500, 600)

# Setup the turtle.
turtle.penup()
turtle.hideturtle()

# Create named constrants fo the star coordinates.
Left_Shoulder_X = -70
Left_Shoulder_Y = 200

Right_Shoulder_X = 80
Right_Shoulder_Y = 180

Left_Beltstar_X = -40
Left_Beltstar_Y = -20

Middle_Beltstar_X = 0
Middle_Beltstar_Y = 0

Right_Beltstar_X = 40
Right_Beltstar_Y = 20

Left_Knee_X = -90
Left_Knee_Y = -180

Right_Knee_X = 120
Right_Knee_Y = -140

# Draw the stars.
turtle.goto(Left_Shoulder_X, Left_Shoulder_Y)    # Left Shoulder
turtle.dot()
turtle.goto(Right_Shoulder_X, Right_Shoulder_Y)    # Right Shoulder
turtle.dot()
turtle.goto(Left_Beltstar_X, Left_Beltstar_Y)   # Left Belt star
turtle.dot()
turtle.goto(Middle_Beltstar_X, Middle_Beltstar_Y)   # Middle Belt Star
turtle.dot()
turtle.goto(Right_Beltstar_X, Right_Beltstar_Y) #Right Belt Star
turtle.dot()
turtle.goto(Left_Knee_X, Left_Knee_Y)   # Left Knee
turtle.dot()
turtle.goto(Right_Knee_X, Right_Knee_Y) # Right Knee
turtle.dot()

# Display the star names
turtle.goto(Left_Shoulder_X, Left_Shoulder_Y)   # Left Shoulder
turtle.write('Betegeuse')
turtle.goto(Right_Shoulder_X, Right_Shoulder_Y) # Right Shoulder
turtle.write('Meissa')
turtle.goto(Left_Beltstar_X, Left_Beltstar_Y)   # Left Belt star
turtle.write('Alnitak')
turtle.goto(Middle_Beltstar_X, Middle_Beltstar_Y)   # Middle Belt star
turtle.write('Alnilam')
turtle.goto(Right_Beltstar_X, Right_Beltstar_Y) # Right Belt star
turtle.write('Mintaka')
turtle.goto(Left_Knee_X, Left_Knee_Y)   # Left Knee
turtle.write('Saiph')
turtle.goto(Right_Knee_X, Right_Knee_Y) # RIght Knee
turtle.write('Rigel')

# Draw a line from the left shoulder to left belt star
turtle.goto(Left_Shoulder_X, Left_Shoulder_Y)
turtle.pendown()
turtle.goto(Left_Beltstar_X, Left_Beltstar_Y)
turtle.penup()

#Draw a line from the right shoulder to right belt star
turtle.goto(Right_Shoulder_X, Right_Shoulder_Y)
turtle.pendown()
turtle.goto(Right_Beltstar_X, Right_Beltstar_Y)
turtle.penup()

# Draw a line from the left belt star to the middle belt star
turtle.goto(Left_Beltstar_X, Left_Beltstar_Y)
turtle.pendown()
turtle.goto(Middle_Beltstar_X, Middle_Beltstar_Y)
turtle.penup()

# Draw a line from the middle belt star to the right belt star
turtle.goto(Middle_Beltstar_X, Middle_Beltstar_Y)
turtle.pendown()
turtle.goto(Right_Beltstar_X, Right_Beltstar_Y)
turtle.penup()

# Draw a line from the left belt star to the left knee
turtle.goto(Left_Beltstar_X, Left_Beltstar_Y)
turtle.pendown()
turtle.goto(Left_Knee_X, Left_Knee_Y)
turtle.penup()

# Draw a line from the right belt star to the right knee
turtle.goto(Right_Beltstar_X, Right_Beltstar_Y)
turtle.pendown()
turtle.goto(Right_Knee_X, Right_Knee_Y)

# Keep the Window open. (NOT NECESSARY WITH IDLE.)
turtle.done()
