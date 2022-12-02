import pygame as pg 
from settings import *

class Background:
    def __init__(self,game) -> None:
        self.game = game
        self.image = game.background_image
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.speed = SCROLL_SPEED - 2

    def update(self):
        self.x = (self.x - self.speed) % -WIDTH
        # print(self.x)

    def draw(self):
        self.game.screen.blit(self.image,(self.x,self.y))
        self.game.screen.blit(self.image,(WIDTH + self.x,self.y))


class Ground(Background):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.image = self.game.ground_image
        self.x = 0
        self.y = GROUND_Y