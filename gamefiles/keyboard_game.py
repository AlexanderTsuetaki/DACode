
import pygame
import sys
from client_test import send_data
import time


class Keything:
    indexlist = []
    letterlist = ''
    alphabet = {}
    """
    for i in range(26):
        alphabet[i + 97] = string.ascii_lowercase[i]
    for j in range(10):
        alphabet[j + 48] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9][j]
    alphabet[32] = ' '
    """
    for i in range(128):
        alphabet[i] = chr(i)
    alphabet[8] = 'del'
    alphabet[13] = 'ret'

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((441, 176))
        pygame.display.set_caption("")
        self.image = pygame.image.load("menu_new.png")

        self.block = pygame.Rect((177, 89), (1, 16))
        self.button = pygame.Rect((352, 137), (68, 18))

    def interpret_list(self):
        for char in self.indexlist:
            if char in self.alphabet:
                if self.alphabet[char] == 'del':
                    self.letterlist = self.letterlist[0:len(self.letterlist) - 1]
                elif self.alphabet[char] == 'ret':
                    # self.letterlist += 'RET'
                    pass
                else:
                    self.letterlist += str(self.alphabet[char])
        self.indexlist = []

    def run(self):
        self.running = True
        loops = 0
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pass
                if event.type == pygame.KEYDOWN:
                    self.indexlist.append(event.key)
                    if event.key == 13:
                        if len(self.letterlist) > 6:
                            self.running = False
                    elif event.key == 8:
                        if self.block.x > 177:
                            if len(self.letterlist) < 39:
                                self.block.x -= 6
                    elif event.key in self.alphabet:
                        if self.block.x < 405:
                            self.block.x += 6
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    self.interpret_list()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())
                    if self.button.collidepoint(pygame.mouse.get_pos()):
                        if len(self.letterlist) > 6:
                            time.sleep(0.1)
                            self.running = False

            self.screen.blit(self.image, (0, 0))
            if loops % 70 >= 35:
                pygame.draw.rect(self.screen, (0, 0, 0), self.block)
            for i in range(len(self.letterlist)):
                pygame.draw.ellipse(self.screen, (50, 50, 50), pygame.Rect(178 + 6*i, 96, 5, 5))
                if i > 36:
                    break
            pygame.display.update()
            loops += 1
        self.interpret_list()
        send_data(self.letterlist)
        pygame.quit()
        sys.exit()

k = Keything()
k.run()
