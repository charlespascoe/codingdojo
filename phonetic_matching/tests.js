var matching = require('./matching')
,   fs = require('fs');

var sample_names, data, tests = {};

data = fs.readFileSync('tests.txt');
data.toString().split('\n').forEach(function (line) {
    var pair = line.split(': ');
    var name = pair[0], output = pair[1];
    tests[name] = output.split(', '); 
});

data = fs.readFileSync('names2.txt');
sample_names = data.toString().split('\n');

for (var test_name in tests) {
    var expected = tests[test_name];
    var actual = matching.match([test_name], sample_names);
    var result = (JSON.stringify(expected) == JSON.stringify(actual));
    
    console.log(test_name + ': ' + result);
    if (!result) console.log('Expected: ' + expected + ', Actual: ' + actual);
}
