import pygame as pg
from settings import *
from game_objects import *
from bird import *
from pipe import *

class FlappyBird:
    def __init__(self) -> None:
        self.screen = pg.display.set_mode(POS)
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.load_assets()
        self.new_game()

    def load_assets(self):
        """Load all assets"""
        # Load the bird image
        bird_image = [pg.image.load(f"imgs/bird{i}.png").convert_alpha() for i in range(1,4)]
        self.bird_image = [pg.transform.scale2x(img) for img in bird_image]
        # Load the background image
        background_image = pg.image.load("./imgs/bg.png").convert()
        self.background_image = pg.transform.scale(background_image,POS)
        # Load the ground image
        ground_image = pg.image.load("./imgs/base.png").convert_alpha()
        self.ground_image = pg.transform.scale(ground_image,(WIDTH,GROUND_HEIGHT))
        # Load the pipe image
        pipe_image = pg.image.load("./imgs/pipe.png").convert()
        self.bottom_pipe_image = pg.transform.scale2x(pipe_image)
        self.top_pipe_image = pg.transform.flip(self.bottom_pipe_image,False,True)


    def run_game(self):
        """The game loop"""
        while True:
            self.check_event()
            self.draw()
            self.update()

    def check_event(self): 
        for event in pg.event.get():
            if (event.type) == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE): 
                pg.quit()
                exit()
            self.bird.check_event(event)

    def new_game(self):
        self.bird_sprite = pg.sprite.Group()
        self.bird = Bird(self)
        self.background = Background(self)
        self.ground = Ground(self)
        self.pipe_sprite = pg.sprite.Group()
        self.pipe_handler = PipeHandler(self)

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        self.background.update()
        self.bird_sprite.update()
        self.bird.update()
        self.ground.update()
        self.pipe_handler.update()

    def draw(self):
        # self.screen.fill('black')
        self.background.draw()
        pg.display.set_caption(f"{self.clock.get_fps():.1f}")
        self.bird_sprite.draw(self.screen)
        # pg.draw.rect(self.screen,"red",self.bird.rect,4)
        # self.bird.mask.to_surface(self.screen,unsetcolor=None,dest=self.bird.rect,setcolor="green")
        self.ground.draw()

if __name__ == "__main__":
    fb = FlappyBird()
    fb.run_game()
        