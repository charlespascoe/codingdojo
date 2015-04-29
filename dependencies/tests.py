import dep
import sys
import unittest


def test(actual, expected):
    assert actual == expected, 'Got {}, expected {}'.format(actual, expected)

if __name__ == '__main__':
    packages = {}

    with open('packages.txt') as f:
        for line in f.read().split('\n'):
            name, deps = line.split(' -> ')
            packages[name] = deps.split(' ')

    d = dep.Dependencies(packages);

    test(d.get_dependencies('swingui'), ['extensions', 'framework', 'runner'])
    test(d.get_dependencies('awtui'), ['framework', 'runner'])
    test(d.get_dependencies('unknown'), [])

    print('Tests passed')
