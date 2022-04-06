
#custom Function imports
from importDataset import importDataset

from frequentItemsetExtraction import extractFrequentItemsetsFromData

from extractRulesFromFrequentItemset import extractAssociationRules
#math liabrary for rounding off
import math

def main():
  #step1: import data
  data,header = importDataset('Play_Tennis_Data_Set.csv')
  #step 2: ask for support and confidence
  min_sup = float(input("Enter the minimum support threshold : " ))
  support = math.ceil(float(min_sup * len(data)))
  min_conf = float(input("Enter the minimum confidence threshold : "))
  #step 3: Find frequent Itemset
  totalAssociations = extractFrequentItemsetsFromData(data,support)
  print("List of total Frequent Itemsets with support greater than",support)
  print(totalAssociations)
  #step 4: Find associations from the itemset and store them in Rules.txt
  fileName = "Rules.txt"
  extractAssociationRules(fileName,totalAssociations,min_conf,min_sup,data,header)





if __name__ == "__main__":
    main()