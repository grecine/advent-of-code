import os


def read_input(fname):
    day_dir = os.path.realpath(__file__).split('/')[:-1]
    fname = os.path.join('/', *day_dir, fname)

    data = []
    with open(fname) as f:
        data.extend(line.strip() for line in f)
    return data


def char2val(c):
    """
    Lowercase item types a through z have values 1 through 26.
    Uppercase item types A through Z have values 27 through 52.
    """
    lowercase_origin = 96
    uppercase_origin = 38
    return (ord(c) - uppercase_origin) if c.isupper() else (ord(c) - lowercase_origin)


class rpss:
    """
    Rock, Paper, Scissors game and the inverse game
    1) The game: You provide your hand and the opponent's hand and win, lose, draw is returned
    2) The inverse game: You provide your opponent's hand and if you should win, lose, or draw,
       and you needed hand is returned
    """
    def __init__(self):
        self.rock = 'rock'
        self.paper = 'paper'
        self.scissors = 'scissors'
        self.win = 'win'
        self.lose = 'lose'
        self.draw = 'draw'

    def play(self, turn):
        """
        Rock Paper Scissors, shoot!
        """
        them = turn[0]
        you = turn[1]
        if you == them:
            return self.draw
        elif you == self.rock:
            return self.win if them == self.scissors else self.lose
        elif you == self.paper:
            return self.win if them == self.rock else self.lose
        elif you == self.scissors:
            return self.win if them == self.paper else self.lose

    def play_inv(self, turn):
        them = turn[0]
        res = turn[1]
        if res == self.draw:
            return them
        elif res == self.win:
            if them == self.rock:
                return self.paper
            if them == self.paper:
                return self.scissors
            if them == self.scissors:
                return self.rock
        elif res == self.lose:
            if them == self.rock:
                return self.scissors
            if them == self.paper:
                return self.rock
            if them == self.scissors:
                return self.paper
