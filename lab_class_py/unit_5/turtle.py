

# square 

# import turtle

# turtle.showturtle()

# for i in range(4) :
#     turtle.forward(50)
#     turtle.right(90)


# turtle.done()









# star

# import turtle 

# turtle.showturtle()

# for i in range(5) :
#     turtle.forward(100)
#     turtle.right(144)

# turtle.done()









# hexagon

# import turtle

# turtle.showturtle()

# for i in range(6) :
#     turtle.forward(50)
#     turtle.left(60)










# square spiral


# import turtle

# window = turtle.Screen()

# window.bgcolor("light green")

# window.title("Turtle")

# turtle.color("blue")

# def sqrfunc(size) :
#     for i in range(4) :
#         turtle.fd(size)
#         turtle.left(90)
#         size = size - 5
# sqrfunc(146) 
# sqrfunc(126) 
# sqrfunc(106) 
# sqrfunc(86) 
# sqrfunc(66) 
# sqrfunc(46) 
# sqrfunc(26)


# turtle.done()















# # Olympic rings


# import turtle

# turtle.shape('turtle')

# turtle.width(10)

# start_pos_x = -180
# start_pos_y = 60

# # problem in black
# colors = ['blue', 'green', 'yellow', 'red', 'black']

# for i in range(5) :
#     turtle.color(colors[i])
#     turtle.circle(50)
#     turtle.penup()

#     if (i == 1) :
#         start_pos_y = 0
#     else :
#         start_pos_y = 60

#     if (i == 4) :
#         start_pos_x = 60


#     turtle.setposition(start_pos_x, start_pos_y)
#     start_pos_x += 60 
    
#     turtle.pendown()











# olympic rings 

# import turtle
# turtle.shape('turtle')
# turtle.width(10)

# turtle.color('blue')
# turtle.circle(50)
# turtle.penup()
# turtle.setposition(-120, 0)
# turtle.pendown()
# turtle.color('green')
# turtle.circle(50)
# turtle.penup()
# turtle.setposition(60,60)
# turtle.pendown()
# turtle.color('yellow')
# turtle.circle(50)
# turtle.penup()
# turtle.setposition(-60, 60)
# turtle.pendown()
# turtle.color('red')
# turtle.circle(50)
# turtle.penup()
# turtle.setposition(-180, 60)
# turtle.pendown()
# turtle.color('black')
# turtle.circle(50)
# turtle.done()














# import turtle
# turtle.showturtle()
# turtle.fillcolor('red')
# turtle.color('red')
# turtle.begin_fill()
# turtle.circle(100)
# turtle.end_fill()
# turtle.penup()
# turtle.goto(-70, 100)
# turtle.write("JECRC University", font = 10)
# turtle.bgcolor('pink')
# turtle.done()













# import turtle
# turtle.speed(0)
# turtle.showturtle()
# turtle.penup()
# turtle.right(90)
# for i in range(1, 11) :
#     turtle.write(i)
#     turtle.forward(20)
# turtle.done()












# import turtle
# # turtle.speed(0)
# start_x = -200
# start_y = 200
# x = start_x
# y = start_y

# for i in range(1, 6) :
#     for j in range(i) :
#         turtle.penup()
#         turtle.goto(x, y)
#         # turtle.pendown()
#         turtle.write("* ", font = ("arial", 12, "bold"))
#         x += 20
#     x = start_x
#     y -= 30

# turtle.hideturtle()
# turtle.done()











import turtle
turtle.showturtle()
turtle.penup()
for i in range(1, 11) :
    turtle.write(i)
    turtle.forward(20)
turtle.done()


import turtle 
turtle.showturtle() 
turtle.fillcolor('pink')
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
turtle.penup() 
turtle.goto(0, 50)
turtle.write('Khushi') 
turtle.undo()
turtle.goto(-25, 50)
turtle.write('Khushi', font =("jokerman", 15))  


# program to write the counting


'''
for i in range(11) :
    print(i)

    
'''