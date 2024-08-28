def linear_Search(arr, target):
  for index in range(len(arr)):
    if arr[index] == target:
      return index
  
  return -1

arr = list(map(int, input("Enter the element of the array separated by speace").split()))
target = int(input("enter target val: "))

result = linear_Search(arr, target)

if result != -1:
  print(f"Element found of index {result}")
else:
  print("Elemnt not found in the array")