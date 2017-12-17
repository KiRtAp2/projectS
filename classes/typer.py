import pygame
from utility import value_consts, text, colors


EVENTS_TO_CHARACTERS = {
    97: 'a',
    98: 'b',
    99: 'c',
    100: 'd',
    101: 'e',
    102: 'f',
    103: 'g',
    104: 'h',
    105: 'i',
    106: 'j',
    107: 'k',
    108: 'l',
    109: 'm',
    110: 'n',
    111: 'o',
    112: 'p',
    113: 'q',
    114: 'r',
    115: 's',
    116: 't',
    117: 'u',
    118: 'v',
    119: 'w',
    120: 'x',
    121: 'z',
    122: 'y',
    13: 'RETURN',
    32: ' ',
    46: '.',
    44: ',',
    8: 'BACKSPACE',
    48: '0',
    49: '1',
    50: '2',
    51: '3',
    52: '4',
    53: '5',
    54: '6',
    55: '7',
    56: '8',
    57: '9',
    45: '\'',
    304: None,  # shift
}


class TooLongException(Exception):
    pass


class TooShortException(Exception):
    pass


class InvalidCharacterException(Exception):
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
        try:
            return EVENTS_TO_CHARACTERS[self.id]
        except KeyError:
            raise InvalidCharacterException


class TypingField(object):
    """This is where the user can type. Experimental."""

    def __init__(self, min_length=1, max_length=value_consts.inf, color=colors.BLACK, text_size=30, display_ending=True):
        self.max_length = max_length
        self.min_length = min_length
        self.field = ""
        self.field_length = 0
        self.color = color
        self.text_size = text_size
        self.done = False
        self.display_ending = display_ending

    def type(self, event_key: int):
        """Call with event key that comes on event manager if you have no better use for the event"""
        print(event_key)
        c = TypingChar(event_key)
        if c.get_value() == 'RETURN':
            if self.field_length < self.min_length:
                raise TooShortException
            self.done = True
            return True

        elif c.get_value() == 'BACKSPACE':
            self.field = self.field[:self.field_length-1]
            self.field_length -= 1
            return True

        else:
            try:
                if self.field_length >= self.max_length:
                    raise TooLongException

                self.field += c.get_value()
                self.field_length += 1
                return True

            except TypeError:
                return False

    def get_surf(self):
        """Return surface to blit to screen"""
        return text.get_surf(
            self.field+'|' if self.display_ending else self.field,
            self.color,
            self.text_size
        )
