def calculate (r, unit, arr, n):
  if arr is None or n ==0:
    return -1

  totalFoodRequired = r * unit
  foodTillNow = 0
  
  for hourse in range (n):
    foodTillNow += arr[hourse]
    if (foodTillNow >= totalFoodRgit equired):
      return hourse + 1
  return 0

r = int(input("Enter number of rat:"))
unit = int(input("Enter the value of units:"))
n = int(input("number of elements in a array:"))
arr = list(map(int, input("List elements with space separated:").split()))