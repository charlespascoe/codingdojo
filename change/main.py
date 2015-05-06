coins = [200,100,50,20,10,5,2,1]

def change(n):
    l = []
    for coin in coins:
        if n >= coin:
            l.extend([coin] * (n // coin))
            n %= coin
    return l

def test(actual, expected):
    assert actual == expected, 'Expected: {}, Actual: {}'.format(expected, actual)


test(change(73), [50,20,2,1])
test(change(100), [100])
test(change(173), [100,50,20,2,1])

