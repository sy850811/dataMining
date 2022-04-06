import itertools
def uniqun(arr,index): # finds unique values
  s = []
  for i in arr:
    if i[index] not in s:
      s.append(i[index])
  return s

def findFirst(arr, n, x): # finds the occurance index
    count = 0
    isX = False
    for i in range(n):
        if (arr[i] == x):
            isX = True
        elif (arr[i] < x):
            count += 1
 
    return -1 if(isX == False) else count

def aggregate(input,measureIndex = 4,sum = 0):#aggregates the sales values for a partition
  for i in input:
    sum += i[measureIndex]
  return sum

def uniq(arr,index):# finds unique value for a dimention
  s = []
  for i in arr:
    if i[index] not in s:
      s.append(i[index])
  s.sort()
  return s

def findCardinality(input,numDims,s):#find unique possible values for all the dimentions 
  cardi = []
  for i in range(numDims):
    if s==True:
      possibleValues = uniq(input,i)
    else:
      possibleValues = uniqun(input,i)
    cardi.append([len(possibleValues),possibleValues]) # changing the nature of cardinality
  return cardi

def createCuboid(dimTup):
  #give me list of dimentions and I will give you cuboid corresponding to that dimention up till 4 dimentions
  if len(dimTup) == 0:
    return ['Aggregate',0]
  elif len(dimTup) == 1:
    return [' ' for i in range(dimTup[0])]
  elif len(dimTup) == 2:
    return [[' ' for j in range(dimTup[1])] for i in range(dimTup[0])]
  elif len(dimTup) == 3:
    subCuboid = [[[' ' for j in range(dimTup[2])] for i in range(dimTup[1])] for k in range(dimTup[0])]
    return subCuboid
  elif len(dimTup) == 4:
    subCuboid = [[[[' ' for j in range(dimTup[3])] for i in range(dimTup[2])] for k in range(dimTup[1])]for k in range(dimTup[0])]
    return subCuboid

def createDictionaryOfCuboids(numDims,dimNames,cardinality):
  #create a dictionary whose key is the concatination of dimentions and value is a correspondingly sized cuboid
  table = list(itertools.product([False, True], repeat=numDims)) 
  cuboids = {}
  for truthTableRow in table:
    cuboidName = ''
    dimentionOfCuboid = []
    for dimIndex in range(len(truthTableRow)):
      if  truthTableRow[dimIndex] == True:
        cuboidName += dimNames[dimIndex]
        dimentionOfCuboid.append(cardinality[dimIndex][0])
    #we formulate a name and dimention for cuboid correspoding to the current row

    if cuboidName == '':
      cuboidName = 'apex'
    
    #once we have name and dimention of the cuboid we create the cuboid and assignthat cuboid to a dictionary
    cuboids[cuboidName] = createCuboid(dimentionOfCuboid)
  return cuboids