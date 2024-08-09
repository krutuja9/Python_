def calculate (r, unit, arr, n):
  if n == 0:
    returen -1
    
  totalFoodRequired = r * unit
  foodTillNow = 0;
  house = 0
  
  for house in range(n):
    foodTillNow += arr[house]
    if foodTillNow >= totalFoodRequired:
      break
  
  if totalFoodRequired > foodTillNow:
    return 0
  return house + 1
  
r = int(input("Enter rat Number "))
unit = int (input("Enter Unit "))
n = int(input("enter Number "))
arr = list (map(int, input("enter arra ").split()))
print (calculate (r, unit, arr, n))