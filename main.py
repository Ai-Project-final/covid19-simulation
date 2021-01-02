from math import trunc
import pygame
import random
from pygame import *
import math

# globals
population = 10000
display_width = 1300
display_height = 800
display_side_pane_width = 500
personperrow = int(math.sqrt(population))
width = (display_width-display_side_pane_width)/personperrow
height = display_height/personperrow
margin = ((width/100)*1.5, (height/100)*1.5)
infection_percent = 0.20
flagg = True
infection_locked = []


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
                dis, blue, (((p.location[0] * width)), ((p.location[1]*height)), width-margin[0], height-margin[1]))


def event_handler():

    for event in pygame.event.get():
        if (event.type == QUIT):
            running = False
            pygame.quit()
            quit()
            return "shut"


def check_spread(people):
    no_of_infected = 0
    for p in people:

        if(p.infected == True and p not in infection_locked):

            x, y = p.location
            ind = people.index(p)
            current_p = []   # left ,right ,up ,down

            if(y < personperrow-1):

                index_bottom = ind + personperrow
                if(people[index_bottom].infected == False):
                    chance = random.random()
                    if(chance < infection_percent):
                        people[index_bottom].infected = True
                        no_of_infected += 1
                else:
                    current_p.append(1)

            else:
                current_p.append(1)

            if(x > 0):

                index_right = ind-1
                if(people[index_right].infected == False):
                    chance = random.random()
                    if(chance < infection_percent):
                        people[index_right].infected = True
                        no_of_infected += 1
                else:
                    current_p.append(1)

            else:
                current_p.append(1)

            if(y > 0):

                index_top = ind - personperrow
                if(people[index_top].infected == False):
                    chance = random.random()
                    if(chance < infection_percent):
                        people[index_top].infected = True
                        no_of_infected += 1
                else:
                    current_p.append(1)

            else:
                current_p.append(1)

            if(x < personperrow-1):

                index_left = ind+1
                if(people[index_left].infected == False):
                    chance = random.random()
                    if(chance < infection_percent):
                        people[index_left].infected = True
                        no_of_infected += 1
                else:
                    current_p.append(1)

            else:
                current_p.append(1)

            if(current_p == [1, 1, 1, 1]):

                infection_locked.append(p)
    return people, no_of_infected


def drawbuttons(tex):

    pygame.draw.rect(dis, white, (display_width-display_side_pane_width,
                                  0, (display_side_pane_width), display_height))

    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render(tex[1], True, black)
    textRect = text.get_rect()
    textRect.center = (display_width-100, display_height/2)

    dis.blit(text, textRect)


def game_loop():
    people = []
    j = 0
    k = 0
    no_of_infected = 1
    for i in range(population):
        people.append(person(i, (j, k)))
        # print(j, "  ", k)

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
    days = 0
    while(no_of_infected-1 < population):
        close = event_handler()
        if close == 'shut':
            break

        display_person(people)
        # move_person(people)
        people, no = check_spread(people)
        no_of_infected += no
        days += 1
        ipd = str(no_of_infected)
        t = str(days)
        text = (t, ipd)
        drawbuttons(text)
        pygame.display.update()
        dis.fill(white)
        pygame.time.wait(10)

        """"if(a > 100):
            break
        else:
            a += 1
"""""


game_loop()
