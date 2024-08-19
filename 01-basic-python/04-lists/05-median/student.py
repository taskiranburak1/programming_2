# Write your code here
def median(ns):
  ns.sort()
  if len(ns) % 2 == 1:
    return ns[len(ns)//2]
  else:
    sum = ns[len(ns)//2] + ns[(len(ns)//2)-1]
    return sum / 2