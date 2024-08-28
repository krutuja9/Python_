# def intTostr(i):
#   digits = '0123456789'
#   if i == 0:
#     return "0"
#   result = ""
#   while i >0:
#     result = digits[i%10] + result
#     i = i//10
#   return result

# result = intTostr(1234)
# print(result) 

num =123;
num_Str = str(num)

print("the integer as a string is:", num_Str)
print("type of num_Str", type(num_Str))