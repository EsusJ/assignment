# Name: Zhang Haoxin
# Assignment One

from turtle import *


# Task A - based on drawing.py
def draw_pinwheel():
    setup(500, 500)
    title("Triangle Pinwheel")
    bgcolor("white")
    speed(5)
    pensize(2)

    # stick
    pencolor("gray")
    penup()
    goto(0, -190)
    pendown()
    goto(0, 0)

    # four triangles with different colors and sizes
    colors = ["red", "gold", "blue", "green"]
    length = 90
    for i in range(4):
        pencolor(colors[i])
        fillcolor(colors[i])
        begin_fill()
        for j in range(3):
            fd(length)
            rt(120)
        end_fill()
        rt(90)
        length = length + 15

    hideturtle()
    print("Click the drawing window to close it.")
    exitonclick()


# Task B - input loop based on maths.py
def qa_bot():
    print("------ Welcome to the question answering system -----")
    print("Keywords: HKU, robot, jetson, ai, human")
    print("Enter 0 to stop.")

    while True:
        question = input("Your question is: ").lower().strip()
        if question == "0":
            print("Questions finished.")
            break
        elif question == "hku":
            print("Bot: HKU stands for the University of Hong Kong.")
        elif question == "robot":
            print("Bot: A robot is a machine that can carry out tasks.")
        elif question == "jetson":
            print("Bot: Jetson Nano is an AI computer.")
        elif question == "ai":
            print("Bot: AI means Artificial Intelligence.")
        elif question == "human":
            print("Bot: A human is a person.")
        else:
            print("Bot: Sorry, I don't understand.")


# Task C - terminal calculator
def calc():
    print("Simple Calculator")
    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        op = input("Choose operation (+, -, *, /): ").strip()

        if op == "+":
            print("Result:", n1 + n2)
        elif op == "-":
            print("Result:", n1 - n2)
        elif op == "*":
            print("Result:", n1 * n2)
        elif op == "/":
            if n2 == 0:
                print("Cannot divide by zero.")
            else:
                print("Result:", n1 / n2)
        else:
            print("Invalid operation.")
    except ValueError:
        print("Please use numbers as the input.")


print("----- Welcome to the assignment system ----")
a = input("---- Please select what you want to run:\n"
          " (1 for pinwheel, 2 for QA bot, 3 for calculator)\n"
          "Your selection is: ")
if a == "1":
    draw_pinwheel()
elif a == "2":
    qa_bot()
elif a == "3":
    calc()
else:
    print("Please input the value in [1, 2, 3]")
