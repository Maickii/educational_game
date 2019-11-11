import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (245, 212, 66)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

block_color = (53, 115, 255)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Fun with Numbers!')

clock = pygame.time.Clock()


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_intro()


def correct():
    message_display("You're Correct")


def wrong():
    message_display("You're Wrong")


def crash():
    message_display('You Crashed')

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def Answer(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def game_intro():
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill([255, 255, 255])
        gameDisplay.blit(BackGround.image, BackGround.rect)
        largeText = pygame.font.Font('freesansbold.ttf', 55)
        TextSurf, TextRect = text_objects("Fun with Numbers", largeText)
        TextRect.center = ((display_width / 2), (display_height / 4))
        gameDisplay.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()

        print(mouse)

        if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_green, (((display_width / 2)-50), (display_height / 2), 100, 50))
        else:
            pygame.draw.rect(gameDisplay, green, (((display_width / 2)-50), (display_height / 2), 100, 50))


        if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_red, (((display_width / 2)-50), (display_height-150), 100, 50))
        else:
            pygame.draw.rect(gameDisplay, red, (((display_width / 2)-50), (display_height-150), 100, 50))

        button("GO!",(display_width / 2)-50, (display_height / 2), 100, 50,green,bright_green,game_loop)
        button("Help!", ((display_width / 2)-50), (display_height-150), 100, 50, red, bright_red, game_loop)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill([255, 255, 255])
        gameDisplay.blit(BackGround.image, BackGround.rect)
        largeText = pygame.font.Font('freesansbold.ttf', 55)
        TextSurf, TextRect = text_objects("What is 200-50:", largeText)
        TextRect.center = ((display_width / 2), (display_height / 4))
        gameDisplay.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()

        print(mouse)

        if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_green, (((display_width / 6)), (display_height / 2), 100, 50))
        else:
            pygame.draw.rect(gameDisplay, green, (((display_width / 6)), (display_height / 2), 100, 50))

        if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_red, ((display_width -250), (display_height / 2), 100, 50))
        else:
            pygame.draw.rect(gameDisplay, red, ((display_width -250), (display_height / 2), 100, 50))

        Answer("150", display_width / 6, (display_height / 2), 100, 50,green,bright_green,correct)
        Answer("250", (display_width - 250), (display_height / 2), 100, 50, red, bright_red, wrong)
        things_dodged(dodged)

        pygame.display.update()
        clock.tick(15)


BackGround = Background('background_image.png', [0,0])
game_intro()
game_loop()
pygame.quit()
quit()