# Write your code here

def coins(one,two,five,goal):
  for i in range(one + 1):
    for j in range(two + 1):
      for k in range(five + 1):
        sum = i*1 + j*2 + k*5
        if sum == goal:
          return True
  return False