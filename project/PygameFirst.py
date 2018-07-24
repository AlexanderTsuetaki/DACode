#!/bin/usr/ver python2.7
# PygameFirst.py
# PYGAMEZ AREZ AWEZOMZ!!!
# 03-23-2016
__author__ = "Julian Cochran"

import random
import pygame
from color import Color
from pygame import *


class PygameFirst:
    width = 800
    height = 600
    xSpeed = 0
    ySpeed = 0
    screen = None
    block = None
    block_color = None
    myFont = None
    bounce_spot = (0,0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("+ MY FIRZT PYGAMEZ +")
        self.block = Rect(0,0,60,60)
        self.bounce_spot = self.screen.get_rect().center
        self.block.center = self.bounce_spot
        self.xSpeed = random.randint(-5,5)
        self.ySpeed = random.randint(-5,5)
        # if you want to find a device to let the user select the color, do it here
        self.block_color = Color.YELLOW

    def draw_block(self):
        pygame.draw.ellipse(self.screen, self.block_color, self.block)

    def draw_message(self, msg):
        self.myFont = pygame.font.SysFont(None,46)
        text = self.myFont.render(msg, True, Color.WHITE)
        textRect = text.get_rect()
        textRect.center = self.bounce_spot
        self.screen.blit(text, textRect)

    def run(self):
        running = True
        displayMsg = "HELLO"
        while(running):
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            # move the block
            self.block.move_ip(self.xSpeed, self.ySpeed)
            self.screen.fill(Color.BLACK)
            self.draw_block()
            self.draw_message(displayMsg)
            pygame.display.flip()
            # bounce the block off the walls, if needed
            if self.block.left < 1:
                self.block.left = 1
                self.xSpeed *= -1
                displayMsg = str(self.block.center)
                self.block_color = Color.random_color()
                self.bounce_spot = self.block.center
            elif self.block.right > self.width-1:
                self.block.right = self.width-1
                self.xSpeed *= -1
                displayMsg = str(self.block.center)
                self.block_color = Color.random_color()
                self.bounce_spot = self.block.center
            if self.block.top < 1:
                self.block.top = 1
                self.ySpeed *= -1
                displayMsg = str(self.block.center)
                self.block_color = Color.random_color()
                self.bounce_spot = self.block.center
            elif self.block.bottom > self.height-1:
                self.block.bottom = self.height-1
                self.ySpeed *= -1
                displayMsg = str(self.block.center)
                self.block_color = Color.random_color()
                self.bounce_spot = self.block.center

        pygame.quit()
        print('Program closing')
        sys.exit(0)

if __name__ == "__main__":
    app = PygameFirst()
    app.run()