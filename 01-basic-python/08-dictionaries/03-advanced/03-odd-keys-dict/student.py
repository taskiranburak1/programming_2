# Write your code here
def odd_keys_dict(dictionary):
  result = {}
  for key, value in dictionary.items():
    if key % 2 == 1:
      result[key] = value
  return result