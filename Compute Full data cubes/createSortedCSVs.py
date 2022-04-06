import csv #used for importing the data in Car_Sales_Data_Set.csv
from sorting import mergeSort # custom implementation of merge sort is imported here

def storeSortedData(fileName,fields,rows):
    # this function stores the given data with the given filename, Headings, and records/rows
  with open(fileName, 'w') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(rows)

def createSortedCSV(fileName,nameList):
    #here we read firstly read the dataset that we have to sort 
    header = ""
    with open(fileName, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        data = []
        f = False
        for row in spamreader:
            if f == False:
                f = True
                header = row #extract texual headings
                continue
            data.append([row[0],
                        int(row[1]),
                        int(row[2]),
                        row[3],
                        int(row[4])])
    # data to be sorted is now fetched
    arr = data
    #Now we begin sorting data with respect to the #dimention-Country at 0th column, #dimention-Year 1st column, #dimention-Quarter 2nd column 
    arr = mergeSort(arr,0) #sorting with respect to country
    storeSortedData(nameList[0],header,arr) # store the countrywise sorted array
    for j in range(1,3):
        s = 0
        e = len(arr)
        currentElement = arr[0][j-1]
        for i in range(len(arr)):
            if currentElement != arr[i][j-1]:
                arr[s:i] = mergeSort(arr[s:i],j) # sorting with respect to year and quarter in first and second iteration respectively
                s = i
                currentElement = arr[i][j-1]
        arr[s:e] = mergeSort(arr[s:e],j)
        storeSortedData(nameList[j],header,arr) # store the sorted array 
    return arr # return the extracted data to perform further OLAP operations
