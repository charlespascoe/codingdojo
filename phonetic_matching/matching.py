import sys
import re

discarded = 'AEIHOUWY'

categories = ['AEIOU', 'CGJKQSXYZ', 'BFPVW', 'DT', 'MN', 'H', 'L', 'R']


def categorise(name):
    name = re.sub('[^A-Z]', '', name.upper())
    letters = [name[0]]

    for l in name[1:]:
        if l not in discarded:
            letters.append(l)

    cname = []

    for letter in letters:
        for ci, cat in enumerate(categories):
            if letter in cat:
                cletter = ci
                break

        if len(cname) == 0 or cletter != cname[-1]:
            cname.append(cletter)

    return cname


def match(input_names, sample_list):
    names = []

    cinput_names = []
    for name in input_names:
        cinput_names.append(categorise(name))

    for sample_name in sample_list:
        csample_name = categorise(sample_name)
        if csample_name in cinput_names:
            names.append(sample_name)

    return names


if __name__ == '__main__':
    with sys.stdin as f:
        sample_list = f.read().split('\n')

    for name in match(sys.argv[1:], sample_list):
        print(name)
