

def meets_criteria(password):
  return len(password) == 6 \
    and any(password[i] == password[i+1] \
      and password[i] not in password[0:i] \
      and password[i] not in password[i+2:6] for i in range(5)) \
    and all(password[i] <= password[i+1] for i in range(5))


assert meets_criteria('112233') == True
assert meets_criteria('123444') == False
assert meets_criteria('111122') == True

count=0
for i in range(278384, 824796):
  if meets_criteria(str(i)):
    count += 1

print(count)
