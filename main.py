import pygame

import colors
import consts
from consts import WHEIGHT, WWIDTH
from classes import player


window = pygame.display.set_mode((WWIDTH, WHEIGHT))
clock = pygame.time.Clock()

pl = player.Player()


def main():
    running = True

    while running:

        for e in pygame.event.get():

            if e.type == pygame.QUIT:
                running = False

            if e.type == pygame.KEYDOWN:

                pass

        window.fill(colors.WHITE)
        pl.show(window)

        pygame.display.update()
        clock.tick(consts.FRAMERATE)


if __name__ == '__main__':
    pygame.init()
    main()
