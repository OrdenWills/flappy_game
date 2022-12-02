import pygame as pg
from settings import *
from collections import deque

class Bird(pg.sprite.Sprite):
    def __init__(self,game, *groups) -> None:
        super().__init__(game.bird_sprite)
        self.game = game
        self.image = game.bird_image[0]
        self.rect = self.image.get_rect()
        self.rect.center = BIRD_START_POS
        self.mask = pg.mask.from_surface(self.image)

        self.images = deque(self.game.bird_image)
        self.animation_event = pg.USEREVENT + 0
        pg.time.set_timer(self.animation_event,BIRD_ANIMATION_TIME)

        self.first_jump = False
        self.falling_velocity = 0
        self.angle = 0

    def jump(self):
        self.first_jump = True
        self.falling_velocity = BIRD_JUMP_VALUE

    def check_collision(self):
        self.mask = pg.mask.from_surface(self.image)
        hit = pg.sprite.spritecollide(self,self.game.pipe_sprite,False,collided=pg.sprite.collide_mask)
        if (hit) or (self.rect.bottom >= GROUND_Y) or (self.rect.top < self.game.screen_rect.top - 25):
            pg.time.wait(1000)
            self.game.new_game()

    def use_gravity(self):
        if (self.first_jump):
            self.falling_velocity += GRAVITY
            self.rect.y += self.falling_velocity * 0.5 + GRAVITY

    def rotate(self):
        if (self.first_jump):
            if (self.falling_velocity < -BIRD_JUMP_VALUE):
                self.angle = BIRD_JUMP_ANGLE
            else:
                self.angle = max(-2.5 * self.falling_velocity,-90)
        self.image = pg.transform.rotate(self.image,self.angle)

    def update(self):
        self.use_gravity()
        self.check_collision()

    def animate(self):
        self.images.rotate(-1)
        self.image = self.images[0]

    

    def check_event(self,event):
        if (event.type == pg.USEREVENT):
            self.animate()
            self.rotate()
        if (event.type == pg.KEYDOWN):
            if event.key == pg.K_SPACE:
                self.jump()
        # key = pg.key.get_pressed()
        # if 