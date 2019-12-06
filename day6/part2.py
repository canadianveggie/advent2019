def run(filename):
  orbits = dict()
  with open(filename) as in_memory:
    for line in in_memory:
      (a, b) = (line.strip().split(')'))
      orbits[b] = a

  nodes = set(orbits.values()).union(orbits.keys())

  myOrbits = list()
  x = 'YOU'
  while x != 'COM':
    x = orbits.get(x)
    myOrbits.append(x)

  santaOrbits = list()
  x = 'SAN'
  while x != 'COM':
    x = orbits.get(x)
    santaOrbits.append(x)

  commonPoint = [x for x in myOrbits if x in santaOrbits][0]

  return myOrbits.index(commonPoint) + santaOrbits.index(commonPoint)

assert run('./data/test2.txt') == 4
print(run('./data/orbits.txt'))
