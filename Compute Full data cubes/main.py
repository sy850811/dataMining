from createSortedCSVs import createSortedCSV # This file contains methords responsible for sorting the dataset as required
from cuboidFunctions import empty,country,timeYear,timeQuarterTimeYear,carManufacturer,country___timeYear,country___timeQuarterTimeYear,country___carManufacturer,timeYear___carManufacturer,timeQuarterTimeYear___carManufacturer,country___timeYear___carManufacturer,country___timeQuarterTimeYear___carManufacturer
#the above imports are the functions that compute each cuboid


def main():
    originalList = 'Car_Sales_Data_Set.csv' #dataset
    SortedNameList = ["Car_Sales_Data_Set_First_Sorting.csv","Car_Sales_Data_Set_Second_Sorting.csv","Car_Sales_Data_Set_Third_Sorting.csv"] #name of sorted csv's we will be generating
    arr = createSortedCSV(originalList,SortedNameList) # this function a) Loads the dataset b) Uses concept of merge sort to perform sorting and storing the sorted data in new CSV files
    #arr contains nothing but the dataset

# OLAP operations Menu
    while True:
        print('''
        1. ()
        2. (Country)
        3. (Time_Year)
        4. (Time_Quarter - Time_Year)
        5. (Car_ Manufacturer)
        6. (Country, Time_Year)
        7. (Country, Time_Quarter - Time_Year)
        8. (Country, Car_ Manufacturer)
        9. (Time_Year, Car_ Manufacturer)
        10. (Time_Quarter - Time_Year, Car_ Manufacturer)
        11. (Country, Time_Year, Car_ Manufacturer)
        12. (Country, Time_Quarter - Time_Year, Car_ Manufacturer)

        Press any other key to Exit''')
        
        c = int(input())
        if c == 1:
            empty(arr)
        elif c == 2:
            country(arr)
        elif c == 3:
            timeYear(arr)
        elif c == 4:
            timeQuarterTimeYear(arr)
        elif c == 5:
            carManufacturer(arr)
        elif c == 6:
            country___timeYear(arr)
        elif c == 7:
            country___timeQuarterTimeYear(arr)
        elif c == 8:
            country___carManufacturer(arr)
        elif c == 9:
            timeYear___carManufacturer(arr)
        elif c == 10:
            timeQuarterTimeYear___carManufacturer(arr)
        elif c == 11:
            country___timeYear___carManufacturer(arr)
        elif c == 12:
            country___timeQuarterTimeYear___carManufacturer(arr)
        else:
            break

if __name__ == "__main__":
    #let the show begin
    main()
