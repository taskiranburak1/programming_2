# Write your code here
"""
def is_increasing(ns):
  ms = ns[1:]
  compare = list(zip(ns, ms))
  for i in range(len(compare)):
    if compare[i][0] > compare[i][1]:
      return False
  return True
"""

def is_increasing(ns):
  for (a,b) in zip(ns, ns[1:]):
    if a > b:
      return False
  return True