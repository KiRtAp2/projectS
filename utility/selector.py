from utility import text
from utility import colors


class AlreadyStartedException(Exception):
    pass


class NotStartedException(Exception):
    pass


class Selector(object):
    
    def __init__(self, choices, startpos, fontsize=35, autostart=False, color=colors.BLACK):
        self.choices = choices
        self.x, self.y = startpos
        self.font_size = fontsize
        self.selected = None
        self.started = False
        self.color = color
        if autostart: 
            self.start_choosing()

    def show(self, window):
        curr_x = self.x
        curr_y = self.y

        for i, c in enumerate(self.choices):
            window.blit(text.get_surf(str(c), self.color, self.font_size), (curr_x, curr_y))
            if self.selected == i:
                window.fill(self.color, (curr_x-20, curr_y+self.font_size*0.2, 10, 10))
            curr_y += self.font_size + 2

    def start_choosing(self):
        if self.started:
            raise AlreadyStartedException
        
        self.started = True
        self.selected = 0

    def go_down(self):
        if not self.started:
            raise NotStartedException

        self.selected += 1
        if self.selected == len(self.choices):
            self.selected = 0

    def go_up(self):
        if not self.started:
            raise NotStartedException

        self.selected -= 1
        if self.selected < 0:
            self.selected = len(self.choices)-1

    def get_selected_num(self):
        if not self.started:
            raise NotStartedException

        return self.selected

    def get_selected_el(self):
        if not self.started:
            raise NotStartedException

        return self.choices[self.selected]

    def get_started(self):
        return self.started
