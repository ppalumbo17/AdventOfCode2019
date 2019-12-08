import math

def fuelCalculation(fuel, sum):
  fuelNeeded = math.floor(int(fuel) / 3) - 2
  if (fuelNeeded < 0):
    return sum;
  else:
    return fuelCalculation(fuelNeeded, sum + fuelNeeded)

filename = 'input.txt'
file = open(filename)
fl = file.readlines()
sum = 0
for fuel in fl:
  sum += fuelCalculation(fuel, 0)
  print(sum)
print('Total sum is', sum)

