import math
filename = 'input.txt'
file = open(filename)
fl = file.readlines()
sum = 0
for fuel in fl:
  sum += (math.floor(int(fuel) / 3) - 2)
  print(sum)
print('Total sum is', sum)