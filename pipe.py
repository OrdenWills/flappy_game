import pygame as pg
from settings import *
import random

class TopPipe(pg.sprite.Sprite):
    def __init__(self,game,gap_y_pos,*groups) -> None:
        super().__init__(game.pipe_sprite,game.bird_sprite,*groups)
        self.image = game.top_pipe_image
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.bottomleft = WIDTH,gap_y_pos - HALF_GAP_HEIGHT - GROUND_HEIGHT
        # print(self.rect.bottomleft)

    def update(self) -> None:
        self.rect.left -= SCROLL_SPEED
        if self.rect.right < 0:
            self.kill()



class BottomPipe(TopPipe):
    def __init__(self, game, gap_y_pos, *groups) -> None:
        super().__init__(game, gap_y_pos, *groups)
        self.image = game.bottom_pipe_image
        self.rect.topleft = WIDTH , gap_y_pos + HALF_GAP_HEIGHT - GROUND_HEIGHT

class PipeHandler:
    def __init__(self,game) -> None:
        self.game = game
        self.pipe_dist = DIST_BTW_PIPES

    def update(self):
        self.generate_pipes()

    @staticmethod
    def get_gap_y_position():
        return random.randint(GAP_HEIGHT,HEIGHT - GAP_HEIGHT)

    def generate_pipes(self):
        if self.game.bird.first_jump:
            self.pipe_dist += SCROLL_SPEED
            if self.pipe_dist > DIST_BTW_PIPES:
                self.pipe_dist = 0
                gap_y = self.get_gap_y_position()

                TopPipe(self.game,gap_y)
                BottomPipe(self.game,gap_y)