# Write your code here
def contains_duplicates(xs):
  for i in range(len(xs)):
    for j in range(len(xs)):
      if i != j and xs[i] == xs[j]:
        return True
  return False