# Write your code here
def double_dict_values(dictionary):
  result = {}
  for k,v in dictionary.items():
    result[k] = 2 * v
  return result