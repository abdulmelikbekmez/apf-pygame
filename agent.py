from __future__ import annotations
from pygame import Vector2
from pygame.draw import circle
from pygame.surface import Surface


class Agent:
    RADIUS = 5
    REP_RANGE = 100
    K_REP = 500
    agents: list[Agent] = list()
    id = 0

    def __init__(self, pos: Vector2) -> None:
        self.id = Agent.id
        Agent.id += 1
        self.pos = pos
        self.vel = Vector2(0, 0)
        Agent.agents.append(self)

    def draw(self, surface: Surface):
        circle(surface, (255, 0, 0), self.pos, self.RADIUS)

    def update(self, dt: float):
        self.__update_vel(dt)
        self.__update_pos(dt)

    def __update_vel(self, dt: float):
        self.__update_vel_repulsion(dt)
        self.__update_vel_attractive(dt)

    def __update_pos(self, dt: float):
        self.pos += self.vel * dt  # m/s * s = m

    def __update_vel_attractive(self, dt: float):
        ...

    def __update_vel_repulsion(self, dt: float):
        repulsion = Vector2(0, 0)
        for agent in Agent.agents:
            if agent.id == self.id:
                continue

            dif = self.pos - agent.pos

            if dif.length() < Agent.REP_RANGE:
                repulsion += (
                    Agent.K_REP
                    * (1.0 / dif.length() - 1.0 / Agent.REP_RANGE)
                    * (1.0 / dif.length() ** 2)
                    * (dif.normalize())
                )

        self.vel += repulsion * dt  # (m / s**2) * s = m/s
        print(f"{self.id} vel => {self.vel}")
