# names = ["artin","abtin", "nikan", "sara"]
# print(names)
# print(names[0])
# print(names[-1])
# print(names[:2])

# new_name = input("enter a name: ")
# names.remove(new_name)
# del names[0]
# names.pop(1)
# print(names)


# numbers = []
# for i in range(3):
#     new_number =  int(input("enter a number: "))
#     numbers.append(new_number)
# print(numbers)
# print(sum(numbers))



# names = []

# while True:
#     n = input("enter a name: ")
#     if n[0] == "a" or n[0] ==  "A":
#         names.append(n)
#     if input("Do you want to quit (y or n): ") == "y":
#         break

# print(names)





# even_numbers = []
# odd_numbers = []

# for i in range(5):
#     n = int(input("enter a number: "))
#     if n % 2 == 0:
#         even_numbers.append(n)
#     else:
#         odd_numbers.append(n)

# print("even numbers:", even_numbers)
# print("odd numbers:", odd_numbers)

# print("sum of evens:", sum(even_numbers))
# print("sum of odds:", sum(odd_numbers))


import turtle
turtle.register_shape("apple.gif")
turtle.shape("apple.gif") # 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
turtle.color("red")
turtle.shapesize(2)
turtle.pensize(2)

sides = int(turtle.textinput("sides", "how many sides you want?"))

turtle.begin_fill()
for i in range(sides):
    turtle.forward(100)
    turtle.left(360/sides)
turtle.end_fill()
turtle.penup()
turtle.goto(-300, 200)
turtle.stamp()
turtle.goto(300, 200)
turtle.stamp()
turtle.goto(300, -200)
turtle.stamp()
turtle.done()