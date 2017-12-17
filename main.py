import pygame
import consts
import events
from classes import bullet, player, enemy, totem, typer
from consts import WHEIGHT, WWIDTH
from utility import colors, text, selector
from utility.texture_loader import textures

window = pygame.display.set_mode((WWIDTH, WHEIGHT))
clock = pygame.time.Clock()

pl = player.Player()
t = totem.Totem()
bullet_list = []
enemy_list = []
score = 0

pygame.time.set_timer(events.ENEMY_SPAWN, consts.ENEMY_SPAWN_DELAY*1000)
pygame.display.set_caption("Igra za informatiko")


def main():
    global score, pl, t, bullet_list, enemy_list
    running = True

    # resets game state after playing again
    pl = player.Player()
    t = totem.Totem()
    bullet_list = []
    enemy_list = []
    score = 0


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

            if e.type == pygame.KEYUP:

                if e.key in (pygame.K_w, pygame.K_s):
                    pl.velocity = 0

            if e.type == pygame.MOUSEMOTION:
                pl.rotate(pygame.mouse.get_pos())

            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    bullet_list.append(bullet.Bullet(pl))

            if e.type == events.ENEMY_SPAWN:
                enemy_list.append(enemy.Enemy(t.get_pos, score))

        window.fill(colors.WHITE)
        t.show(window)

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

        pl.move()
        pl.show(window)

        pygame.display.update()
        clock.tick(consts.FRAMERATE)


def pre_game_loop():
    
    running = True

    SELECTOR_OPTIONS = ["Play", "Exit"]

    sel = selector.Selector(SELECTOR_OPTIONS, (WWIDTH*0.2, WHEIGHT*0.45), autostart=True)

    typing = False
    typing_field = typer.TypingField()

    while running:

        for e in pygame.event.get():

            if not typing:
                if e.type == pygame.QUIT:
                    running = False

                if e.type == pygame.KEYDOWN:

                    if e.key == pygame.K_RETURN:
                        if sel.get_selected_el() == "Exit":
                            running = False

                        if sel.get_selected_el() == "Play":
                            running = False
                            main()
                            continue

                    if e.key == pygame.K_DOWN:
                        sel.go_down()

                    if e.key == pygame.K_UP:
                        sel.go_up()

                    if e.key == pygame.K_p:
                        typing = True
            else:
                if e.type == pygame.QUIT:
                    running = False

                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        typing = False
                    else:
                        typing_field.type(e.key)

        window.fill(colors.WHITE)
        sel.show(window)
        window.blit(textures["logo"], (WWIDTH*0.1, WHEIGHT*0.1))
        window.blit(typing_field.get_surf(), (WWIDTH*0.1, WHEIGHT*0.8))
        pygame.display.update()


def game_over():

    SELECTOR_OPTIONS = ["Title screen", "Exit"]

    sel = selector.Selector(SELECTOR_OPTIONS, (WWIDTH*0.2, WHEIGHT*0.6), autostart=True)

    running = True
    while running:
        for e in pygame.event.get():

            if e.type == pygame.QUIT:
                running = False

            if e.type == pygame.KEYDOWN:

                if e.key == pygame.K_DOWN:
                    sel.go_down()

                if e.key == pygame.K_UP:
                    sel.go_up()

                if e.key == pygame.K_RETURN:

                    if sel.get_selected_el() == "Exit":
                        running = False
                        continue

                    if sel.get_selected_el() == "Title screen":
                        pre_game_loop()
                        running = False
                        continue

        window.fill(colors.WHITE)
        window.blit(textures["game_over"], (WWIDTH*0.1, WHEIGHT*0.1))
        window.blit(text.get_surf("Score: "+str(score), colors.BLACK, 30), (WWIDTH*0.2, WHEIGHT*0.5))
        sel.show(window)
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    pre_game_loop()


pygame.quit()
