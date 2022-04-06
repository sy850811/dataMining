#This class is just to make fancy captions and bold cuboid table headings defining fonts and colors
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def print2(cuboid):
    # this function prints 2d cuboid
  for i in range( len( cuboid) ):
    for j in range( len ( cuboid[i]) ):
      if i==0 or j == 0:
        print(color.BOLD + "{:^20}|".format(cuboid[i][j]) + color.END,end='')
      else:
        print("{:^20}|".format(cuboid[i][j]),end='')
    print()

def index_2d(myList, v):
    #find index of an element in a list
  for i in range(len(myList)):
    if myList[i][0] == v:
      return i

def uniq(arr,index):
    # here we identify the unique values for each dimention like "Canada , US " in case of dimention country
  s = []
  for i in arr:
    if i[index] not in s:
      s.append(i[index])
  return s

######################################################
#Below this point 11 functions associated to each requested cuboid is implemented

#In each function we : 
# a) print a caption
# b) Figure out the shape of cuboid and initialise it with zero
# c) Traverse the dataset once and based on teh record of the sample we update corresponding elements of the cuboid
# d) Finally the generated cuboid in printed
######################################################
def empty(arr):
  print("\t\t"+color.BOLD +color.UNDERLINE+color.DARKCYAN+ "This is apex cuboid of zero dimention." + color.END+"\n\n") 
  heading0 = ["Sales"]
  cuboid =[heading0,[0]]
  for i in arr:
    cuboid[1][0]+=int(i[4])
  print2(cuboid)

def country(arr):
    countries = uniq(arr,0)
    print("\t\t"+color.BOLD +color.UNDERLINE+color.DARKCYAN+ "This cuboid is of one dimention. (Country" + color.END+"\n\n")
    cuboid = [[i,0] for i in countries]
    for i in arr:
        ci = countries.index(i[0])
        cuboid[ci][1] = cuboid[ci][1] + i[4]
    cuboid.insert(0,[" "*20,"Sales"])
    print2(cuboid)

def timeYear(arr):
    years = uniq(arr,1)
    print("\t\t"+color.BOLD +color.UNDERLINE+color.DARKCYAN+ "This cuboid is of one dimention. (Time( Hierarchy : years) " + color.END+"\n\n")
    cuboid = [[i,1] for i in years]
    for i in arr:
        ci = years.index(i[1])
        cuboid[ci][1] = cuboid[ci][1] + i[4]
    cuboid.insert(0,[" "*20,"Sales"])
    print2(cuboid)

def carManufacturer(arr):
    carManufacturers = uniq(arr,3)
    print("\t\t"+color.BOLD +color.UNDERLINE+color.DARKCYAN+ "This cuboid is of one dimention. (Car Manufacturer) " + color.END+"\n\n")
    cuboid = [[i,3] for i in carManufacturers]
    for i in arr:
        ci = carManufacturers.index(i[3])
        cuboid[ci][1] = cuboid[ci][1] + i[4]
    cuboid.insert(0,[" "*20,"Sales"])
    print2(cuboid)

def timeQuarterTimeYear(arr):
    quarters = uniq(arr,2)
    years = uniq(arr,1)
    timeQuarterTimeYears = [''+str(j)+'-'+str(i) for j in quarters for i in years]
    print("\t\t"+color.BOLD +color.UNDERLINE+color.DARKCYAN+ "This cuboid is of one dimention. (Time(Hierarchy : Quarter-years)) " + color.END+"\n\n")
    cuboid = [[''+str(j)+'-'+str(i),0] for j in quarters for i in years] #change this later the way of calculating this cuboid generation leveraging timeQuarterTimeYears variable 
    for i in arr:
        ci = index_2d(cuboid,''+str(i[2])+'-'+str(i[1]))
        cuboid[ci][1] = cuboid[ci][1] + i[4]
    cuboid.insert(0,[" "*20,"Sales"])
    print2(cuboid)

def country___timeYear(arr):
    countries = uniq(arr,0)
    years = uniq(arr,1)
    print("\t\t"+color.BOLD +color.UNDERLINE+color.DARKCYAN+ "This cuboid is of two dimention. (Country x Time( Hierarchy : years)) " + color.END+"\n\n")
    cuboid = [[i]+[0 for j in years] for i in countries]
    for i in arr:
        country = i[0]
        year = i[1]
        ci = countries.index(country)
        yi = years.index(year)
        cuboid[ci][yi+1] += i[4]
    h = [" "*20] + years
    cuboid.insert(0,h)
    print2(cuboid)

def country___timeQuarterTimeYear(arr):
    countries = uniq(arr,0)
    years = uniq(arr,1)
    quarters = uniq(arr,2)
    timeQuarterTimeYears = [''+str(j)+'-'+str(i) for j in quarters for i in years]
    print("\t\t"+color.BOLD +color.UNDERLINE+color.DARKCYAN+ "This cuboid is of two dimention. (Country x Time(Hierarchy :Quarte-years)) " + color.END+"\n\n")
    cuboid = [[i]+[0 for j in timeQuarterTimeYears] for i in countries]

    for i in arr:
        country = i[0]
        tqTy = str(i[2]) + '-' + str(i[1])
        ci = countries.index(country)
        tqTyi = timeQuarterTimeYears.index(tqTy)
        cuboid[ci][tqTyi+1] += i[4]
    h = [" "*20] + timeQuarterTimeYears
    cuboid.insert(0,h)
    print2(cuboid)

def country___carManufacturer(arr):
    countries = uniq(arr,0)
    carManufacturers = uniq(arr,3)
    print("\t\t"+color.BOLD +color.UNDERLINE+color.DARKCYAN+ "This cuboid is of two dimention. (Country x Car Manufacturer) " + color.END+"\n\n")
    cuboid = [[i]+[0 for j in carManufacturers] for i in countries]

    for i in arr:
        country = i[0]
        carManufacturer = i[3]
        # print(country,carManufacturer)
        ci = countries.index(country)
        cmi = carManufacturers.index(carManufacturer)
        cuboid[ci][cmi+1] += i[4]
    h = [" "*20] + carManufacturers
    cuboid.insert(0,h)
    print2(cuboid)

def timeYear___carManufacturer(arr):
    years = uniq(arr,1)
    carManufacturers = uniq(arr,3)
    print("\t\t"+color.BOLD +color.UNDERLINE+color.DARKCYAN+ "This cuboid is of two dimention. (Time(Hierarchy :years) x Car Manufacturer) " + color.END+"\n\n")
    cuboid = [[i]+[0 for j in carManufacturers] for i in years]

    for i in arr:
        year = i[1]
        carManufacturer = i[3]
        # print(country,carManufacturer)
        ci = years.index(year)
        cmi = carManufacturers.index(carManufacturer)
        cuboid[ci][cmi+1] += i[4]
    h = [" "*20] + carManufacturers
    cuboid.insert(0,h)
    print2(cuboid)

def timeQuarterTimeYear___carManufacturer(arr):
    quarters = uniq(arr,2)
    years = uniq(arr,1)
    carManufacturers = uniq(arr,3)
    timeQuarterTimeYears = [''+str(j)+'-'+str(i) for j in quarters for i in years]
    print("\t\t"+color.BOLD +color.UNDERLINE+color.DARKCYAN+ "This cuboid is of two dimention. (Time(Hierarchy :Quarter-years) x Car Manufacturer) " + color.END+"\n\n")
    cuboid = [[i]+[0 for j in carManufacturers] for i in timeQuarterTimeYears]

    for i in arr:
        tqTy = str(i[2]) + '-' + str(i[1])
        carManufacturer = i[3]

        tqTyi = timeQuarterTimeYears.index(tqTy)
        cmi = carManufacturers.index(carManufacturer)
        cuboid[tqTyi][cmi+1] += i[4]
    h = [" "*20] + carManufacturers
    cuboid.insert(0,h)
    print2(cuboid)

def country___timeYear___carManufacturer(arr):
    countries = uniq(arr,0)
    years = uniq(arr,1)
    carManufacturers = uniq(arr,3)
    print("\t\t"+color.BOLD +color.UNDERLINE+color.DARKCYAN+ "This cuboid is of three dimention. (Country x Time(Hierarchy :years) x Car Manufacturer) " + color.END+"\n\n")
    subCuboid = [ [i] + [0 for j in carManufacturers] for i in years]
    h = [" "*20] + carManufacturers
    subCuboid.insert(0,h)
    cuboid = [subCuboid for k in countries]
    for i in arr:
        country = i[0]
        year = i[1]
        carManufacturer = i[3]
        ci = countries.index(country)
        yi = years.index(year)
        cmi = carManufacturers.index(carManufacturer)
        cuboid[ci][yi+1][cmi+1] += i[4]
    for i in range(len(cuboid)):
        print(color.BOLD + countries[i] + " : " + color.END)
        print2(cuboid[i])
        print("\n\n")

def country___timeQuarterTimeYear___carManufacturer(arr):
    quarters = uniq(arr,2)
    years = uniq(arr,1)
    countries = uniq(arr,0)
    carManufacturers = uniq(arr,3)
    timeQuarterTimeYears = [''+str(j)+'-'+str(i) for j in quarters for i in years]
    print("\t\t"+color.BOLD +color.UNDERLINE+color.DARKCYAN+ "This cuboid is of three dimention. (Country x Time(Hierarchy :quarter-years) x Car Manufacturer) " + color.END+"\n\n")
    subCuboid = [[i] +[0 for j in carManufacturers] for i in timeQuarterTimeYears]
    h = [" "*20] + carManufacturers
    subCuboid.insert(0,h)
    cuboid = [subCuboid for k in countries]
    for i in arr:
        country = i[0]
        tqTy = str(i[2]) + '-' + str(i[1])
        carManufacturer = i[3]
        ci = countries.index(country)
        tqTyi = timeQuarterTimeYears.index(tqTy)
        cmi = carManufacturers.index(carManufacturer)
        cuboid[ci][tqTyi+1][cmi+1] += i[4]
    for i in range(len(cuboid)):
        print(color.BOLD + countries[i] + " : " + color.END)
        print2(cuboid[i])
        print("\n\n")