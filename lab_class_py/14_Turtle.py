# 01.) Write a program to display the hexagon.

import turtle
turtle.showturtle()
for i in range(6) :
    turtle.forward(30)
    turtle.left(60)





# 02.) Write a program to create a circle with specifications as: 
#  (a) Fill circle with red color 
#  (b) Display the text message “JECRC University” inside the circle.  


import turtle 
turtle.showturtle() 
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.penup() 
turtle.goto(-70, 100)
turtle.write("JECRC University", font = 10) 
turtle.bgcolor('pink')






# 03.) Write a program to display 1 to 10 numbers in the Turtle graphics window .

import turtle
turtle.showturtle()
turtle.penup()
turtle.right(90)
for i in range(1, 11) :
    turtle.write(i) 
    turtle.forward(20)







# 04.) Write a program to display the patterns of stars in the Turtle graphics window as shown. 
'''
 * 
 * * 
 * * *
 * * * * 
 * * * * *
'''
 

import turtle 
# turtle.speed(0)
start_x = -200
start_y = 200
x = start_x
y = start_y

for i in range(1, 6) :
    for j in range(i) :
            turtle.penup()
            turtle.goto(x, y)
            # turtle.pendown()
            turtle.write("* ", font = ("Arial", 12, "normal"))
            x += 20
    x = start_x
    y -= 30

turtle.hideturtle()



turtle.done()