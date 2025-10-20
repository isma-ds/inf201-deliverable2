# drawing.py
# INF201 – Deliverable 2 (Weeks 43–44)
# Author: Isma Sohail
# Source: Simplified version using matplotlib only (works on all systems)

import matplotlib

matplotlib.use("TkAgg")  # ensures it runs on macOS
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
        print(
            f"Rectangle(ll: {self.ll}, ur: {self.ur}), color={self.color}, lw={self.lw}"
        )

    def draw(self, ax):
        width = self.ur[0] - self.ll[0]
        height = self.ur[1] - self.ll[1]
        rect = plt.Rectangle(
            self.ll, width, height, fill=False, color=self.color, linewidth=self.lw
        )
        ax.add_patch(rect)


class Triangle:
    def __init__(self, *points, color="blue", linewidth=1):
        self.points = points
        self.color = color
        self.lw = linewidth

    def area(self):
        return None

    def info(self):
        print(f"Triangle{self.points}, color={self.color}, lw={self.lw}")

    def draw(self, ax):
        x = [p[0] for p in self.points] + [self.points[0][0]]
        y = [p[1] for p in self.points] + [self.points[0][1]]
        ax.plot(x, y, color=self.color, linewidth=self.lw)


class Circle:
    def __init__(self, center, radius, color="blue", linewidth=1):
        self.ctr = center
        self.rad = radius
        self.color = color
        self.lw = linewidth

    def area(self):
        return math.pi * self.rad**2

    def info(self):
        print(
            f"Circle(center: {self.ctr}, radius: {self.rad}), color={self.color}, lw={self.lw}"
        )

    def draw(self, ax):
        circ = plt.Circle(
            self.ctr, self.rad, fill=False, color=self.color, linewidth=self.lw
        )
        ax.add_patch(circ)


if __name__ == "__main__":
    shapes = [
        Rectangle((0, 0), (150, 200), color="red"),
        Rectangle((100, 50), (200, 210), linewidth=2),
        Rectangle((-100, -100), (0, 0), color="black", linewidth=3),
        Triangle((-50, -50), (90, -20), (0, 70), color="darkgreen"),
        Rectangle((-50, -150), (150, 50), color="black", linewidth=1),
        Circle((50, -50), 100, color="purple", linewidth=2),
    ]

    for s in shapes:
        s.info()

    fig, ax = plt.subplots()
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(-200, 300)
    ax.set_ylim(-200, 300)
    ax.set_title("INF201 – Deliverable 2 Shapes")

    for s in shapes:
        s.draw(ax)

    plt.show()
