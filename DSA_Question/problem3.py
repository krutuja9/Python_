def CheckPassword(password: str) -> int:
  if len(password) < 4:
    return 0
  
  if password[0].isdigit():
    return 0

  has_digit = False
  has_upper = False
  
  for char in password:
    if char in (' ','/'):
      return 0
    if char.isdigit():
      has_digit = True
    
    if char.isupper():
      has_upper = True
      
  if has_digit and has_upper:
    return 1
  
  return 0

userinput = input()
print(CheckPassword(userinput))