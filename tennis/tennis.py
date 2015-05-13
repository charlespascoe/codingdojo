
class TennisGame:
    def __init__(self, player_names, serving_player=0):
        self.player_names = player_names
        self.serving_player = serving_player
        self.scores = [0, 0]

    def point(self, scoring_player):
        if self.scores[scoring_player] < 30:
            self.scores[scoring_player] += 15
        elif self.scores[not scoring_player] == 50:
            self.scores[not scoring_player] -= 10
        else:
            self.scores[scoring_player] += 10

    def _score(self, n):
        if n == 0:
            return 'love'
        else:
            return str(n)

    @property
    def score(self):
        if max(self.scores) - min(self.scores) >= 20 and max(self.scores) > 40:
            return self.player_names[self.scores.index(max(self.scores))] + ' wins'


        if self.scores[0] == self.scores[1]:
            if self.scores[0] == 40:
                return 'deuce'
            return '{} all'.format(self._score(self.scores[0]))
        elif self.scores[0] <= 40 and self.scores[1] <= 40:
            return '{}-{}'.format(self._score(self.scores[self.serving_player]), self._score(self.scores[not self.serving_player]))
        else:
            return 'advantage {}'.format(self.player_names[self.scores.index(max(self.scores))])
