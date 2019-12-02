

codes = list()

with open('./data/input.txt') as inputcodes:
  for line in inputcodes:
    codes.extend(list(int(x) for x in line.split(',')))

position = 0
while True:
  if position >= len(codes):
    raise Error('Ran out of instructions at position {}'.format(position))

  if codes[position] == 99:
    break

  if codes[position] == 1:
    if (position + 3) >= len(codes):
      raise Error('Misisng arguments at position {}'.format(position))
    codes[codes[position + 3]] = codes[codes[position + 1]] + codes[codes[position + 2]]

  if codes[position] == 2:
    if (position + 3) >= len(codes):
      raise Error('Misisng arguments at position {}'.format(position))
    codes[codes[position + 3]] = codes[codes[position + 1]] * codes[codes[position + 2]]

  position = position + 4


with open('./data/output.txt', 'w') as outputcodes:
  outputcodes.write(','.join(str(x) for x in codes))
