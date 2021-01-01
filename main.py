from math import trunc
import pygame
import random

# globals
display_width = 400
display_height = 400
population = 100


# predefined colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
bright_green = (0, 255, 0)


pygame.init()
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("covid-19 simulation")


class person():
    def __init__(self, name, point):
        self.name = name
        self.infected = False
        self.survived = False
        self.location = point


def move_person(people):
    for persons in people:
        i = 0
        displacement = random.random()
        while(True):
            if(displacement < 0.2):
                break

        x, y = persons.location
        x += displacement
        y += displacement
        persons.location = (x, y)


def game_loop():
    people = []
    for i in range(population):
        people.append(person(i, (0, 0)))

    while(True):
        move_person(people)
        pygame.display.update()
        dis.fill(white)
        pygame.time.wait(50)
        print("hasnain")
