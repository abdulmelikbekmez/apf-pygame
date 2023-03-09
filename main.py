import pygame as pg
from pygame import Vector2
from pygame.draw import circle
from pygame.time import Clock

from agent import Agent


class App:
    FPS = 60

    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((800, 600))
        self.running = True
        self.clock = Clock()
        self.agents = [
            Agent(Vector2(100, 100)),
            Agent(Vector2(110, 110)),
            Agent(Vector2(120, 120)),
            Agent(Vector2(130, 130)),
        ]

    def __hande_event(self):
        for event in pg.event.get():
            if event.type is pg.QUIT:
                self.running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False

    def __draw(self):
        for agent in self.agents:
            agent.draw(self.screen)

        circle(self.screen, (255, 255, 255), Agent.GOAL, 5)
        for pos in Agent.obstacle:
            circle(self.screen, (0, 0, 0), pos, 5)

    def __update(self):
        for agent in self.agents:
            agent.update(1 / self.FPS)

    def run(self):
        while self.running:
            self.__hande_event()

            self.screen.fill((0, 0, 255))

            self.__update()
            self.__draw()

            pg.display.update()
            self.clock.tick(self.FPS)


if __name__ == "__main__":
    App().run()
