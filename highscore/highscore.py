u"""Ta datoteka je odgovorna za beleženje najvišjih doseženih točk."""


import json
import consts


def find_dict(l, key, value):
    """Find dict d from list l where key matches value. Return index"""
    for i, d in enumerate(l):
        if d[key] == value:
            return i


class User(object):

    def __init__(self, d):
        # d je dictionary, kot je zapisan v highscores.json
        self.name = d["name"]
        self.score = d["score"]
        self.changed = False

    def new_score(self, score):
        if self.score < score:
            self.changed = True
            self.score = score

    def get_dict(self):
        return dict(name=self.name, score=self.score)


class UserLoader(object):

    def __init__(self, filepath="highscore/", filename="highscores.json", username=""):
        if username == "":
            self.check_score = False
            self.username = ""
        else:
            self.check_score = True
            self.file = filepath+filename
            self.username = username

            fobj = open(self.file)
            self.d = json.load(fobj)
            fobj.close()

            self.user = None
            if self.username in self.d['users']:
                useri = find_dict(self.d['scores'], "name", self.username)
                self.user = User(self.d['scores'][useri])
            else:
                self.user = User(dict(name=self.username, score=0))
                self.d['users'].append(self.username)
                self.d['scores'].append(dict(name=self.username, score=0))
                
        if not consts.TRACK_HIGH_SCORES:
            self.check_score = False

    def scoreup(self, new_score):
        if self.check_score:
            self.user.new_score(new_score)

    def update_file(self):
        if self.check_score:
            self.d['scores'][find_dict(self.d['scores'], "name", self.username)] = self.user.get_dict()
            fobj = open(self.file, 'w')
            json.dump(self.d, fobj)

    def get_name(self):
        return self.username

    def get_highscore(self):
        if self.check_score:
            return max((self.user.score, self.d['scores'][find_dict(self.d['scores'], "name", self.username)]['score']))
        else:
            return None
