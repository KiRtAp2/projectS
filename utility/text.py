import pygame


def get_surf(text: str, color: tuple, size: int):
    font = pygame.font.SysFont("consolas", size)
    return font.render(text, True, color)
