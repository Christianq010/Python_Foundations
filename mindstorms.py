import turtle

def draw_square():
  for i in range(1,5):
    some_turtle.forward(100)
    some_turtle.right(90)

def draw_art():    
  window = turtle.Screen()
  window.bgcolor("red")

  #Create the turtle Brad - Draw a Sqaure
  brad = turtle.Turtle()
  brad.shape("turtle")
  brad.color("yellow")
  brad.speed(2)
  draw_sqaure(brad)

  #Create the turtle Angie - Draw a Circle

  angie = turtle.Turtle()
  angie.shape("arrow")
  angie.color("blue")
  angie.circle(100)
  

  window.exitonclick()

draw_art()
