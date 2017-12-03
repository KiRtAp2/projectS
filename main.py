import pygame
import consts
import events
from classes import bullet, player, enemy, totem
from consts import WHEIGHT, WWIDTH
from utility import colors, text

window = pygame.display.set_mode((WWIDTH, WHEIGHT))
clock = pygame.time.Clock()

pl = player.Player()
t = totem.Totem()
bullet_list = []
enemy_list = []
score = 0

pygame.time.set_timer(events.ENEMY_SPAWN, consts.ENEMY_SPAWN_DELAY*1000)


def main():
    global score
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
                    bullet_list.append(bullet.Bullet(pl))

                if e.key == pygame.K_p:
                    game_over()
                    running = False
                    continue

            if e.type == pygame.KEYUP:

                if e.key in (pygame.K_w, pygame.K_s):
                    pl.velocity = 0

            if e.type == pygame.MOUSEMOTION:
                pl.rotate(pygame.mouse.get_pos())

            if e.type == events.ENEMY_SPAWN:
                enemy_list.append(enemy.Enemy(t.get_pos()))

        window.fill(colors.WHITE)
        t.show(window)
        pl.move()
        pl.show(window)

        for b in bullet_list:
            if b.move():
                bullet_list.remove(b)
            else:
                b.show(window)

        for e in enemy_list:
            e.move()
            e.show(window)
            for b in bullet_list:
                if e.is_hit_by(b):
                    bullet_list.remove(b)
                    enemy_list.remove(e)
                    score += 1

        for e in enemy_list:
            if e.is_hit_by(t):
                game_over()
                running = False
                continue

        pygame.display.update()
        clock.tick(consts.FRAMERATE)


def game_over():
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        window.fill(colors.WHITE)
        window.blit(text.get_surf("GAME OVER", colors.BLACK, 50), (WWIDTH*0.3, WHEIGHT*0.4))
        window.blit(text.get_surf("Score: "+str(score), colors.BLACK, 30), (WWIDTH*0.3, WHEIGHT*0.5))
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    main()
