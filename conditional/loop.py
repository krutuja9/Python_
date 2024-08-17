# n = int(input("Enter a number: "))
# for i in range(1,11):
#   print(f"{n} X {i} = {n*i}")
  
# Prime number
# n = int(input("Enter number : "))
# for i in range(2,n):
#   if(n%i )==0:
#     print("number is not prime")
#     break
# else:
#     print("NUmber is prime")

#print sum

# n=int(input("Enter the number: "))
# i =1
# sum = 0
# while(i<n):
#   sum += i
#   i+=1 
  
# print(sum)


# Factorial
# n = int(input("enter the number: "))
# product = 1
# for i in range(1, n+1):
#   product = product * i
  
# print(f"the factorial of {n} is {product}")

# star
# n = int(input("enter the number: "))

# for i in range(1, n+1):
#   print(" "* (n-i), end=" ")
#   print("*"*(2*i-1), end=" ")
#   print(" ")
'''  *  
    ***
   *****
  *******
 ********* 
 '''
 

# n = int(input("enter the number: "))

# for i in range(1, n+1):
#   print("*"* i, end="")
#   print("")

# *
# **
# ***
# ****
# *****


n = int(input("enter the number: "))

for i in range(1, n+1):
  if (i==1 or i==n):
    print("*"* n, end="")
  else:
    print("*", end="")
    print(" "*(n-2), end="")
    print("*", end="")
  print("")
  