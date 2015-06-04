import re


def min_col(d, r):
  m = [m.groups() for m in [re.search(r, l) for l in d] if m]
  x = min(m, key=lambda x: abs(int(x[1])-int(x[2])))
  return x[0], abs(int(x[1])-int(x[2]))


if __name__ == '__main__':
  with open('weather.dat') as f:
    weather = f.read().split('\n')

  day, difference = min_col(weather, r'\s+(\d+)\s+(\d+)\s+(\d+)')

  print('min temp difference: day {}, diff {}'.format(day, difference))

  assert int(day) == 14, 'incorrect day: {}'.format(day)
  assert difference == 2, 'incorrect difference: {}'.format(difference)


  with open('football.dat') as f:
    football = f.read().split('\n')

  team, difference = min_col(football, r'([A-Za-z_]+)(?:\s+\d+)+\s+(\d+)\s+-\s+(\d+)')

  print('min goal difference: team {}, diff {}'.format(team, difference))

  assert team == 'Aston_Villa', 'incorrect team: {}'.format(team)
  assert difference == 1, 'incorrect difference: {}'.format(difference)
