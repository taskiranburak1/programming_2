# Write your code here
def cakes (eggs, butter, flour):
  cake1 = eggs // 5
  cake2 = butter // 250
  cake3 = flour // 250

  max_amount_cakes = min(cake1, cake2, cake3)
  return max_amount_cakes