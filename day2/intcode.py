def run (noun, verb):
  memory = list()

  with open('./data/input.txt') as in_memory:
    for line in in_memory:
      memory.extend(list(int(x) for x in line.split(',')))

  memory[1] = noun
  memory[2] = verb

  position = 0
  while True:
    if position >= len(memory):
      raise Exception('Ran out of instructions at position {}'.format(position))

    if memory[position] == 99:
      break
    elif memory[position] == 1:
      if (position + 3) >= len(memory):
        raise Exception('Misisng arguments at position {}'.format(position))
      memory[memory[position + 3]] = memory[memory[position + 1]] + memory[memory[position + 2]]
    elif memory[position] == 2:
      if (position + 3) >= len(memory):
        raise Exception('Misisng arguments at position {}'.format(position))
      memory[memory[position + 3]] = memory[memory[position + 1]] * memory[memory[position + 2]]
    else:
      raise Exception('Unknown opCode {} at position {}'.format(memory[position], position))
    position = position + 4

  return memory[0]

print(run(12, 2))

target = 19690720
for noun in range(100):
  for verb in range(100):
    result = run(noun, verb)
    if result == target:
      print(noun, verb, target)

