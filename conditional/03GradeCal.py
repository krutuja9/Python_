score  = 845

if score >= 101:
  print("verfiy your grade")
  exit()
if score >= 90:
   grade = "A"
elif score >= 80:
  grade = "B"
elif score >= 50:
  grade = "C"
else :
  grade = "F"
  
print("Grade: ", grade)
