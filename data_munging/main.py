import re


def min_temp(data):
  m = [m for m in [re.findall('(?:\s+(\d+))', line) for line in data] if len(m) > 1]
  x = min(m, key=lambda x: abs(int(x[1])-int(x[2])))
  return int(x[0]), abs(int(x[1])-int(x[2]))

def min_goal(data):
  m = [m.groups() for m in [re.search('([A-Za-z_]+)(?:\s+\d+)+\s+(\d+)\s+-\s+(\d+)', line) for line in data] if m]
  x = min(m, key=lambda x: abs(int(x[1])-int(x[2])))
  return x[0], abs(int(x[1])-int(x[2]))


if __name__ == '__main__':
  with open('weather.dat') as f:
    weather = f.read().split('\n')

  day, difference = min_temp(weather)

  assert day == 14, 'incorrect day: {}'.format(day)
  assert difference == 2, 'incorrect difference: {}'.format(difference)


  with open('football.dat') as f:
    football = f.read().split('\n')

  team, difference = min_goal(football)

  assert team == 'Aston_Villa', 'incorrect team: {}'.format(team)
  assert difference == 1, 'incorrect difference: {}'.format(difference)
