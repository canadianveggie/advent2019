import math

def fuel_requirement(mass):
  return max(math.floor(mass / 3) - 2, 0);

fuel = 0
with open('./data/module_mass.txt') as module_mass:
  for mass in module_mass:
    fuel += fuel_requirement(int(mass))

print(fuel)

