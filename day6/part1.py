def run(filename):
  orbits = dict()
  with open(filename) as in_memory:
    for line in in_memory:
      (a, b) = (line.strip().split(')'))
      orbits[b] = a

  nodes = set(orbits.values()).union(orbits.keys())

  count = 0
  for n in nodes:
    x = n
    while x != 'COM':
      count += 1
      x = orbits[x]

  return count

assert run('./data/test1.txt') == 42
print(run('./data/orbits.txt'))
