from math import trunc
import pygame
import random
from pygame import *
import math

# globals
display_width = 800
display_height = 800
population = 1000000
personperrow = math.sqrt(population)
print(personperrow)
width = display_width/personperrow
height = display_height/personperrow
margin = ((width/100)*1.5, (height/100)*1.5)
infection_percent = 0.002


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

        while(True):
            displacement = random.random()

            if(displacement < 0.1):
                break

        a = random.random()

        if(a < 0.5):
            displacement = displacement * -1

        x, y = persons.location
        if(x <= 0 or x >= display_width):
            if(displacement < 0 and x >= display_width+width):
                x += displacement
            if(displacement > 0 and x <= 0):
                x += displacement

        else:
            x += displacement
        if(y <= 0 or x >= display_height):
            if(displacement < 0 and y >= display_height+height):
                y += displacement
            if(displacement > 0 and y <= 0):
                y += displacement

        else:
            y += displacement
        persons.location = (x, y)


def display_person(people):
    for p in people:
        if(p.infected == True):
            pygame.draw.rect(
                dis, red, (((p.location[0] * width)), ((p.location[1]*height)), width-margin[0], height-margin[1]))
        else:
            pygame.draw.rect(
                dis, black, (((p.location[0] * width)), ((p.location[1]*height)), width-margin[0], height-margin[1]))


def event_handler():

    for event in pygame.event.get():
        if (event.type == QUIT):
            running = False
            pygame.quit()
            quit()


def check_spread(people):
    for p in people:

        if(p.infected == True):

            x, y = p.location
            if(x > 0):
                for q in people:
                    if(q.location == (x-1, y)):
                        chance = random.random()
                        if(chance < infection_percent):
                            # print("111")
                            q.infected = True

            if(x < personperrow-1):
                for q in people:
                    if(q.location == (x+1, y)):
                        chance = random.random()
                        if(chance < infection_percent):
                            q.infected = True

            if(y > 0):
                for q in people:
                    if(q.location == (x, y-1)):
                        chance = random.random()
                        if(chance < infection_percent):
                            q.infected = True

            if(y < personperrow-1):
                for q in people:
                    if(q.location == (x, y+1)):
                        chance = random.random()
                        if(chance < infection_percent):
                            q.infected = True

    return people


def check_end_state(people):
    c = False
    for p in people:
        if(p.infected == False):
            c = True
    return c


def game_loop():
    people = []
    j = 0
    k = 0
    for i in range(population):
        people.append(person(i, (j, k)))
        #print(j, "  ", k)

        if(j >= personperrow-1):
            j = 0
            k += 1
        else:
            j += 1

    center = math.ceil(personperrow/2)

    for p in people:
        if(p.location == (center, center)):
            p.infected = True

    print()

    while(check_end_state(people)):
        event_handler()
        display_person(people)
        # move_person(people)
        people = check_spread(people)
        pygame.display.update()
        dis.fill(white)
        pygame.time.wait(50)

        """"if(a > 100):
            break
        else:
            a += 1
"""""


game_loop()
