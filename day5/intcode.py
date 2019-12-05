def run (input_val):
  memory = list()

  with open('./data/input.txt') as in_memory:
    for line in in_memory:
      memory.extend(list(int(x) for x in line.split(',')))

  position = 0
  output_val = -1
  while True:
    if position >= len(memory):
      raise Exception('Ran out of instructions at position {}'.format(position))

    instruction = memory[position]
    command = instruction % 100
    modes = [int(i) for i in str(instruction // 100)]
    modes.reverse()
    modes.extend([0] * (4 - len(modes)))

    if command == 99:
      break
    elif command == 1:
      if (position + 3) >= len(memory):
        raise Exception('Misisng arguments at position {}'.format(position))
      arg1 = memory[position + 1] if modes[0] else memory[memory[position + 1]]
      arg2 = memory[position + 2] if modes[1] else memory[memory[position + 2]]
      memory[memory[position + 3]] = arg1 + arg2
      position += 4
    elif command == 2:
      if (position + 3) >= len(memory):
        raise Exception('Misisng arguments at position {}'.format(position))
      arg1 = memory[position + 1] if modes[0] else memory[memory[position + 1]]
      arg2 = memory[position + 2] if modes[1] else memory[memory[position + 2]]
      memory[memory[position + 3]] = arg1 * arg2
      position += 4
    elif command == 3:
      if (position + 1) >= len(memory):
        raise Exception('Misisng arguments at position {}'.format(position))
      memory[memory[position + 1]] = input_val
      position += 2
    elif command == 4:
      if (position + 1) >= len(memory):
        raise Exception('Misisng arguments at position {}'.format(position))
      arg1 = memory[position + 1] if modes[0] else memory[memory[position + 1]]
      output_val = arg1
      position += 2
    else:
      raise Exception('Unknown opCode {} at position {}'.format(memory[position], position))

  return output_val

print(run(1))
