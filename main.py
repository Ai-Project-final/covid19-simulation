import pygame
import random
from pygame import *
import math
import matplotlib.pyplot as plt

# globals
population = 10000
display_width = 1200
display_height = 800
display_side_pane_width = 400
personperrow = int(math.sqrt(population))
width = (display_width-display_side_pane_width)/personperrow
height = display_height/personperrow
margin = ((width/100)*1.5, (height/100)*1.5)
infection_percent = 10/100
infection_locked = []
recovery_days = 28
recovery_percent = 10 / 100
preventive_measures_followed_percentage = 5/100
mask_prevention = 9

# predefined colours
white = (255, 255, 255)  # mask wale log
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
bright_green = (0, 255, 0)
yellow = (255, 255, 0)

pygame.init()
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("covid-19 simulation")
f = open("record.txt", 'w')


class person():
    def __init__(self, name, point):
        self.name = name
        self.infected = False
        self.survived = False
        self.dead = False
        self.location = point
        self.mask = False
        self.days_infected = 0


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
            pygame.draw.circle(dis, red, ((p.location[0] * width)+(
                width-margin[0])/2, (p.location[1]*height)+(height-margin[1])/2), (width-margin[0])/2)
            # pygame.draw.rect(
            #   dis, red, (((p.location[0] * width)), ((p.location[1]*height)), width-margin[0], height-margin[1]))

        elif(p.infected == False and p.survived == True and p.dead == False):
            pygame.draw.circle(dis, green, ((p.location[0] * width)+(
                width-margin[0])/2, (p.location[1]*height)+(height-margin[1])/2), (width-margin[0])/2)
            # pygame.draw.rect(
            #    dis, green, (((p.location[0] * width)), ((p.location[1]*height)), width-margin[0], height-margin[1]))

        elif(p.infected == False and p.survived == True and p.dead == True):
            pygame.draw.circle(dis, yellow, ((p.location[0] * width)+(
                width-margin[0])/2, (p.location[1]*height)+(height-margin[1])/2), (width-margin[0])/2)
            # pygame.draw.rect(
            #    dis, black, (((p.location[0] * width)), ((p.location[1]*height)), width-margin[0], height-margin[1]))

        elif(p.infected == False and p.mask == True):
            pygame.draw.circle(dis, white, ((p.location[0] * width)+(
                width-margin[0])/2, (p.location[1]*height)+(height-margin[1])/2), (width-margin[0])/2)
            # pygame.draw.rect(dis, blue, ((
            #    (p.location[0] * width)), ((p.location[1]*height)), width-margin[0], height-margin[1]))

        else:
            pygame.draw.circle(dis, blue, ((p.location[0] * width)+(
                width-margin[0])/2, (p.location[1]*height)+(height-margin[1])/2), (width-margin[0])/2)
            # pygame.draw.rect(
            #    dis, white, (((p.location[0] * width)), ((p.location[1]*height)), width-margin[0], height-margin[1]))


def event_handler():

    for event in pygame.event.get():
        if (event.type == QUIT):
            running = False
            pygame.quit()
            quit()
            return "shut"


def check_spread(people, infected):
    no_of_infected = 0

    if(infected < population*0.60):

        for p in people:

            if(p.infected == True and p not in infection_locked):

                x, y = p.location
                ind = people.index(p)
                current_p = []   # left ,right ,up ,down

                if(y < personperrow-1):

                    index_bottom = ind + personperrow
                    if(people[index_bottom].infected == False and people[index_bottom].survived == False):
                        chance = random.random()
                        if(people[index_bottom].mask == True):
                            chance = chance*mask_prevention

                        if(chance < infection_percent):
                            people[index_bottom].infected = True
                            no_of_infected += 1
                    else:
                        current_p.append(1)

                else:
                    current_p.append(1)

                if(x > 0):

                    index_right = ind-1
                    if(people[index_right].infected == False and people[index_right].survived == False):
                        chance = random.random()
                        if(people[index_right].mask == True):
                            chance = chance*mask_prevention
                        if(chance < infection_percent):
                            people[index_right].infected = True
                            no_of_infected += 1
                    else:
                        current_p.append(1)

                else:
                    current_p.append(1)

                if(y > 0):

                    index_top = ind - personperrow
                    if(people[index_top].infected == False and people[index_top].survived == False):
                        chance = random.random()
                        if(people[index_top].mask == True):
                            chance = chance*mask_prevention
                        if(chance < infection_percent):
                            people[index_top].infected = True
                            no_of_infected += 1
                    else:
                        current_p.append(1)

                else:
                    current_p.append(1)

                if(x < personperrow-1):

                    index_left = ind+1
                    if(people[index_left].infected == False and people[index_left].survived == False):
                        chance = random.random()
                        if(people[index_left].mask == True):
                            chance = chance*mask_prevention
                        if(chance < infection_percent):
                            people[index_left].infected = True
                            no_of_infected += 1
                    else:
                        current_p.append(1)

                else:
                    current_p.append(1)

                if(current_p == [1, 1, 1, 1]):

                    infection_locked.append(p)
    else:
        for p in people:

            if(p.infected == False and p.survived == False):

                x, y = p.location
                ind = people.index(p)

                if(y < personperrow-1 and p.infected == False):

                    index_bottom = ind + personperrow
                    if(people[index_bottom].infected == True):
                        chance = random.random()
                        if(p.mask == True):
                            chance = chance*mask_prevention
                        if(chance < infection_percent):
                            p.infected = True
                            no_of_infected += 1

                if(x > 0 and p.infected == False):

                    index_right = ind-1
                    if(people[index_right].infected == True):
                        chance = random.random()
                        if(p.mask == True):
                            chance = chance*mask_prevention
                        if(chance < infection_percent):
                            p.infected = True
                            no_of_infected += 1

                if(y > 0 and p.infected == False):

                    index_top = ind - personperrow
                    if(people[index_top].infected == True):
                        chance = random.random()
                        if(p.mask == True):
                            chance = chance*mask_prevention
                        if(chance < infection_percent):
                            p.infected = True
                            no_of_infected += 1

                if(x < personperrow-1 and p.infected == False):

                    index_left = ind+1
                    if(people[index_left].infected == True):
                        chance = random.random()
                        if(p.mask == True):
                            chance = chance*mask_prevention
                        if(chance < infection_percent):
                            p.infected = True
                            no_of_infected += 1

    return people, no_of_infected


def drawbuttons():
    pg = pygame
    screen = pygame.display.set_mode((640, 480))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(100, 100, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        population = int(text)
                        text = ''
                        done = True
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pg.draw.rect(screen, color, input_box, 2)
        pg.display.flip()
        clock.tick(30)


def boxes():
    pygame.draw.rect(dis, (246, 4, 4), (430, 30, 40, 40))
    pygame.draw.rect(dis, (255, 255, 255), (10, 70, 40, 40))
    pygame.draw.rect(dis, (250, 247, 2), (10, 130, 40, 40))
    pygame.draw.rect(dis, (87, 208, 3), (10, 200, 40, 40))


def check_recovery(people):
    recovered = 0
    deaths = 0
    for p in people:
        if(p.infected == True):
            if(p.days_infected < recovery_days):
                p.days_infected += 1
            else:
                chance = random.random()
                if(chance > recovery_percent):
                    p.infected = False
                    p.survived = True
                    p.dead = False
                    recovered += 1
                else:
                    p.infected = False
                    p.survived = True
                    p.dead = True
                    deaths += 1
    return deaths, recovered


def preventive_measures(people):
    for p in people:
        chance = random.random()
        if(chance < preventive_measures_followed_percentage):
            p.mask = True
        else:
            p.mask = False


def record_data(no, deaths, recoverd, days, total_deaths, total_recovered, n):
    total_recovered = str(total_recovered)
    total_deaths = str(total_deaths)
    n = str(n)
    days = str(days)
    no = str(no)
    deaths = str(deaths)
    recoverd = str(recoverd)
    l = days + "," + deaths+","+recoverd+","+no+"," + \
        n+","+total_deaths+","+total_recovered+"\n"
    f.write(l)


def plot_curve():
    alldays = []
    allinfected = []
    alldead = []
    allrecovered = []
    data = []
    f = open("record.txt", "r")
    l = f.readlines()

    for item in l:
        t = []
        length = item.__len__()
        d = ""
        for j in range(length):

            if not item[j] == ",":
                d = d+item[j]
            else:
                t.append(int(d))
                d = ""
        data.append(t)

    for i in data:
        alldays.append(i[0])
        allinfected.append(i[3])
        alldead.append(i[1])
        allrecovered.append(i[2])

    if(allinfected.__len__() % 2 == 1):
        allinfected.append(allinfected[-1])
    i = 0
    allinfected_noramalized = []
    for j in range(int(allinfected.__len__() / 2)):
        avg = (allinfected[i] + allinfected[i+1])/2
        i += 2
        allinfected_noramalized.append(avg)

    plt.subplot(2, 1, 1)
    plt.title('days vs number of cases perday')
    plt.xlabel('Number of days')
    plt.ylabel('Numbe rof cases')
    plt.plot(alldays, allinfected)
    plt.subplot(2, 1, 2)
    plt.title('days vs number of deaths perday')
    plt.xlabel('Number of days')
    plt.ylabel('Number of deaths')
    plt.plot(alldays, alldead)
    """"plt.subplot(2, 1, 1.5)
    plt.title('days vs number of recovered perday')
    plt.xlabel('Number of days')
    plt.ylabel('Number of recovered')
    plt.plot(alldays, allrecovered)
    """""
    plt.subplots_adjust(left=None, bottom=None, right=None,
                        top=None, wspace=None, hspace=0.471)
    plt.show()


def game_loop():
    # drawbuttons()

    boxes()

    people = []
    j = 0
    k = 0
    total_deaths = 0
    total_recovered = 0
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
        if(p.location == (0, 0)):
            p.infected = True
        if(p.location == (personperrow-1, personperrow-1)):
            p.infected = True

    display_person(people)
    preventive_measures(people)
    print()
    days = 0
    i = 0
    previous_n = 0
    while(True):
        close = event_handler()
        if close == 'shut':
            break
        # move_person(people)
        people, no = check_spread(people, no_of_infected)
        deaths, recoverd = check_recovery(people)
        display_person(people)
        total_deaths += deaths
        total_recovered += recoverd
        no_of_infected += no
        days += 1
        n = population - (no_of_infected)
        record_data(no, deaths, recoverd, days,
                    total_deaths, total_recovered, n)

        pygame.display.update()
        dis.fill(black)
        pygame.time.wait(1)
        if(previous_n == total_recovered):
            i += 1
            if(i >= 60):
                break
        previous_n = total_recovered


game_loop()
f.close()
pygame.time.wait(100)
plot_curve()
