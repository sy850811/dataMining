import itertools
# Extract items out of dataset
def find_unique_items_from_datasets(data):
  candidateSet1 = set()
  for i in data:
    for j in i:
      candidateSet1.add(j)
  return [[i,0] for i in candidateSet1] # 0 if for storing the support

# Find support for the dataset using issubset property of sets
def find_support_for_an_itemset(itemset,dataset):
  count = 0
  for i in dataset:
    if set(itemset).issubset(set(i)):
      count +=1
  return count

# Find support for each itemset in a candidate
def find_support_of_itemSets_in_dataset(candidateSet,dataset):
  for i in candidateSet:
    i[-1] = find_support_for_an_itemset(i[:-1],dataset)
  return candidateSet

# eleminate itemsets from candidate sets for which the support is below the minimum
def eleminate_weak_itemsets(candidateSet,support):
  newCandidateSet = []
  for i in range(len(candidateSet)):
    if candidateSet[i][-1] >= support:
      newCandidateSet.append(candidateSet[i])
  return newCandidateSet

# join itemsets for which k-1 elements are same to form K-candidate set
def create_candidate_set_from_K_minus_1_itemset(candidateSetWithSupport1):
  cs = []
  for i in range(len(candidateSetWithSupport1)):
    for j in range(i+1,len(candidateSetWithSupport1)):
      if candidateSetWithSupport1[i][:-2] == candidateSetWithSupport1[j][:-2]:
        cs.append(candidateSetWithSupport1[i][:-1] + [candidateSetWithSupport1[j][-2]] + [0])
  return cs

#check if list of k-1 length subsets are present in L_k-1
def aprioriFilter(L_K_Minus_1,subsets):
  for i in subsets:
    found = False
    for itemset in L_K_Minus_1:
      if itemset[:-1] == list(i):
        found = True
        break
    if found == False:
      return False
  return True

# for each itemsets in candidateSet find subsets and pass them through aprioriFilter
def apriori(candidateSet,lkminus1):
  filteredCandidates = []
  for i in candidateSet:
    k = len(i) -1
    subSets = list(itertools.combinations(i[:-1], k-1))
    valid = aprioriFilter(lkminus1,subSets)
    if valid:
      filteredCandidates.append(i)
  return filteredCandidates

def extractFrequentItemsetsFromData(data,support):
  #the work for L_1 
  candidateSet1 = find_unique_items_from_datasets(data)
  candidateSetWithSupport1 = find_support_of_itemSets_in_dataset(candidateSet1,data)
  candidateSetWithSupport1 = eleminate_weak_itemsets(candidateSetWithSupport1,support)

  #place to store all itemsets which we will use for creating associations
  totalAssociations = [] + candidateSetWithSupport1

  #loop for finding all the frequent itemsets
  L_K_Minus_1 = candidateSetWithSupport1
  while len(L_K_Minus_1)!=0: # till there is no more items in an itemsets
    #findCandidateFrequentItemsets
    candidateSet = create_candidate_set_from_K_minus_1_itemset(L_K_Minus_1)
    candidateSetWithSupport = find_support_of_itemSets_in_dataset(candidateSet,data)
    #filter Apriori
    candidateAfterAprioriFilter = apriori(candidateSetWithSupport,L_K_Minus_1)
    # eleminate itemsets with not enough support
    if len(candidateAfterAprioriFilter) == 0:
      break
    L_K = eleminate_weak_itemsets(candidateAfterAprioriFilter,support)
    #store all found frequent itemsets
    totalAssociations.extend(L_K)
    L_K_Minus_1 = L_K
  return totalAssociations
