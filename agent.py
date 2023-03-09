from __future__ import annotations
from pygame import Vector2
from pygame.draw import circle
from pygame.surface import Surface


class Agent:
    RADIUS = 5
    REP_RANGE = 100
    K_REP = 5000000
    K_ATT = 30.1
    GOAL = Vector2(400, 400)
    agents: list[Agent] = list()
    obstacle: list[Vector2] = [
        Vector2(200, 100),
        Vector2(200, 200),
        Vector2(200, 300),
        Vector2(200, 400),
        Vector2(200, 500),
        Vector2(300, 300),
        Vector2(320, 322),
    ]
    id = 0

    def __init__(self, pos: Vector2) -> None:
        self.id = Agent.id
        Agent.id += 1
        self.pos = pos
        self.vel = Vector2(0, 0)
        Agent.agents.append(self)

    def draw(self, surface: Surface):
        circle(surface, (255, 0, 0), self.pos, self.RADIUS)

    def __reset(self):
        self.vel = Vector2(0, 0)

    def update(self, dt: float):
        self.__update_vel(dt)
        self.__update_pos(dt)
        self.__reset()

    def __update_vel(self, dt: float):
        self.__update_vel_repulsion(dt)
        self.__update_vel_attractive(dt)

    def __update_pos(self, dt: float):
        self.pos += self.vel * dt  # m/s * s = m

    def __update_vel_attractive(self, dt: float):
        # TODO: cekme kisminda pid nin i (integral) kismi da uygulanabilir

        dif = self.pos - self.GOAL  # p kismi
        attr = -self.K_ATT * dif

        self.vel += attr * dt
        print(f"{self.id} attr => {attr}")

    def __update_vel_repulsion(self, dt: float):
        repulsion = Vector2(0, 0)
        tmp = [
            agent.pos for agent in Agent.agents if agent.id != self.id
        ] + Agent.obstacle
        for pos in tmp:

            dif = self.pos - pos

            if dif.length() < Agent.REP_RANGE:
                repulsion += (
                    Agent.K_REP
                    * (1.0 / dif.length() - 1.0 / Agent.REP_RANGE)
                    * (1.0 / dif.length() ** 2)
                    * (dif.normalize())
                )

        print(f"{self.id} rep => {repulsion}")
        self.vel += repulsion * dt  # (m / s**2) * s = m/s
        # print(f"{self.id} vel => {self.vel}")
