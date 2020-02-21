# input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,10,23,2,10,23,27,1,27,6,31,1,13,31,35,1,13,35,39,1,39,10,43,2,43,13,47,1,47,9,51,2,51,13,55,1,5,55,59,2,59,9,63,1,13,63,67,2,13,67,71,1,71,5,75,2,75,13,79,1,79,6,83,1,83,5,87,2,87,6,91,1,5,91,95,1,95,13,99,2,99,6,103,1,5,103,107,1,107,9,111,2,6,111,115,1,5,115,119,1,119,2,123,1,6,123,0,99,2,14,0,0]
input = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,10,23,2,10,23,27,1,27,6,31,1,13,31,35,1,13,35,39,1,39,10,43,2,43,13,47,1,47,9,51,2,51,13,55,1,5,55,59,2,59,9,63,1,13,63,67,2,13,67,71,1,71,5,75,2,75,13,79,1,79,6,83,1,83,5,87,2,87,6,91,1,5,91,95,1,95,13,99,2,99,6,103,1,5,103,107,1,107,9,111,2,6,111,115,1,5,115,119,1,119,2,123,1,6,123,0,99,2,14,0,0]
# input = [2,4,4,5,99,0]
# Loop through with index
# Create slice array of index to index + 4
# Check operand 1, 2, or 99
# return input at 0
def add(tmp):
  input[tmp[3]] = input[tmp[1]] + input[tmp[2]]

def multiply(tmp):
  input[tmp[3]] = input[tmp[1]] * input[tmp[2]]

def end(tmp):
  print('Ended with final initial value of', input[0])
  quit()

for i in range(0,len(input),4):
  tmp = input[i:i+4]
  op = tmp[0]
  switcher = {
    1: add,
    2: multiply,
    99: end,
  }
  func = switcher.get(op)
  if (func):
    func(tmp)
    print(input)
  else:
    print('Something went wrong at position', i)
  # switch(op) {
  #   case 1:
  #     input[tmp[3]] = input[tmp[1]] + input[tmp[2]]
  #     break
  #   case 2:
  #     input[tmp[3]] = input[tmp[1]] * input[tmp[2]]
  #     break
  #   case 99:
  #     print('You have broken from the op computer with final initial value of', input[0])
  #     break
  #   default:
  #     print('Something went wrong at position', i)
  #     break
  # };

print(input)