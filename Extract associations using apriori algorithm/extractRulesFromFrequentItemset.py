import itertools
from frequentItemsetExtraction import find_support_for_an_itemset
# from subsets of a frequent itemset extract rules and print/paste them in the  "Rules.txt" file
def printAssociation(a,b,s,c,fileName,data,header,ruleNo):
  with open(fileName, 'a') as write:
    print(a)
    strin = 'Rule#'+str(ruleNo)+': '
    first = True
    for item in a:
      if first:
        first = False
      else:
        strin =strin +', '
      for i in data:
        if item in i:
          index = i.index(item)
          strin += "{"+ header[index]+"="+item +"}"
          break
      
    strin += " => "
    first = True
    for item in b:
      if first:
        first = False
      else:
        strin =strin +', '
      for i in data:
        if item in i:
          index = i.index(item)
          strin += "{"+ header[index]+"="+item +"}"
          break  
    write.write(strin+"\n")
    write.write("(Support="+str(round(s,2))+", Confidence="+str(round(c,2))+")\n\n")

#extract association rules from frequent itemsets
def extractAssociationRules(fileName,totalAssociations,min_conf,support,data,header):
  with open(fileName, 'w') as write:
    pass
  with open(fileName,'a') as write:
    '''1. User Input: 
        Support=0.30 
        Confidence=0.60
       2. Rules:'''
    write.write("1. User Input:\n\n")
    write.write("Support="+str(support)+"\n")
    write.write("Confidence="+str(min_conf)+"\n\n")
    write.write("2. Rules:\n\n")
  ruleNo = 0
  #find association rules from frequent itemset usign generative apporach
  for i in totalAssociations: #For each itemset I
    if len(i) == 1:
      continue
    table = list(itertools.product([False, True], repeat= len(i) - 1))
    del table[0]
    del table[-1]
    supportForAUB = i[-1] # support for A U B
    for j in range(len(table)):
      a = []
      b = []
      for k in range(len(table[j])): # find S and I-S
        if table[j][k] == True:
          a.append(i[k])
        else: 
          b.append(i[k])

      # find support for A
      supportForA = find_support_for_an_itemset(a,data) # Support for A
      # calculate confidence and verfy if its greater than threshold
      if supportForA > 0 and supportForAUB/supportForA >= min_conf:
        c = supportForAUB/supportForA
        s = supportForAUB/len(data)
        ruleNo +=1
        printAssociation(a,b,s,c,fileName,data,header,ruleNo)
        #create a ReadME file
