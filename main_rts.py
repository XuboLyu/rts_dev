import os,sys
# make sure the video driver is correct. "dummy" is headless, so do not use it.
# os.environ['SDL_VIDEODRIVER'] = "x11"
# os.putenv("DISPLAY", ":0")
#
#
# # os.environ['SDL_AUDIODRIVER'] =  "pulseaudio"
# os.putenv("PULSE_SERVER", "tcp:localhost")

import pygame
from pygame.locals import *
from button import Button
import time

display_width = 640
display_height= 480
purple = (128, 0, 128)
lime = (0,255,0)
yellow = (255, 255, 0)

cur_dir = os.path.dirname(os.path.realpath(__file__))
print(cur_dir)

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load(cur_dir + '/assets/sounds/06 motorized.mp3')
screen = pygame.display.set_mode((display_width,display_height))


intro_img = pygame.image.load(cur_dir + "/assets/images/splash2.jpg")
print("img shape:", intro_img.get_size())
if intro_img.get_size() != (display_width, display_height):
    intro_img = pygame.transform.scale(intro_img, (display_width, display_height))

button_single = Button(purple, (450, 250, 150, 50))
button_multi = Button(yellow, (450, 310, 150, 50))
button_quit  = Button(lime, (450, 370, 150, 50))

start_time = time.time()
pygame.mixer.music.play(-1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.blit(intro_img, (0,0))

    cur_time = time.time()
    if cur_time - start_time > 5:
        button_single.Draw(screen, text='Single Player')
        button_multi.Draw(screen, text='Multiple Players')
        button_quit.Draw(screen, text='Quit Game')

    pygame.display.update()






