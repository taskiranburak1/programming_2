# Write your code here
def word_count(string):
  count = 1
  if len(string) == 0:
    return 0
  for i in range(len(string)):
    if string[i] == " ":
      count += 1
  return count 