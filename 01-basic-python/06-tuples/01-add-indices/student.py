# Write your code here
def add_indices(xs):
  index = []
  for i in range(len(xs)):
    index.append(i)
  return list(zip(index, xs))

