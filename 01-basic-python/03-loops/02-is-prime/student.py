# Write your code here

def is_prime(n):
  if n == 0 or n == 1:
    return False
  if n == 2:
    return True
  count = n//2 +1
  while count != 1:
    if n % count == 0:
      return False
    else:
      count -= 1
  return True
  