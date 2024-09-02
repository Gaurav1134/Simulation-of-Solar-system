import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")

class Planet:
    def __init__(self, name, radius, distance, color, speed):
        self.name = name
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.shapesize(radius)
        self.turtle.color(color)
        self.distance = distance
        self.speed = speed
        self.angle = 0

    def move(self):
        self.angle += self.speed
        x = self.distance * math.cos(math.radians(self.angle))
        y = self.distance * math.sin(math.radians(self.angle))
        self.turtle.goto(x, y)

# Create the sun
sun = turtle.Turtle()
sun.shape("circle")
sun.shapesize(2)
sun.color("yellow")

# Define planets with their characteristics
planets = [
    Planet("Mercury", 0.3, 50, "gray", 6),
    Planet("Venus", 0.5, 100, "orange", 5),
    Planet("Earth", 0.6, 150, "blue", 4),
    Planet("Mars", 0.4, 200, "red", 3.5),
    Planet("Jupiter", 1.2, 300, "tan", 2),
    Planet("Saturn", 1, 400, "goldenrod", 1.5),
    Planet("Uranus", 0.8, 500, "light blue", 1.2),
    Planet("Neptune", 0.8, 600, "blue", 1),
    Planet("Pluto", 0.2, 700, "light gray", 0.8),  # Pluto
]

# Main animation loop
while True:
    for planet in planets:
        planet.move()
    sun.goto(0, 0)  # Keep the sun at the center

    screen.update()  # Update the screen

# turtle.done()  # Uncomment this if running as a script
