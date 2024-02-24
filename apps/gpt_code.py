import turtle

# Создаем экземпляр класса Turtle
star = turtle.Turtle()

# Задаем цвет и толщину линии
star.color("black")
star.pensize(3)

# Рисуем пятиконечную звезду
for _ in range(5):
    star.forward(100)
    star.right(144)

# Закрываем окно при клике
turtle.exitonclick()
