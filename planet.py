import turtle
import random
import math

class SolarSystem:
    def __init__(self, width, height):
        self.thesun = None
        self.planets = []
        self.ssturtle = turtle.Turtle()
        self.ssturtle.hideturtle()
        self.ssscreen = turtle.Screen()
        self.ssscreen.bgcolor("black")  # Set the background color to black

        self.ssscreen.setworldcoordinates(-width / 2.0, -height / 2.0, width / 2.0, height / 2.0)
        self.ssscreen.tracer(50)
        
        # Draw the starry background
        self.draw_stars()

        self.label = turtle.Turtle()
        self.label.hideturtle()
        self.label.penup()
        self.label.goto(-width / 2.0 + 10, height / 2.0 - 30)
        self.label.color("white")
        self.label.write("", align="left", font=("Arial", 16, "normal"))
        self.check_hover()

    def draw_stars(self):
        star_turtle = turtle.Turtle()
        star_turtle.hideturtle()
        star_turtle.penup()
        star_turtle.color("white")
        for _ in range(100):  # Adjust the number of stars here
            x = random.uniform(-1, 1) * self.ssscreen.window_width() / 2
            y = random.uniform(-1, 1) * self.ssscreen.window_height() / 2
            star_turtle.goto(x, y)
            star_turtle.dot(random.randint(2, 4))  # Random size for stars
        star_turtle.hideturtle()

    def addPlanet(self, aplanet):
        self.planets.append(aplanet)

    def addSun(self, asun):
        self.thesun = asun

    def showPlanets(self):
        for aplanet in self.planets:
            print(aplanet)

    def showPlanetDetails(self, planet):
        details = f"Name: {planet.getName()}\nRadius: {planet.getRadius()} km\nMass: {planet.getMass()} kg\nDistance: {planet.getDistance()} AU"
        self.label.clear()
        self.label.write(details, align="left", font=("Arial", 16, "normal"))

    def check_hover(self):
        x, y = turtle.getcanvas().winfo_pointerx(), turtle.getcanvas().winfo_pointery()
        screen_x, screen_y = self.ssscreen.cv.winfo_pointerx(), self.ssscreen.cv.winfo_pointery()
        x -= screen_x
        y -= screen_y
        for planet in self.planets:
            if math.sqrt((planet.getXPos() - x) ** 2 + (planet.getYPos() - y) ** 2) < planet.getRadius() * 1.5:
                self.showPlanetDetails(planet)
                break
        else:
            self.label.clear()
        self.ssscreen.ontimer(self.check_hover, 100)

    def freeze(self):
        self.ssscreen.exitonclick()

    def movePlanets(self):
        G = .1
        dt = .001

        for p in self.planets:
            p.moveTo(p.getXPos() + dt * p.getXVel(), p.getYPos() + dt * p.getYVel())

            rx = self.thesun.getXPos() - p.getXPos()
            ry = self.thesun.getYPos() - p.getYPos()
            r = math.sqrt(rx ** 2 + ry ** 2)

            accx = G * self.thesun.getMass() * rx / r ** 3
            accy = G * self.thesun.getMass() * ry / r ** 3

            p.setXVel(p.getXVel() + dt * accx)
            p.setYVel(p.getYVel() + dt * accy)

class Sun:
    def __init__(self, iname, irad, im, itemp):
        self.name = iname
        self.radius = irad
        self.mass = im
        self.temp = itemp
        self.x = 0
        self.y = 0

        self.sturtle = turtle.Turtle()
        self.sturtle.shape("circle")
        self.sturtle.color("yellow")

    def getName(self):
        return self.name

    def getRadius(self):
        return self.radius

    def getMass(self):
        return self.mass

    def getTemperature(self):
        return self.temp

    def getVolume(self):
        v = 4.0 / 3 * math.pi * self.radius ** 3
        return v

    def getSurfaceArea(self):
        sa = 4.0 * math.pi * self.radius ** 2
        return sa

    def getDensity(self):
        d = self.mass / self.getVolume()
        return d

    def setName(self, newname):
        self.name = newname

    def __str__(self):
        return self.name

    def getXPos(self):
        return self.x

    def getYPos(self):
        return self.y

class Planet:
    def __init__(self, iname, irad, im, idist, ivx, ivy, ic):
        self.name = iname
        self.radius = irad
        self.mass = im
        self.distance = idist
        self.x = idist
        self.y = 0
        self.velx = ivx
        self.vely = ivy
        self.color = ic

        self.pturtle = turtle.Turtle()
        self.pturtle.up()
        self.pturtle.color(self.color)
        self.pturtle.shape("circle")
        self.pturtle.goto(self.x, self.y)
        self.pturtle.down()

    def getName(self):
        return self.name

    def getRadius(self):
        return self.radius

    def getMass(self):
        return self.mass

    def getDistance(self):
        return self.distance

    def getVolume(self):
        v = 4.0 / 3 * math.pi * self.radius ** 3
        return v

    def getSurfaceArea(self):
        sa = 4.0 * math.pi * self.radius ** 2
        return sa

    def getDensity(self):
        d = self.mass / self.getVolume()
        return d

    def setName(self, newname):
        self.name = newname

    def show(self):
        print(self.name)

    def __str__(self):
        return self.name

    def moveTo(self, newx, newy):
        self.x = newx
        self.y = newy
        self.pturtle.goto(newx, newy)

    def getXPos(self):
        return self.x

    def getYPos(self):
        return self.y

    def getXVel(self):
        return self.velx

    def getYVel(self):
        return self.vely

    def setXVel(self, newvx):
        self.velx = newvx

    def setYVel(self, newvy):
        self.vely = newvy

def createSSandAnimate():
    ss = SolarSystem(2, 2)

    sun = Sun("SUN", 5000, 10, 5800)
    ss.addSun(sun)

    m = Planet("MERCURY", 19.5, 330, 0.25, 0, 2.4, "gray")
    ss.addPlanet(m)

    m = Planet("VENUS", 60.52, 4868.5, 0.4, 0, 1.76, "yellow")
    ss.addPlanet(m)

    m = Planet("EARTH", 63.78, 5973.6, 0.6, 0, 1.5, "blue")
    ss.addPlanet(m)

    m = Planet("MARS", 33.9, 641.85, 0.8, 0, 1.2, "red")
    ss.addPlanet(m)

    m = Planet("JUPITER", 699.11, 1898600, 1.2, 0, 0.9, "orange")
    ss.addPlanet(m)

    m = Planet("SATURN", 582.32, 568460, 1.6, 0, 0.68, "gold")
    ss.addPlanet(m)

    m = Planet("URANUS", 253.62, 86832, 2.0, 0, 0.5, "light blue")
    ss.addPlanet(m)

    m = Planet("NEPTUNE", 246.22, 102430, 2.4, 0, 0.4, "dark blue")
    ss.addPlanet(m)

    m = Planet("Pluto", 11.18, 13.05, 2.8, 0, 0.3, "brown")
    ss.addPlanet(m)

    numTimePeriods = 20000
    for amove in range(numTimePeriods):
        ss.movePlanets()

    ss.freeze()

createSSandAnimate()
