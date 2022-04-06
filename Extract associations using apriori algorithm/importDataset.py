import csv
def importDataset(fileName):
    header = ""
    with open(fileName, newline='') as csvfile:
      spamreader = csv.reader(csvfile)
      data = []
      f = False
      for row in spamreader:
        if f == False:
          f = True
          header = row # header is removed
          continue
        temp = []
        for i in range(len(row)):
          temp.append(row[i])
        data.append(temp)
    return data,header