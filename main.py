import pygame

import consts
import events
from classes import bullet, player, enemy, totem
from consts import WHEIGHT, WWIDTH
from highscore.highscore import UserLoader
from utility import colors, text, selector, typer
from utility.texture_loader import textures

window = pygame.display.set_mode((WWIDTH, WHEIGHT))
clock = pygame.time.Clock()

pl = player.Player()
t = totem.Totem()
bullet_list = []
enemy_list = []
score = 0
user = UserLoader()

pygame.time.set_timer(events.ENEMY_SPAWN, consts.ENEMY_SPAWN_DELAY*1000)
pygame.display.set_caption("Igra za informatiko")
pygame.display.set_icon(textures["icon"])

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

        window.blit(textures["background"], (0, 0))
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
                    user.scoreup(score)
                    user.update_file()

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
    global user
    
    running = True

    # selector
    SELECTOR_OPTIONS = ["Igraj", "Prijava", "Izhod"]
    sel = selector.Selector(SELECTOR_OPTIONS, (WWIDTH*0.2, WHEIGHT*0.45), autostart=True, color=colors.WHITE)

    # login
    typing = False
    typing_field = typer.TypingField(start_text=user.get_name(), color=colors.WHITE, min_length=0)

    while running:

        for e in pygame.event.get():

            if not typing:  # testing
                if e.type == pygame.QUIT:
                    running = False

                if e.type == pygame.KEYDOWN:

                    if e.key == pygame.K_RETURN:
                        if sel.get_selected_el() == "Izhod":
                            running = False

                        if sel.get_selected_el() == "Prijava":
                            typing = True
                            continue

                        if sel.get_selected_el() == "Igraj":
                            running = False
                            main()
                            continue

                    if e.key == pygame.K_DOWN:
                        sel.go_down()

                    if e.key == pygame.K_UP:
                        sel.go_up()

                    if e.key == pygame.K_l:
                        typing = True

            else:  # type name

                if e.type == pygame.QUIT:
                    running = False

                if e.type == pygame.KEYDOWN:

                    if e.key == pygame.K_ESCAPE or e.key == pygame.K_RETURN:
                        typing = False
                        user = UserLoader(username=typing_field.get_text())

                    else:

                        try:
                            typing_field.type(e.key)
                        except typer.InvalidCharacterException:
                            pass

        window.blit(textures["background"], (0, 0))
        sel.show(window)
        window.blit(textures["logo"], (WWIDTH*0.1, WHEIGHT*0.1))
        window.blit(typing_field.get_surf(), (WWIDTH*0.1, WHEIGHT*0.8))
        if typing:
            window.blit(text.get_surf("Pritisni ESC za potrditev", colors.WHITE, 18), (WWIDTH*0.1, WHEIGHT*0.9))
        pygame.display.update()


def game_over():

    SELECTOR_OPTIONS = ["Naslovna stran", "Izhod"]

    sel = selector.Selector(SELECTOR_OPTIONS, (WWIDTH*0.1, WHEIGHT*0.6), autostart=True, color=colors.WHITE)

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

                    if sel.get_selected_el() == "Izhod":
                        running = False
                        continue

                    if sel.get_selected_el() == "Naslovna stran":
                        pre_game_loop()
                        running = False
                        continue

        window.blit(textures["background"], (0, 0))
        window.blit(textures["game_over"], (WWIDTH*0.1, WHEIGHT*0.1))
        window.blit(text.get_surf("Rezultat: "+str(score), colors.WHITE, 30), (WWIDTH*0.1, WHEIGHT*0.45))
        window.blit(text.get_surf("Najvisji rezultat: "+str(user.get_highscore()), colors.WHITE, 30), (WWIDTH*0.1, WHEIGHT*0.5))
        sel.show(window)
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    pre_game_loop()
    pygame.quit()
