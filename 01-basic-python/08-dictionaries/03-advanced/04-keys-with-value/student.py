# Write your code here
def keys_with_value(dictionary, value):
  result = []
  for k,y in dictionary.items():
    if y == value:
      result.append(k)
  return result