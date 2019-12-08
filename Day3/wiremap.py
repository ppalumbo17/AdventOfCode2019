
# Right is positive x
# Up is positive y
# Left is negative x
# Down is negative y
# Make a map of points for first wire
# Compare with map of second wire creating list of convergence
# Loop through convergence comparing distances

# Setup
import csv
import sys
import math
import copy
# inputData = [['R75','D30','R83','U83','L12','D49','R71','U7','L72'],['U62','R66','U55','R34','D71','R55','D58','R83']]
inputData = [['R8','U5','L5','D3'],['U7','R6','D4','L4']]
# with open('input.txt', mode='r') as csv_file:
#   csv_reader = csv.reader(csv_file);
#   for row in csv_reader:
#     inputData.append(row)

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def getX(self):
    return self.x

  def getY(self):
    return self.y

  def print(self):
    return str(self.y) + ', ' + str(self.x)

def move(cp, action):
  direction = action[0]
  distance = int(action[1:])
  if direction == 'R':
    cp.x = cp.getX() + distance
  elif direction == 'U':
    cp.y = cp.getY() + distance
  elif direction == 'L':
    cp.x = cp.getX() - distance
  elif direction == 'D':
    cp.y = cp.getY() - distance
  return cp

def createWireSet(input):
  wireMap = set()
  currentPoint = Point(0, 0)
  for route in input:
    newPoint = copy.copy(currentPoint)
    newPoint = move(newPoint, route)
    # wireMap.add((currentPoint.getX(), currentPoint.getY()))
    wireMap.update(findAllPointsBetween(currentPoint, newPoint))
    currentPoint = copy.copy(newPoint)
  return wireMap

def findAllPointsBetween(p1, p2):
  print('P1', p1.print(), 'P2', p2.print())
  points = set()
  xValue = True if p1.getX() == p2.getX() else False
  lesser = p1.getX() if p1.getX() < p2.getX() else p2.getX() if not xValue else p1.getY() if p1.getY() < p2.getY() else p2.getY()
  # lesser =
  greater = p1.getX() if p1.getX() > p2.getX() else p2.getX() if not xValue else p1.getY() if p1.getY() > p2.getY() else p2.getY()
  # greater =
  print('Lesser', lesser)
  print('Greater', greater)
  if xValue:
    for y in range(lesser, greater):
      points.add((p1.getX(), y))
  else:
    for x in range(lesser, greater):
      points.add((x, p1.getY()))
  print('Points are', points)
  return points

def getMinDistance(input):
  minDistance = sys.maxsize
  for tup in input:
    currentDistance = math.fabs(tup[0]) + math.fabs(tup[1])
    minDistance = min(currentDistance, minDistance)
  return minDistance


# print(createWireSet(inputData[0]))
s1 = createWireSet(inputData[0])
print('S1', s1)
s2 = createWireSet(inputData[1])
print('S2', s2)
s3 = s1.intersection(s2)
print('S3', s3)
print(getMinDistance(s3))