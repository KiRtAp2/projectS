import pygame
from utility import value_consts, text, colors


class TooLongException(Exception):
    pass


class TooShortException(Exception):
    pass


class TypingChar(object):
    """Crka za pisanje. Shranjuje pygame.event kot svojo vrednost"""

    def __init__(self, eventid: int):
        self.id = eventid

    def __str__(self):
        return chr(self.get_value())

    def __repr__(self):
        return chr(self.get_value())

    def get_value(self):
        return self.id


class TypingField(object):

    def __init__(self, min_length=1, max_length=value_consts.inf, color=colors.BLACK, text_size=30):
        self.max_length = max_length
        self.min_length = min_length
        self.field = ""
        self.field_length = 0
        self.color = color
        self.text_size = text_size
        self.done = False

    def type(self, event_key):
        c = TypingChar(event_key)
        if c.get_value() == 13:
            if self.field_length < self.min_length:
                raise TooShortException
            self.done = True
            return True

        elif c.get_value() == 8:
            self.field = self.field[:self.field_length-1]
            self.field_length -= 1
            return True

        elif c.get_value() == 32:
            self.field += " "
            self.field_length += 1

        elif 97 <= c.get_value() <= 122:
            if self.field_length >= self.max_length:
                raise TooLongException

            self.field += chr(c.get_value())
            self.field_length += 1
            return True

        return False

    def get_surf(self):
        return text.get_surf(self.field, self.color, self.text_size)
