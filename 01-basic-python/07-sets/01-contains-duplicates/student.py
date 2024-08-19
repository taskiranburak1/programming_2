# Write your code here
def contains_duplicates(xs):
  a = len(xs)
  b = len(set(xs))
  if a == b:
    return False
  return True
# return len(set(xs)) != len(xs)