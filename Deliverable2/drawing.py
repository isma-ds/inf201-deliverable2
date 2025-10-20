# drawing.py
# INF201 – Deliverable 2 (Weeks 43–44)
# Author: Isma Sohail
# Source: Based on lecture 8 and instructor example

import matplotlib
matplotlib.use("TkAgg")  # helps macOS show the window
from turtleplotlib import Turtle
import matplotlib.pyplot as plt
import math


class Rectangle:
    def __init__(self, lower_left, upper_right, color="blue", linewidth=1):
        self.ll = lower_left
        self.ur = upper_right
        self.color = color
        self.lw = linewidth

    def area(self):
        return (self.ur[0] - self.ll[0]) * (self.ur[1] - self.ll[1])

    def info(self):
        print(f"Rectangle(ll: {self.ll}, ur: {self.ur}), color={self.color}, lw={self.lw}")

    def draw(self, turtle):
        turtle.teleport(self.ll)
        turtle.setheading(0)
        turtle.color(self.color)
        turtle.width(self.lw)
        width = self.ur[0] - self.ll[0]
        height = self.ur[1] - self.ll[1]
        for d in [width, height, width, height]:
            turtle.forward(d)
            turtle.left(90)


class Triangle:
    def __init__(self, *points, color="blue", linewidth=1):
        self.points = points
        self.color = color
        self.lw = linewidth

    def area(self):
        return None

    def info(self):
        print(f"Triangle{self.points}, color={self.color}, lw={self.lw}")

    def draw(self, turtle):
        turtle.color(self.color)
        turtle.width(self.lw)
        turtle.teleport(self.points[0])
        for p in self.points[1:]:
            turtle.goto(p)
        turtle.goto(self.points[0])


class Circle:
    def __init__(self, center, radius, color="blue", linewidth=1):
        assert radius >= 0, "Radius must be positive"
        self.ctr = center
        self.rad = radius
        self.color = color
        self.lw = linewidth

    def area(self):
        return math.pi * self.rad ** 2

    def info(self):
        print(f"Circle(center: {self.ctr}, radius: {self.rad}), color={self.color}, lw={self.lw}")

    def draw(self, turtle):
        N = 180
        seg_len = 2 * math.pi * self.rad / N
        turn = 360 / N
        turtle.color(self.color)
        turtle.width(self.lw)
        start = (self.ctr[0] + self.rad, self.ctr[1])
        turtle.teleport(start)
        turtle.setheading(90 + turn / 2)
        for _ in range(N):
            turtle.forward(seg_len)
            turtle.left(turn)
        turtle.goto(start)


if __name__ == "__main__":
    shapes = [
        Rectangle((0, 0), (150, 200), color="red"),
        Rectangle((100, 50), (200, 210), linewidth=2),
        Rectangle((-100, -100), (0, 0), color="black", linewidth=3),
        Triangle((-50, -50), (90, -20), (0, 70), color="darkgreen"),
        Rectangle((-50, -150), (150, 50), color="black", linewidth=1),
        Circle((50, -50), 100, color="purple", linewidth=2)
    ]

    for s in shapes:
        s.info()

    t = Turtle(interactive=False)
    for s in shapes:
        s.draw(t)

    plt.show()
