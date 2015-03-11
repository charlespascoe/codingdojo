import matching

tests = {}

with open('tests.txt') as f:
    for line in f.read().split('\n'):
        name, output = line.split(': ')
        tests[name] = output.split(', ')

with open('names2.txt') as f:
    sample_names = f.read().split('\n')

for test_name in tests:
    expected = tests[test_name]
    actual = matching.match([test_name], sample_names)
    result = (expected == actual)
    print('{}: {}'.format(test_name, result))
    if not result:
        print('Expected: {}, Actual: {}'.format(expected, actual))
