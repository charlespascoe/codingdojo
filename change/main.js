var assert = require('assert');

var coins = [200,100,50,20,10,5,2,1];

function change (n) {
    var l = [];
    coins.forEach(function (coin) {
        if (n >= coin) {
            for (var i = 0; i < parseInt(n/coin); i++) l.push(coin);
            n = n % coin;
        }
    });
    return l;
}

function test (actual, expected) {
    assert.deepEqual(actual, expected, 'Expected: ' + expected + ', Actual: ' + actual);
}

test(change(73), [50,20,2,1]);
test(change(100), [100]);
test(change(173), [100,50,20,2,1]);

