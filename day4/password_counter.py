

def meets_criteria(password):
  return len(password) == 6 \
    and any(password[i] == password[i+1] for i in range(5)) \
    and all(password[i] <= password[i+1] for i in range(5))


assert meets_criteria('111111') == True
assert meets_criteria('223450') == False
assert meets_criteria('123789') == False

count=0
for i in range(278384, 824796):
  if meets_criteria(str(i)):
    count += 1

print(count)
