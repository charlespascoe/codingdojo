import tennis

PLAYER1 = 0
PLAYER2 = 1

def test(actual, exp):
    assert actual == exp, 'Expected: {}, Actual: {}'.format(exp, actual)

if __name__ == '__main__':
    game = tennis.TennisGame(['Alice', 'Bob'])

    test(game.score, 'love all')

    game.point(PLAYER1)
    test(game.scores[PLAYER1], 15)
    test(game.score, '15-love')

    game.point(PLAYER2)
    test(game.scores[PLAYER2], 15)
    test(game.score, '15 all')

    game.point(PLAYER2)
    test(game.score, '15-30')

    game.point(PLAYER2)
    test(game.scores[PLAYER2], 40)
    test(game.score, '15-40')

    game.point(PLAYER1)
    game.point(PLAYER1)
    test(game.score, 'deuce')

    game.point(PLAYER1)
    test(game.score, 'advantage Alice')

    game.point(PLAYER2)
    test(game.score, 'deuce')

    game.point(PLAYER2)
    test(game.score, 'advantage Bob')

    game.point(PLAYER2)
    test(game.score, 'Bob wins')

    game2 = tennis.TennisGame(['Alice', 'Bob'], PLAYER2)

    test(game2.score, 'love all')

    game2.point(PLAYER1)
    test(game2.score, 'love-15')


    game2.point(PLAYER1)
    game2.point(PLAYER1)




    print('Success!')

