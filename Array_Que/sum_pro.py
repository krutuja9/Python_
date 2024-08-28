L = [1,3,3,4]

sum =0
for i in L:
  sum = sum + i
print(sum)


pro = 1
for i in L:
  pro = pro * i; 
print(pro)

  
# Printing in Pairs
for i in L:
  for j in L:
    print('({},{})'.format(i,j))