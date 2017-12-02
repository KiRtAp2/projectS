import pygame
import colors
import consts
from consts import WHEIGHT, WWIDTH
from classes import player
from classes import bullet


window = pygame.display.set_mode((WWIDTH, WHEIGHT))
clock = pygame.time.Clock()

pl = player.Player()
bullet_list = []


def main():
    running = True

    while running:

        for e in pygame.event.get():

            if e.type == pygame.QUIT:
                running = False

            if e.type == pygame.KEYDOWN:

                if e.key == pygame.K_w:
                    pl.velocity = -consts.PLAYER_SPEED

                if e.key == pygame.K_s:
                    pl.velocity = consts.PLAYER_SPEED

                if e.key == pygame.K_f:
                    bullet_list.append(bullet.Bullet(pl.get_pos(), pl.rotation))

            if e.type == pygame.KEYUP:

                if e.key in (pygame.K_w, pygame.K_s):
                    pl.velocity = 0

            if e.type == pygame.MOUSEMOTION:
                pl.rotate(pygame.mouse.get_pos())

        window.fill(colors.WHITE)
        pl.move()
        pl.show(window)

        for b in bullet_list:
            if b.move():
                bullet_list.remove(b)
            else:
                b.show(window)

        pygame.display.update()
        clock.tick(consts.FRAMERATE)


if __name__ == '__main__':
    pygame.init()
    main()
