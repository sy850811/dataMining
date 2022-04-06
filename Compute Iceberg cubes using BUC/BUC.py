from sort import mergeSort # Before making partition we use this sort methord
from fileHandling import readCsv,writeResult #readCSV function reads the dataset, writeResult writes the cuboids in a text file
from helpers import aggregate,findCardinality,createDictionaryOfCuboids # aggregate -> aggregates the sales, findCardinality finds the no. of unique values, createDictionaryOfcuboids create a dictionary containing lattice of cuboids
from appendHeadersToResult import Item,ItemLocation,ItemLocationYear # we modify the interested cuboids (rearrange rows as computer should come before camera,append headers to rows and columns, in 3d cuboids change cuboid such that Year is first dimention )


header,data = readCsv('Product_Sales_Data_Set.csv') #now we have data and we hace headers(dimention + measure names)
print("Enter the value for minimum support please - ")
minSupport = int(input()) # ask user for minimum support for our iceberg cubes
numDims = len(data[0]) -1 #no of dimentions
cardinality = findCardinality(data,numDims,s=True) # find the number of unique values for each dimention 
cardinalityUn = findCardinality(data,numDims,s=False)# finding the order in which unique values appear in the dataset as required by assignmetnt description
outputRec = [] # records the partition being explored explored 
dimNames = header 
cuboids = createDictionaryOfCuboids(numDims,dimNames,cardinality) # dictionary of cuboids have been 

def partition(input, dim, cardinality,possibleValues):
  #this function tells in our input, where does each partition begins for each unique value(possibleValues)and where it ends for a given dimention

  input = mergeSort(input,dim) #. For ease of partition data is sorted
  count = [0] * cardinality  #variable holds.. how many rows for a given partition
  correspondingSales = [0] * cardinality # sales value ForIndividual Partition

  for row in range(len(input)):
    value = input[row][dim]
    index = possibleValues.index(value)
    sales = input[row][-1]
    count[index] +=1
    correspondingSales[index] += sales

  return count,correspondingSales # returns the size of each partition and sales corresponding to each partition

def cuboidName_and_correspondingAggregateCellIndex(outputRec): # once we have an aggregate cell that satisfies the minSupport we need
  # to store it.This function resolves the cuboid in which we need
  # # to place aggregate cell and withen that cuboid the index of that cell
  cuboidName = ''
  dimentionSValueIndex = []
  for iter in outputRec:
    search = iter
    for i in range(len(cardinality)):
      if search in cardinality[i][1]:
        dimentionSValueIndex.append(cardinality[i][1].index(search))
        cuboidName+= dimNames[i]
        break
  return cuboidName,dimentionSValueIndex

def assignValueToCuboid(cuboidName,dimentionSValueIndex,all):
  #Once we resolve the cuboid and its index we place the aggregate value in corresponding cuboid in this function
  if cuboidName == '':
    cuboidName = 'apex'
    cuboids[cuboidName] = all
  else:
    a = cuboids[cuboidName]
    for i in range(len(dimentionSValueIndex)-1):
      a= a[dimentionSValueIndex[i]]
    a[dimentionSValueIndex[-1]] = all

def BUC(input,dim):
  # the main recursive algorithm to calculate the iceberg cube pertaining to minimum support 
  all = aggregate(input) # calculate aggregate value
  #store aggregate cell
  cuboidName,dimentionSValueIndex = cuboidName_and_correspondingAggregateCellIndex(outputRec)
  assignValueToCuboid(cuboidName,dimentionSValueIndex,all)
  # explore the remaining dimentions
  for d in range(dim,numDims):
    C = cardinality[d][0] 
    #perform partition
    dataCount,correspondingSales = partition(input,dim=d,cardinality= C,possibleValues= cardinality[d][1]) 
    k = 0 # represents starting index of partition which is being currently consider
    for i in range(C):
      c = dataCount[i] # partition  size
      if correspondingSales[i] >= minSupport: # minSup condition check
        outputRec.append(input[k][d])
        BUC(input[k:k+c],d+1) #########BUC recursive call
        outputRec.pop()
      k +=c 

def main():

  BUC(data[:],0) #BUC call
  it,one,yTick = Item(cuboids,data,numDims,cardinality,cardinalityUn,header) # do formatting for ITEM cuboid
  jt,two = ItemLocation(cuboids,data,numDims,cardinalityUn,it,header,yTick) # do formatting for ItemLocation cuboid
  jt,three = ItemLocationYear(cuboids,cardinality,cardinalityUn,header,numDims,data,it,jt) # do formatting for ItemLocationYear cuboid
  fileName = "Iceberg-Cube-Results.txt"
  writeResult(fileName,one,two,three,it,jt,yTick = cardinality[header.index('Year')][1]) # write the formatted cuboids in the text file

if __name__ == "__main__":
    main()