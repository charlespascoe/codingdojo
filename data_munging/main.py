import re


def parse(data):
  m = [m for m in [re.findall('(?:\s+(\d+))', line) for line in data] if len(m) > 1]
  x = min(m, key=lambda x: abs(int(x[1])-int(x[2])))
  return int(x[0]), (int(x[1])-int(x[2]))


if __name__ == '__main__':
  with open('weather.dat') as f:
    data = f.read().split('\n')

  print(parse(data))
