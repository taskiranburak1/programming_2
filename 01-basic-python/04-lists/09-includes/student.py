# Write your code here
def includes(xs,ys):
  for y in ys[:]:
    if y in xs:
      ys.remove(y)
  return not ys