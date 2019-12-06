standary_memory = list()
with open('./data/input.txt') as in_memory:
  for line in in_memory:
    standary_memory.extend(list(int(x) for x in line.split(',')))

def run (mem, input_val, verbose=False):
  p = 0
  output_val = -1
  while True:
    if p >= len(mem):
      raise Exception('Ran out of instructions at position {}'.format(p))

    instruction = mem[p]
    command = instruction % 100
    modes = [int(i) for i in str(instruction // 100)]
    modes.reverse()
    modes.extend([0] * (4 - len(modes)))

    if command == 99: # HALT
      break
    elif command == 1: # ADD arg3 = arg2 + arg1
      [a1, a2, a3] = mem[p+1: p+4]
      arg1 = a1 if modes[0] else mem[a1]
      arg2 = a2 if modes[1] else mem[a2]
      if verbose:
        print(f'{p:4}: \t {instruction:6} {a1:5} {a2:5} {a3:5} =>\tADD {a3} = {arg1} + {arg2}')
      mem[a3] = arg1 + arg2
      p += 4
    elif command == 2: # MULT arg3 = arg2 * arg1
      [a1, a2, a3] = mem[p+1: p+4]
      arg1 = a1 if modes[0] else mem[a1]
      arg2 = a2 if modes[1] else mem[a2]
      if verbose:
        print(f'{p:4}: \t {instruction:6} {a1:5} {a2:5} {a3:5} =>\tMULT {a3} = {arg1} * {arg2}')
      mem[a3] = arg1 * arg2
      p += 4
    elif command == 3: # INPUT arg1 = input_val
      [a1] = mem[p+1: p+2]
      if verbose:
        print(f'{p:4}: \t {instruction:6} {a1:5}             =>\tINPUT {a1} = {input_val}')
      mem[a1] = input_val
      p += 2
    elif command == 4: # OUTPUT output_val = arg1
      [a1] = mem[p+1: p+2]
      arg1 = a1 if modes[0] else mem[a1]
      if verbose:
        print(f'{p:4}: \t {instruction:6} {a1:5}           =>\tOUTPUT {arg1}')
      output_val = arg1
      p += 2
    elif command == 5: # JUMP_IF if arg1, p = arg2
      [a1, a2] = mem[p+1: p+3]
      arg1 = a1 if modes[0] else mem[a1]
      arg2 = a2 if modes[1] else mem[a2]
      if verbose:
        print(f'{p:4}: \t {instruction:6} {a1:5} {a2:5}       =>\tJUMP_IF {arg1} to {arg2}')
      if arg1:
        p = arg2
      else:
        p += 3
    elif command == 6: # JUMP_NOT_IF if !arg1, p = arg2
      [a1, a2] = mem[p+1: p+3]
      arg1 = a1 if modes[0] else mem[a1]
      arg2 = a2 if modes[1] else mem[a2]
      if verbose:
        print(f'{p:4}: \t {instruction:6} {a1:5} {a2:5}       =>\tJUMP_NOT_IF {arg1} to {arg2}')
      if not arg1:
        p = arg2
      else:
        p += 3
    elif command == 7: # IF_LESS arg3 = arg1 < arg 2
      [a1, a2, a3] = mem[p+1: p+4]
      arg1 = a1 if modes[0] else mem[a1]
      arg2 = a2 if modes[1] else mem[a2]

      if verbose:
        print(f'{p:4}: \t {instruction:6} {a1:5} {a2:5} {a3:5} =>\tIF_LESS {a3} = {arg1} < {arg2}')
      if arg1 < arg2:
        mem[a3] = 1
      else:
        mem[a3] = 0
      p += 4
    elif command == 8: # EQUALS arg3 = arg1 == arg 2
      [a1, a2, a3] = mem[p+1: p+4]
      arg1 = a1 if modes[0] else mem[a1]
      arg2 = a2 if modes[1] else mem[a2]

      if verbose:
        print(f'{p:4}: \t {instruction:6} {a1:5} {a2:5} {a3:5} =>\tEQUALS {a3} = {arg1} == {arg2}')
      if arg1 == arg2:
        mem[a3] = 1
      else:
        mem[a3] = 0
      p += 4
    else:
      raise Exception('Unknown instruction {} at position {}'.format(instruction, p))

  return output_val

# Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
assert run([3,9,8,9,10,9,4,9,99,-1,8], 0) == 0
assert run([3,9,8,9,10,9,4,9,99,-1,8], 7) == 0
assert run([3,9,8,9,10,9,4,9,99,-1,8], 8) == 1
assert run([3,9,8,9,10,9,4,9,99,-1,8], 9) == 0
# Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
assert run([3,9,7,9,10,9,4,9,99,-1,8], 0) == 1
assert run([3,9,7,9,10,9,4,9,99,-1,8], 7) == 1
assert run([3,9,7,9,10,9,4,9,99,-1,8], 8) == 0
assert run([3,9,7,9,10,9,4,9,99,-1,8], 9) == 0
# Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
assert run([3,3,1108,-1,8,3,4,3,99], 0) == 0
assert run([3,3,1108,-1,8,3,4,3,99], 7) == 0
assert run([3,3,1108,-1,8,3,4,3,99], 8) == 1
assert run([3,3,1108,-1,8,3,4,3,99], 9) == 0
# Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
assert run([3,3,1107,-1,8,3,4,3,99], 0) == 1
assert run([3,3,1107,-1,8,3,4,3,99], 7) == 1
assert run([3,3,1107,-1,8,3,4,3,99], 8) == 0
assert run([3,3,1107,-1,8,3,4,3,99], 9) == 0
# Using position mode, take an input, then output 0 if the input was zero or 1 if the input was non-zero:
assert run([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], -1) == 1
assert run([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 0) == 0
assert run([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 1) == 1
# Using immediate mode, take an input, then output 0 if the input was zero or 1 if the input was non-zero:
assert run([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], -1) == 1
assert run([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 0) == 0
assert run([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 1) == 1
# uses an input instruction to ask for a single number. The program will then output 999 if the input value is below 8, output 1000 if the input value is equal to 8, or output 1001 if the input value is greater than 8.
assert run([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
  1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
  999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], 1) == 999
assert run([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
  1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
  999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], 7) == 999
assert run([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
  1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
  999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], 8) == 1000
assert run([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
  1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
  999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], 9) == 1001

print(run(standary_memory.copy(), 1, verbose=True))

print(run(standary_memory.copy(), 5, verbose=True))
